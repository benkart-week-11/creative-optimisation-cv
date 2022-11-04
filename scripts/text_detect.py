# path
import os.path
from os import path
import glob
#colors
import extcolors
import pandas as pd
from colormap import rgb2hex
from matplotlib import pyplot as plt
from PIL import Image
# text extraction lib
import pytesseract
import cv2
import numpy as np
from typing import List, Tuple


class Text_Extraction:
    def __init__(self) -> None:
        pass
    def identify_color_composition(self, image,
                               tolerance: int = 12,
                               limit: int = 1,
                                visualize: bool = False) -> None:
        """Function that identifies the color composition of a
        given image path."""

        extracted_colors = extcolors.extract_from_path(
            image, tolerance=tolerance, limit=limit)

        identified_colors = color_to_df(extracted_colors)

        return identified_colors

    def color_to_df(self, extracted_colors: tuple):
        """Converts RGB Color values from extcolors output to HEX Values."""

        colors_pre_list = str(extracted_colors).replace(
            '([(', '').replace(')],', '), (').split(', (')[0:-1]
        df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
        df_percent = [i.split('), ')[1].replace(')', '')
                    for i in colors_pre_list]

        # convert RGB to HEX code
        df_rgb_values = [(int(i.split(", ")[0].replace("(", "")),
                        int(i.split(", ")[1]),
                        int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]

        df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                            int(i.split(", ")[1]),
                            int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]

        colors_df = pd.DataFrame(zip(df_color_up, df_rgb_values, df_percent),
                                columns=['c_code', 'rgb', 'occurrence'])

        return colors_df
    def convert_hex_to_rgb(self, hex_color: str, normalize: bool = True) -> List[str]:
        """Converts a HEX color to a RGB color

        Args:
            hex_color (str): HEX color code to convert
            normalize (bool, optional): Choice to normalize calculated rgb values . Defaults to True.

        Returns:
            List[str]: List of RGB values in order, normalized or not.
        """
        colors = hex_color[1:]

        # Convert HEX color values to RGB Values
        colors = [int(colors[0:2], base=16),  # RED
                int(colors[2:4], base=16),  # GREEN
                int(colors[4:6], base=16)]  # BLUE

        # Normalize RGB values
        if normalize:
            colors = [color / 255 for color in colors]

        return colors
    #get luminance
    def get_luminance(self, hex_color: str) -> float:
        """Calculates the luminance of a given HEX color

        Args:
            hex_color (str): HEX color code to calculate luminance for

        Returns:
            float: luminance value of color
        """
        colors = convert_hex_to_rgb(hex_color)

        luminance = colors[0] * 0.2126 + colors[1] * 0.7152 + colors[2] * 0.0722

        return luminance
    # fix background
    def fix_image_background(self, image_path: str):
        identified_colors = identify_color_composition(image_path)
        text_color = identified_colors['c_code'].to_list()[0]
        text_color_rgb = identified_colors['rgb'].to_list()[0]
        luminance = get_luminance(hex_color=text_color)

        if luminance < 140:
            background_color = (255, 255, 255)
        else:
            background_color = (0, 0, 0)

        # Load image
        image = cv2.imread(image_path)

        # Make all perfectly green pixels white
        image[np.all(image != text_color_rgb, axis=-1)] = background_color

        return image
    def extract_text(self, image_path, tesseract_cmd: str, fix_background: bool = False):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        extracted_texts =[]
        try:
            if fix_background:
                text = pytesseract.image_to_string(fix_image_background(image_path))

            else:
                text = pytesseract.image_to_string(image_path)
            return text
        except pytesseract.TesseractNotFoundError:
            raise Exception(
                f'Failure: Tesseract is not installed or not available in the defined path {tesseract_cmd}')
        #print(text_df)
        #return text_df

#text extraction
list_assets = glob.glob('../Challenge_Data/Assets/*')
# initialize the class
extract =Text_Extraction()
lists_text =[]

for ls in list_assets:
    #print(ls)
    if path.exists(ls+'/cta.png'):
        lists_text.append(extract.extract_text(ls+'/cta.png', r'/usr/bin/tesseract'))
text_df = pd.DataFrame(zip(lists_text), columns=['Text'])
print(text_df)
