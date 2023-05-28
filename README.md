# Disc Ripper

## Dependencies
**Python modules:** subprocess, caffeine, sys, os

caffeine can be installed by using `pip3 install caffeine`, the others should already be part of your Python install.

**Command Line Applications:** makemkvcon, HandBrakeCLI

## Preamble
I made this script so that I could automate the task of ripping and compressing all my dvds and blurays to my plex server. Doing it manually was painful.

The documentation for makemkvcon particularly is quite lacking, and doesn't seem to have all the same functionality as the gui, atleast it isn't obvious.

This script is optimised to run on a Mac, feel free to fork it and make it better to suit your needs.

Keep in mind, this is a janky script that I wrote to be optimised for my particular situation, so it most definitely isn't perfect!

## How do I use it?
1. `python3 rip-disc.py`

2. Follow the prompts

3. That's it..

## How it works
1. The script starts by using makemkvcon to read all the available titles and display them as an easy to read list in the terminal. The title ID column indicates the index by which each title is associated.

2. Following this, the user is prompted to enter the titles that they want to rip. This can be done in three ways:
  - The user can choose to rip all titles by explicitly passing the argument `all`.
  - The user can choose to rip specific titles by passing a comma separated string of the Title ID's to be ripped as the argument, e.g., `1,5,6,9`.
  - The user can choose to rip a sequential block of titles by passing a hyphen separated interval string of the Title ID's to be ripped as the argument, e.g., `2-5`.

3. The user will be prompted to enter the directory in which they would like for the output to be saved. To save in the current working directory, pass `.` as the directory argument, otherwise, pass the full path of the directory to save in to.

4. The script will iterate sequentially over each title on the disc and rip it. As soon as a title is ripped, a new detached process will be created to compress it using the "Fast 1080p30" setting in HandBrake.

5. Once complete, the script will open the disc drive.

## Notes
- Step three in it's current form won't work, I have only tested it so far using the current working directory. I haven't specified directories elsewhere, and so this is something that I will need to fix in the future.

- I plan on using Tkinter to open a gui window to make directory selection easier.

- If the user selects `all` to rip, then these won't be compressed, I haven't figured this one out yet, so it's probably best to use the entire interval if you want to rip everything, i.e., `n-m`. I'll fix this in due course.