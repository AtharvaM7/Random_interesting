'''
This program has a simple metronome feature.
'''
import time
import winsound
import os

def time_tapping():
    ''' This function analyses if the user is tapping in time with the metronome. '''
    # Ask the user for tempo and time signature
    tempo = int(input('Enter the tempo in BPM: '))
    time_signature = input('Enter the time signature: ')
    # Calculate the time between beats
    time_between_beats = 60 / tempo


