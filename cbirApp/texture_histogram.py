import cv2
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq


class TextureHistogram:
    def __init__(self, radius):
        self.radius = radius

    def describe(self, image):
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        no_points = 8 * self.radius
        lbp = local_binary_pattern(im_gray, no_points, self.radius, method='uniform')
        # Calculate the histogram
        x = itemfreq(lbp.ravel())
        # Normalize the histogram
        hist = x[:, 1] / sum(x[:, 1])
        # print(hist)
        return hist
