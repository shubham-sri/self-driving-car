import numpy as np
import cv2


class Thresholding:
    def __init__(self, image: np.ndarray) -> None:
        self.image = image
        self.input = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.hls_input = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    def sobel_xy(self, orient='x', thresh=(20, 255), kernel_size=3):
        thresh_min, thresh_max = thresh
        x, y = (1, 0) if orient == 'x' else (1, 0)
        R = self.image[:, :, 0]
        sobel = cv2.Sobel(R, cv2.CV_64F, x, y, ksize=kernel_size)
        abs_sobel = np.absolute(sobel)
        scaled_sobel = np.uint8(255 * abs_sobel / np.max(abs_sobel))
        grad_binary = np.zeros_like(scaled_sobel)
        grad_binary[((scaled_sobel >= thresh_min) & (scaled_sobel < thresh_max))] = 1
        return grad_binary

    def mag_thresh(self, thresh=(0, 255), sobel_kernel=3):
        thresh_min, thresh_max = thresh
        R = self.image[:, :, 0]
        sobelx = cv2.Sobel(R, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
        sobely = cv2.Sobel(R, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
        abs_sobel = np.sqrt(sobelx ** 2 + sobely ** 2)
        scaled_sobel = np.uint8(255 * abs_sobel / np.max(abs_sobel))
        mag_binary = np.zeros_like(scaled_sobel)
        mag_binary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1
        return mag_binary

    def dir_thresh(self, thresh=(0, np.pi / 2), sobel_kernel=3):
        thresh_min, thresh_max = thresh
        R = self.image[:, :, 0]
        sobelx = cv2.Sobel(R, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
        sobely = cv2.Sobel(R, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
        abs_sobelx = np.absolute(sobelx)
        abs_sobely = np.absolute(sobely)
        gradient = np.arctan2(abs_sobely, abs_sobelx)
        dir_binary = np.zeros_like(gradient)
        dir_binary[(gradient >= thresh_min) & (gradient <= thresh_max)] = 1
        return dir_binary

    def gradient_thresh(self, thresh_x, thresh_y, thresh_mag, thresh_dir):
        sobelx = self.sobel_xy(orient='x', thresh=thresh_x)
        sobely = self.sobel_xy(orient='y', thresh=thresh_y)
        mag_img = self.mag_thresh(thresh=thresh_mag)
        dir_img = self.dir_thresh(sobel_kernel=11, thresh=thresh_dir)
        gradient_binary = np.zeros_like(dir_img).astype(np.uint8)
        gradient_binary[((sobelx == 1) & (sobely == 1)) | ((mag_img == 1) & (dir_img == 1))] = 1
        return gradient_binary

    def channel_thresh(self, channel, thresh=(80, 255)) -> np.ndarray:
        binary = np.zeros_like(channel)
        binary[(channel > thresh[0]) & (channel <= thresh[1])] = 1
        return binary

    def color_thresh(self, thresh_s):
        S = self.hls_input[:, :, 2]
        s_binary = self.channel_thresh(S, thresh_s)

        return s_binary

    def result(self, grad, hls):
        result = np.zeros_like(hls).astype(np.uint8)
        result[(hls == 1) | (grad == 1)] = 1
        return result
