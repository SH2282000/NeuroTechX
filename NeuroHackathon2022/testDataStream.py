# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:01:06 2022

@author: Topotu
"""

import psychtoolbox as ptb
from pyOpenBCI import OpenBCICyton
from pylsl import StreamInfo, StreamOutlet, local_clock
import numpy as np
# import os
# import glob

SCALE_FACTOR_EEG = (4500000) / 24 / (2 ** 23 - 1)  # uV/count
SCALE_FACTOR_AUX = 0.002 / (2 ** 4)

info_eeg = StreamInfo('OpenBCIEEG', 'EEG', 16, 125, 'float32', 'OpenBCIEEG')

print("Creating LSL stream for AUX. \nName: OpenBCIAUX\nID: OpenBCIEEG\n")

info_aux = StreamInfo('OpenBCIAUX', 'AUX', 3, 125, 'float32', 'OpenBCIAUX')

outlet_eeg = StreamOutlet(info_eeg)
outlet_aux = StreamOutlet(info_aux)

print(local_clock(), ptb.GetSecs())

def lsl_streamers(sample):
    outlet_eeg.push_sample(np.array(sample.channels_data) * SCALE_FACTOR_EEG)
    outlet_aux.push_sample(np.array(sample.aux_data) * SCALE_FACTOR_AUX)

board = OpenBCICyton(port='COM3', daisy=True)

print('starting stream')
board.start_stream(lsl_streamers)