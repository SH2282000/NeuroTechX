import time

import mido as mido
import numpy as np
from pylsl import StreamInfo, StreamOutlet

from frontend import create_app

# app = create_app()


def main():
    info_stimulus = StreamInfo('OpenBCIStimulus', 'Markers', 9, 0, 'string', 'myuidw43536')

    outlet_sti = StreamOutlet(info_stimulus)

    """
    Initial tempo/velocity
    Given task (shown to the user) - immediately shown, in parallel with the tempo beating
    Final tempo/velocity (audible by the user): slowing down or speeding up or staying the same (3 possible states)
    Delay before the behavior kicks in - 1s?
    Duration of the trial - 5s?
    User identity
    """

    user_id = "0"

    time.sleep(5)

    behavior_delays = np.linspace(1, 2, 10)
    trial_duration = 4

    tempo_range = np.linspace(1, 5, 30)
    velocity_range = np.linspace(20, 110, 10)
    task_kinds = ['tempo', 'velocity']
    tasks = {'tempo': ['up', 'down', 'neutral'],
             'velocity': ['up', 'down', 'neutral']}

    task_labels = {
        'tempo': {'up': 'faster', 'down': 'slower', 'neutral': 'N'},
        'velocity': {'up': 'louder', 'down': 'quieter', 'neutral': 'N'},
    }

    coeff = {'up': 1.15, 'down': 0.8, 'neutral': 1}
    quiet_time = 1


    def generate_trial():
        task_kind = np.random.choice(task_kinds)
        task = np.random.choice(tasks[task_kind])
        behavior = np.random.choice(tasks[task_kind])
        behavior_delay = np.random.choice(behavior_delays)
        init_velocity = np.random.choice(velocity_range)
        init_tempo = np.random.choice(tempo_range)
        final_tempo = init_tempo if task_kind == 'velocity' else init_tempo * coeff[task]
        final_velocity = init_velocity if task_kind == 'tempo' else init_tempo * coeff[task]
        return init_tempo, final_tempo, init_velocity, final_velocity, task, task_kind, behavior, behavior_delay


    print(mido.get_output_names())
    midi_device = mido.get_output_names()[0]
    midi_out = mido.open_output(midi_device)

    def sequencer_callback(time, pitch, velocity, debug=False):
        if debug:
            print(time, pitch, velocity)
        midi_out.send(mido.Message('note_on', note=pitch, velocity=0))
        midi_out.send(mido.Message('note_on', note=pitch, velocity=velocity))


    while True:
        trial = generate_trial()
        init_tempo, final_tempo, init_velocity, final_velocity,\
        task, task_kind, behavior, behavior_delay = trial

        trial_config = list(map(str, [user_id, *trial]))
        print(trial_config)

        outlet_sti.push_sample(trial_config)

        t = 0.0
        tempo = init_tempo
        velocity = int(init_velocity)
        
        print(f'{task_labels[task_kind][task]}')
        
        while t < trial_duration:


            if t > behavior_delay:
                if task == 'tempo':
                    tempo = init_tempo + (final_tempo - init_tempo) * (t >= behavior_delay) * (t - behavior_delay) / (trial_duration - behavior_delay)
                elif task == 'velocity':
                    velocity = int(init_velocity + (final_velocity - init_velocity) * (t >= behavior_delay) * (t - behavior_delay) / (trial_duration - behavior_delay))

            sequencer_callback(None, 60, velocity, debug=False)

            time.sleep(1 / tempo)
            t += 1 / tempo

        time.sleep(1)


if __name__ == "__main__":
    # app.run(debug=True)
    main()