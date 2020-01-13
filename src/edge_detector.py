import cv2
import numpy as np
import argparse, os


def noise_filter(image, mode=None, kernel=None):
    """ noise removal
        image     a image stored in ndarray
        mode      the different choice of the filter('Averaging', 'Gaussian', 'Median' and 'Bilateral')
        kernel    self-defined kernel
    """
    if mode.lower() == 'averaging':
        blur = cv2.blur(image, (5, 5))
    elif mode.lower() == 'gaussian':
        blur = cv2.GaussianBlur(image, (5, 5), 0)
    elif mode.lower() == 'median':
        blur = cv2.medianBlur(image, 5)
    elif mode.lower() == 'bilateral':
        blur = cv2.bilateralFilter(image, 5, 75, 75)
    # self-defined filter
    elif mode is None and kernel is not None:
        blur = cv2.filter2D(image, -1, kernel)
    # if no mode and no kernel, print error
    else:
        print('the mode or the kernel is not provided')
    return blur


def edge_detector(image, method='canny'):
    if method.lower() == 'laplacian' or 'laplace':
        lap = cv2.Laplacian(image, cv2.CV_64F)
        lap = np.uint8(np.absolute(lap))
        return lap
    elif method.lower() == 'sobel':
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
        sobelx = np.uint8(np.absolute(sobelx))
        sobely = np.uint8(np.absolute(sobely))
        sobelcombined = cv2.bitwise_or(sobelx, sobely)
        return sobelcombined
    elif method.lower() == 'canny':
        edges = cv2.Canny(image, 100, 200)
        return edges


if __name__ == '__main__':
    # input image as the argument
    argp = argparse.ArgumentParser()
    argp.add_argument('image')
    args = argp.parse_args()

    # load the image
    filename = args.image
    img_original = cv2.imread(args.image)

    # convert the image into gray scale
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    # noise reduction
    filtered_image = noise_filter(img_gray, mode='bilateral')
    filtered_image = noise_filter(filtered_image, mode='bilateral')

    # use thresshold to convert image into black and white
    _, th = cv2.threshold(filtered_image, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('th', th)

    # edge detection
    edges = edge_detector(th, 'canny')
    cv2.imshow('e',edges)

    # draw edges
    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i][j] >= 127:
                img_original[i][j][0] = 0
                img_original[i][j][1] = 255
                img_original[i][j][2] = 0

    filename = filename[8:]
    new_filename = '../output/' + filename[:filename.index('.')]
    file_type = filename[filename.index('.'):]
    whole_filename = new_filename + '_edges' + file_type

    cv2.imwrite(whole_filename, img_original)
    #cv2.imshow('result', img_original)

    cv2.waitKey(0)
    #cv2.destroyAllWindows()
