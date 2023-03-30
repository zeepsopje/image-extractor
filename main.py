import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

import cv2
import extcolors

from colormap import rgb2hex

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_jpgs(file):
    if file.endswith('jpg'):
        return True
    else:
        return False

def extract(image):
    return extcolors.extract_from_path(image, tolerance = 12, limit = 12)

def color_to_df(input):
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]

    #convert RGB to HEX code
    df_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                     int(i.split(", ")[1]),
                     int(i.split(", ")[2].replace(")",""))) for i in df_rgb]

    df = pd.DataFrame(zip(df_up, df_percent), columns = ['c_code','occurence'])
    return df

if __name__ == "__main__":
    images = list(filter(get_jpgs, os.listdir(".")))

    if len(images) == 0:
        print("No images in this directory.")
        sys.exit(0)

    output = {}

    for x, image in enumerate(images):
        colors = extract(image)[0]
        output[image] = []
        for y, color in enumerate(colors):
            hex = rgb_to_hex(color[0][0], color[0][1], color[0][2])
            occ = color[1]
            output[image].append((hex, occ))

    f = open("dump.json", "w")
    f.write(json.dumps(output))
