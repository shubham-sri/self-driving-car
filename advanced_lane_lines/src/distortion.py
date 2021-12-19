import numpy as np
import matplotlib.image as mpeg
from cv2 import \
    findChessboardCorners, \
    cvtColor, \
    COLOR_BGR2GRAY, \
    calibrateCamera, \
    undistort


class Distortion:
    """Compute distortion and undistorted image
    ...
    Attributes
    ----------
    nx : int
        the number of interior corners in the x direction
    ny : int
        the number of interior corners in the y direction
    """

    def __init__(self, nx=8, ny=6) -> None:
        """Initialize a `Distortion` object
        Attributes
        ----------
        nx : int
            the number of interior corners in the x direction
        ny : int
            the number of interior corners in the y direction
        """
        self.nx = nx
        self.ny = ny
        self.obj_points = []
        self.img_points = []

    def calculate(self, images: [str]) -> None:
        """Get the camera calibration parameters
        Parameters
        ----------
        images : list
            a list of images OR image file paths
        """
        self.obj_points = []
        self.img_points = []

        objpt = np.zeros((self.nx * self.ny, 3), np.float32)
        objpt[:, :2] = np.mgrid[0:self.nx, 0:self.ny].T.reshape(-1, 2)

        for image in images:
            img = mpeg.imread(image)
            gray = cvtColor(img, COLOR_BGR2GRAY)
            ret, corners = findChessboardCorners(gray, (self.nx, self.ny))
            if ret:
                self.img_points.append(corners)
                self.obj_points.append(objpt)

    def fix(self, image) -> []:
        gray = cvtColor(image, COLOR_BGR2GRAY)
        ret, mtx, dist, rvecs, tvecs = calibrateCamera(
            self.obj_points,
            self.img_points,
            gray.shape[::-1],
            None,
            None
        )
        return undistort(image, mtx, dist, None, mtx)
