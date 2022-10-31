# MindMusic - NeuroTechX
## Project made for the NeuroTechX hackaton.

It's easy to listen to music (cf. Spotify), but still hard to play something that really fit our mood.​ This proect emphasis around ways to create, pitch and modulate musical pieces in real time, with relation to the neuro-feedbacks of our brain. 

In order to create a personnal experience, the app have two modes: 
 - Recording: This mode allows to train the neural network to our music feedback (Signals from the channels) and be set for the Experiencing mode.
 - Experiencing: In this mode, the models are trained (weighted) to our feedbacks and the music is playing w.r.t. our feelings.


## How to build? 

To clone this repository, run the following command:
```
    git clone git@github.com:SH2282000/NeuroTechX.git
```

You must install `poetry` and `npm` on your system. Then follow this installation procedure:
```
    poetry config virtualenvs.create true
    poetry config virtualenvs.in-project true

    pyenv shell 3.8.10
    poetry env use $(pyenv which python)
    poetry install # from this moment on, you can execute any commands in our virtual environment.

    # To start the frontend user-friendly interface, do the following:
    cd frontend 
    npm start
```

To build the project go into **file** > **Build and Run** and select the destination of the executable file.

## Preview 

Here's a **preview video** of the game running on a mac.
<p align="center">
 <a href="https://youtu.be/vh3UYR2Gg8w">
  <img width="782" alt="Screenshot 2022-10-31 at 09 22 20" src="https://user-images.githubusercontent.com/16389789/198963614-06b34207-708a-4e22-a88e-536ce1c10c05.png">

 </a>
</p>

### Screenshots

<img width="1262" alt="Screenshot 2022-10-31 at 09 20 47" src="https://user-images.githubusercontent.com/16389789/198963262-73e6b9cf-60b8-443f-887a-59a55c30a994.png">


Highest enjoyment of music is experienced during an engaged state of flow. ​(Audio) feedback pulls one in.​ Let's make musical expression as accessible as music listening by letting the user focus on the music and leaving the performance technique to the system.​

We aim to convert EEG signals to performance control parameters which feed a real-time performance renderer, ideally using supervised training.​

## Contributors
### GROUP "Mind Music" (Contributors)
 - Vladimir Viro
 - Tobias Fischer
 - Shannah Santucci
 - Daniel Lindenblatt

[![](https://contrib.rocks/image?repo=SH2282000/NeuroTechX)](https://github.com/SH2282000/NeuroTechX/graphs/contributors)


### Repartition of the Workload
<table>
  <tbody>
    <tr>
      <th align="center">Contirbutors</th>
      <th align="center">WORKLOAD</th>
    </tr>
    <tr>
      <td align="center">Vladimir</td>
      <td align="left">
        <ul>
          <li>Creating the concept</li>
          <li>Hardware manager (Cyton board)</li>
          <li>Musical designer</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td align="center">Tobias</td>
      <td align="left">
        <ul>
          <li>Main logic (Python)</li>
          <li>Team binder</li>
          <li>Git management (GIT)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td align="center">Shannah</td>
      <td align="left">
        <ul>
          <li>FrontEnd development</li>
          <li>Virtual environment manager</li>
          <li>Interfacing following MVC model</li>
          <li>User-frindly in-browser app designer</li>
          <li>General bug fixes python</li>
        </ul>
      </td>
    </tr>
        <tr>
      <td align="center">Daniel</td>
      <td align="left">
        <ul>
          <li>Main logic (Python)</li>
          <li>Git management (GIT)</li>
          <li>Handling documentation</li>
          <li>Slides</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Other ressources
 - Hardware (OpenBCI): Ultracortex Mk IV, Cyton + Daisy boards (16 EEG ch.)​
 - Software: brainflow, LabRecorder [EEG recording];​
 - Peachnote for the musical performance renderer https://peachnotde.de ​
 - Pianoteq for piano sound rendering https://pianoteq.com 
