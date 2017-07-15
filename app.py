from termcolor import colored
from helper import *
from PIL import Image
import json
import sys

print colored('starting...', 'green')

# Read config.josn. All general config files are in this file. you can change 
# them to reflect your custom settings for generated output.
with open('config.json') as data_file:    
    data = json.load(data_file)

progress()

# Create directories
dirs()

# Generate icons
src = Image.open('icon.png')
for i in data["android"]["icon"]:
    start_log(i)
    image = src.resize((i["width"], i["height"]), Image.ANTIALIAS)
    name = data["android_path"] + 'icon/' + i["name"] + '.png'
    image.save(name, 'png')
    end_log(i)

for i in data["windows"]["icon"]:
    start_log(i)
    size = min(i["width"], i["height"])
    image = src.resize((size, size), Image.ANTIALIAS)
    # Windows needs wide icons. Add transparent padding around the area.
    background = Image.new('RGBA', (i["width"], i["height"]), (0, 0, 0, 1))
    background.paste(image, ((i["width"]/2) - (image.size[0]/2), 0), image)
    name = data["windows_path"] + 'icon/' + i["name"] + '.png'
    background.save(name, 'png', optmize=False)
    end_log(i)

# Make sure iOS icons filled.
fill_color = data["fill_color"]
background = Image.new(src.mode[:-1], src.size, fill_color)
background.paste(src, src.split()[-1])
src = background

for i in data["ios"]["icon"]:
    start_log(i)
    image = src.resize((i["width"], i["height"]), Image.ANTIALIAS)
    name = data["ios_path"] + 'icon/' + i["name"] + '.png'
    image.save(name, 'png', optmize=False)
    end_log(i)

# Generate splashes
src = Image.open('splash.png')
for i in data["ios"]["splash"]:
    start_log(i)
    image = crop(src, i["width"], i["height"])
    image.save(data["ios_path"] + 'splash/' + i["name"] + '.png',  'png')
    end_log(i)

for i in data["android"]["splash"]:
    start_log(i)
    image = crop(src, i["width"], i["height"])
    image.save(data["android_path"] + 'splash/' + i["name"] + '.png',  'png')
    end_log(i)

for i in data["windows"]["splash"]:
    start_log(i)
    image = crop(src, i["width"], i["height"])
    # https://github.com/python-pillow/Pillow/issues/2609
    # Windows splash must be jpeg
    fill_color = data["fill_color"]
    if image.mode in ('RGBA', 'LA'):
        background = Image.new(image.mode[:-1], image.size, fill_color)
        background.paste(image, image.split()[-1])
        image = background
    image.save(data["windows_path"] + 'splash/' + i["name"] + '.jpg',  'jpeg')
    end_log(i)

print colored('Finished', 'green')
print colored('Generated Android files are in "' + str(data["android_path"]) + '" directory.', 'green')
print colored('Generated iOS files are in "' + str(data["ios_path"]) + '" directory.', 'green')
print colored('Generated Windows files are in "' + str(data["windows_path"]) + '" directory.', 'green')