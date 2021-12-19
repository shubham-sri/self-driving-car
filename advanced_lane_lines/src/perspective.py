import cv2
import numpy as np


class Perspective:
    def __init__(self, src=None, dst=None):
        self.src = np.float32([[200, 720], [1100, 720], [595, 450], [685, 450]]) if src is None else src
        self.dst = np.float32([[300, 720], [980, 720], [300, 0], [980, 0]]) if dst is None else dst
        self.m = cv2.getPerspectiveTransform(self.src, self.dst)
        self.m_inv = cv2.getPerspectiveTransform(self.dst, self.src)

    def transform(self, image):
        (y, x) = image.shape[:2]
        return cv2.warpPerspective(image, self.m, (x, y), flags=cv2.INTER_LINEAR)

    def inverse_transform(self, image):
        (y, x) = image.shape[:2]
        return cv2.warpPerspective(image, self.m_inv, (x, y), flags=cv2.INTER_LINEAR)
