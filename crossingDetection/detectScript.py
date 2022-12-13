"""
Runs multiple img files from inputImgs and outputs them in results

Note: Input images are named as img<new number>.jpg
It wont work with any other names so make sure you rename it manually to this.

Outputs 3 types of images: Contours(finds boundaries), morphed(expands the binary image to fill gaps) and threshold(max clarity)

img 1-7 Mahima
img 8-43 Ariana
img 44-45 ImVisible
"""

import cv2
import numpy as np

# read image
# imgNumber = str(6)

lastImgNumber = 44
for i in range(1, lastImgNumber):
    imgNumber = str(i)
    img = cv2.imread('inputImgs/img'+ imgNumber + '.jpg')

    # threshold on white/gray sidewalk stripes
    lower = (100,130,130)
    upper = (180,200,200)
    thresh = cv2.inRange(img, lower, upper)


    # apply morphology close to fill interior regions in mask
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((5,5), np.uint8)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

    # get contours
    cntrs = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]

    # filter on area
    contours = img.copy()
    good_contours = []
    for c in cntrs:
        area = cv2.contourArea(c)
        if area > 200:
            cv2.drawContours(contours, [c], -1, (0,0,255), 1)
            good_contours.append(c)

    # combine good contours
    contours_combined = np.vstack(good_contours)

    # get convex hull
    result = img.copy()
    hull = cv2.convexHull(contours_combined)
    cv2.polylines(result, [hull], True, (0,0,255), 2)

    # # Crop part of image
    # x, y = [], []
    # for contour_line in good_contours:
    #     for contour in contour_line:
    #         x.append(contour[0][0])
    #         y.append(contour[0][1])

    # x1, x2, y1, y2 = min(x), max(x), min(y), max(y)

    # cropped = img[y1:y2, x1:x2]
    # cv2.imshow("croppedImg",img)
    # cv2.imwrite('test_cropped_img.jpg',img)

    # write result to disk
    cv2.imwrite("results/img"+ imgNumber + "_thresh.jpg", thresh)
    cv2.imwrite("results/img"+ imgNumber + "_morph.jpg", morph)
    cv2.imwrite("results/img"+ imgNumber + "_contours.jpg", contours)
    # cv2.imwrite("img"+ imgNumber  + "_result.jpg", result)

    # display it
    # cv2.imshow("THRESH", thresh)
    # cv2.imshow("MORPH", morph)
    # cv2.imshow("CONTOURS", contours)
    # cv2.imshow("RESULT", result)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()