import cv2 as cv
im = cv.imread('img/sample.png')
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
print('retval: {}'.format(retval))
