import time
from shutil import copyfile

import cv2
import numpy as np

from cbir import settings
from cbirApp.color_histogram import HSVColorHistogram
from cbirApp.models import Images
from cbirApp.image_item import ImageItem
from cbirApp.feature_extraction_method import FeatureExtractionMethod
from cbirApp.texture_histogram import TextureHistogram
from dataclasses_serialization.json import JSONSerializer


def get_similar_images(dest_image, feature_extraction_method):
    start = time.time()
    print(feature_extraction_method)
    source_image = cv2.imread(cv2.os.path.join(settings.MEDIA_ROOT, str(dest_image)))
    results = []
    if isColorFeature(feature_extraction_method):
        hsv_histogram = HSVColorHistogram([8, 8, 8])
        source_color_features = hsv_histogram.describe(source_image)
    if isTextureFeature(feature_extraction_method):
        texture_histogram = TextureHistogram(radius=3)
        source_texture_features = texture_histogram.describe(source_image)

    db_images = Images.objects.all().filter(status='1')
    for temp_image in db_images:
        score_color = 0
        if isColorFeature(feature_extraction_method):
            db_color_features = get_histogram_from_string(temp_image.color_histogram, 512)
            source_color_features = np.around(np.array(source_color_features, dtype=np.float32), decimals=8)
            db_color_features = np.around(np.array(db_color_features, dtype=np.float32), decimals=8)
            score_color = cv2.compareHist(source_color_features,
                                          db_color_features,
                                          cv2.HISTCMP_BHATTACHARYYA)

        score_texture = 0
        if isTextureFeature(feature_extraction_method):
            db_texture_features = get_histogram_from_string(temp_image.texture_histogram, 26)
            source_texture_features = np.around(source_texture_features, decimals=8)
            score_texture = cv2.compareHist(np.array(source_texture_features, dtype=np.float32),
                                            np.array(db_texture_features, dtype=np.float32),
                                            cv2.HISTCMP_BHATTACHARYYA)
        image_item = ImageItem(temp_image.name,
                               "http://localhost:8000/media/" + temp_image.name,
                               score_color + score_texture,
                               temp_image.width,
                               temp_image.height)
        results.append(image_item)

    results = sorted(results, key=lambda temp: temp.score)[:10]
    print(results)
    for result in results:
        copyfile('/home/gorkem/Desktop/flickr-test-data/' + result.name,
                 cv2.os.path.join(settings.MEDIA_ROOT, result.name))
    end = time.time()
    print("asdsadsadsa")
    print(end - start)
    return list(map((lambda x: JSONSerializer.serialize(x)), results))



def get_histogram_from_string(histogram, size):
    db_image1_text = histogram.translate(str.maketrans(dict.fromkeys('[]')))
    data = db_image1_text.split()
    result = np.zeros(size)
    index = 0
    for i in range(size):
        result[i] = data[index]
        index += 1
    return result


def isColorFeature(feature_extraction_method):
    return (feature_extraction_method == FeatureExtractionMethod.COLOR_TEXTURE.value or
            feature_extraction_method == FeatureExtractionMethod.COLOR.value)


def isTextureFeature(feature_extraction_method):
    return (feature_extraction_method == FeatureExtractionMethod.COLOR_TEXTURE.value or
            feature_extraction_method == FeatureExtractionMethod.TEXTURE.value)
