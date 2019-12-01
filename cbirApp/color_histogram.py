import cv2


class HSVColorHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1, 2], None, self.bins, [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist)
        return hist.flatten()
