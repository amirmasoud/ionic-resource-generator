#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import math
import json
from PIL import Image
from termcolor import colored

# Read config.josn. All general config files are in this file. you can change 
# them to reflect your custom settings for generated output.
with open('config.json') as data_file:    
    data = json.load(data_file)

# Total steps to be passed. It's sum of the icons and splashed that needed to be
# generate.
steps = len(data["android"]["icon"]) + len(data["android"]["splash"]) + \
        len(data["ios"]["icon"]) + len(data["ios"]["splash"]) + \
        len(data["windows"]["splash"]) + len(data["windows"]["icon"])

# Current step
step = 0

def progress():
    global step
    """ Print progress
    """
    sys.stdout.write('\r')
    sys.stdout.write("[%d/%d]  ✔ " % (step, steps))
    sys.stdout.flush()
    step += 1

def end_log(i):
    """ Print end of a step.

    Keyword arguments:
    i -- information about generated image
    """
    global step
    progress()
    print colored(i["name"] + ' ' + str(i["width"]) + 'x' + str(i["height"]), 'green')

def start_log(i):
    """ Print start of a step.

    Keyword arguments:
    i -- information about generated image
    """
    print colored('Generating ' + i["name"] + ' ' + str(i["width"]) + 'x' + str(i["height"]), 'yellow')

def crop(image, width, height):
    """ Crop an image with given width and height.

    Keyword arguments:
    image -- image to crop
    width -- width of cropped image
    height -- height of cropped image
    """
    size = max(width, height)
    image = image.resize((size, size), Image.ANTIALIAS)
    image = image.crop(
        (
            (image.size[0] / 2) - (width /2), 
            (image.size[1] / 2) - (height/2), 
            (image.size[0] / 2) + (width /2), 
            (image.size[1] / 2) + (height/2)
        )
    )
    return image

def dirs():
    """ Create base directories to export Icons and Splashes
    """

    # iOS base path
    ios_icon_path = data["ios_path"] + '/icon'
    ios_splash_path = data["ios_path"] + '/splash'

    # iOS icon path
    try: 
        os.makedirs(ios_icon_path)
    except OSError:
        if not os.path.isdir(ios_icon_path):
            raise
    
    # iOS splash path
    try: 
        os.makedirs(ios_splash_path)
    except OSError:
        if not os.path.isdir(ios_splash_path):
            raise

    # Android base path
    android_icon_path = data["android_path"] + '/icon'
    android_splash_path = data["android_path"] + '/splash'

    # Android icon path
    try: 
        os.makedirs(android_icon_path)
    except OSError:
        if not os.path.isdir(android_icon_path):
            raise

    # Android splash path
    try: 
        os.makedirs(android_splash_path)
    except OSError:
        if not os.path.isdir(android_splash_path):
            raise

    # Windows base path
    windows_icon_path = data["windows_path"] + '/icon'
    windows_splash_path = data["windows_path"] + '/splash'

    # Windows icon path
    try: 
        os.makedirs(windows_icon_path)
    except OSError:
        if not os.path.isdir(windows_icon_path):
            raise

    # Windows splash path
    try: 
        os.makedirs(windows_splash_path)
    except OSError:
        if not os.path.isdir(windows_splash_path):
            raise
    pass