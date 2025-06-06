# constants.py defines parameters and settings for an experiment
# it is passed to the Experiment class on initialization
from pathlib import Path
import os
import MultiTaskBattery as mtb

#Necessary definitions for the experiment:
exp_name = '7TP' # name of the experiment

#UNCOMMENT THIS FOR SCANNING
# response_keys    = ['y', 'g', 'r', 'm'] # scanner keys

#COMMENT THIS FOR SCANNING
response_keys    = ['a', 's', 'k', 'l']

#not used
response_fingers = ['Pinky', 'Ring','Middle', 'Index']

# Directory definitions for experiment
exp_dir = Path(os.path.dirname(os.path.realpath(__file__)))   # where the experiment code is stored
task_dir = exp_dir / "task_files"  # contains target files for the task
run_dir    = exp_dir / "run_files"     # contains run files for each session
data_dir   = exp_dir / "data"          # This is where the result files are being saved

# do run_file_name as a formated string
default_run_filename = 'run_{}.tsv'

# This is were the stimuli for the different task are stored
package_dir = Path(__file__).resolve().parents[2]
stim_dir   = package_dir / "stimuli"

# Is the Eye tracker being used?
eye_tracker = False                                     # do you want to do  eyetracking?

# Running in debug mode?
debug = False                                           # set to True for debugging

# Screen settings for subject display
screen = {}
screen['size'] = [1100, 800] # screen resolution
screen['fullscr'] = False        # full screen, if false it's in a separate window
screen['number'] = 0                # 0 = main display, 1 = secondary display
