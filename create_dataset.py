import os
import shutil
from os.path import isfile, join
import cv2
import numpy as np


src_path = "./Fnt"
dest_path = "./number_fonts"


def copy_required_files(selected_file_names):

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    # selected_files = [25, 26, ]

    # selected_file_names = []

    # for num in selected_files:
    #     num_zeros = 5 - len(str(num))
    #     zero_str = "0"*num_zeros
    #     file_name = zero_str + str(num)
    #     selected_file_names.append(file_name)

    # create directories for numbers

    for i in range(1, 10):
        src_folder = src_path + "/Sample" + str(i)
        dest_folder = dest_path + "/number" + str(i)

        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        source_pretext = "img"
        num_zeros = 3 - len(str(i+1))
        zeros_str = "0"*num_zeros
        source_pretext += zeros_str + str(i+1)

        for selected_file in selected_file_names:
            src_file_name = source_pretext + "-" + selected_file
            dest_file_name = "img" + str(i) + "_" + selected_file
            shutil.copyfile(src_folder + "/" + src_file_name, dest_folder + "/" + dest_file_name)


def preprocess_files():

    img_size = (32, 32)

    for i in range(1, 10):

        path = dest_path + "/number" + str(i)
        file_names = [f for f in os.listdir(path) if isfile(join(path, f))]

        for file_name in file_names:

            img = cv2.imread(path + "/" + file_name, 0)
            img = cv2.bitwise_not(img)

            all_contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            all_contours = sorted(all_contours, key=cv2.contourArea, reverse=True)

            largest_contour = all_contours[0]
            x, y, w, h = cv2.boundingRect(largest_contour)
            cropped_img = img[y:y+h, x:x+w]
            h_w_ratio = h/w

            new_h = 26
            new_w = int(new_h/h_w_ratio)
            cropped_img = cv2.resize(cropped_img, (new_w, new_h))
            rem_h = img_size[1] - new_h
            rem_w = max(img_size[0] - new_w, 0)

            cropped_img = cv2.copyMakeBorder(cropped_img, rem_h//2, rem_h//2, rem_w//2, rem_w//2, cv2.BORDER_CONSTANT, 0)
            processed_img = cv2.resize(cropped_img, img_size)

            cv2.imwrite(path+"/"+file_name, processed_img)


# preproces_files()

def create_number_data():

    sample_path = dest_path + "/Selected_fonts"

    required_fonts = [f.split("-")[1] for f in os.listdir(sample_path) if isfile(join(sample_path, f))]
    # print(len(required_fonts))
    # print(required_fonts[0])

    copy_required_files(required_fonts)
    preprocess_files()


create_number_data()
