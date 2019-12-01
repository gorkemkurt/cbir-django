import os.path

import cv2

from cbirApp.color_histogram import HSVColorHistogram
from cbirApp.models import Images
from cbirApp.texture_histogram import TextureHistogram


def create_color_histogram_database():
    path = "/home/gorkem/Desktop/flickr-test-data"
    list_of_dir = os.listdir(path)
    for file in list_of_dir:
        # image = cv2.imread('/home/gorkem/Desktop/flickr-test-data/134206.jpg')
        image = cv2.imread(path + "/" + file)
        height, width = image.shape[:2]
        extension = os.path.splitext(file)[1][1:]
        color_features_blob = create_hsv_histogram_blob(image)
        texture_features_blob = create_texture_histogram_blob(image)
        p = Images(name=file,
                   type=extension,
                   width=width,
                   height=height,
                   color_histogram=color_features_blob,
                   texture_histogram=texture_features_blob)
        p.save()


def create_hsv_histogram_blob(image):
    hsv_histogram = HSVColorHistogram([8, 8, 8])
    color_features = hsv_histogram.describe(image)
    return color_features


def create_texture_histogram_blob(image):
    texture_histogram = TextureHistogram(radius=3)
    texture_features = texture_histogram.describe(image)
    return texture_features


create_color_histogram_database()
