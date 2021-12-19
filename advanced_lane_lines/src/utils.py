import cv2
import numpy as np


def plot_lines(image, left_fit, right_fit, m_inv, left_curve, right_curve, vehicle_offset):
    ploty = np.linspace(0, image.shape[0]-1, image.shape[0])
    left_fitx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]
    right_fitx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]

    color_warp = np.zeros((720, 1280, 3), dtype='uint8')

    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))

    cv2.fillPoly(color_warp, np.int_([pts]), (0,255, 0))

    newwarp = cv2.warpPerspective(color_warp, m_inv, (image.shape[1], image.shape[0]))
    result = cv2.addWeighted(image, 1, newwarp, 0.3, 0)

    avg_curve = (left_curve + right_curve)/2
    label_str = 'Radius of curvature: %.2f m' % avg_curve
    result = cv2.putText(result, label_str, (30, 40), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

    label_str = 'Vehicle offset(lane center): %.2f m' % vehicle_offset
    result = cv2.putText(result, label_str, (30,70), 0, 1, (0,0,0), 2, cv2.LINE_AA)

    return result