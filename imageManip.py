import numpy as np
import cv2

#blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
#im = cv2.selectROI(edges)

def findLeftOuterBorder(img, start=0):
	for j in range(0,len(img[0])):
		for i in range(0,len(img)):
			if img[i][j] != 0:
				return j

def findRightOuterBorder(img, end=0):
	for j in range(len(img[0])-1,-1,-1):
		for i in range(len(img)-1,-1,-1):
			if img[i][j] != 0:
				return j+1

def findTopOuterBorder(img, start=0):
	for i in range(0,len(img)):
		for j in range(0,len(img[0])):
			if img[i][j] != 0:
				return i

def findBottomOuterBorder(img, end=0):
	for i in range(len(img)-1,-1,-1):
		for j in range(len(img[0])-1,-1,-1):
			if img[i][j] != 0:
				return i+1

def findLeftInnerBorder(img, start=0):
	for j in range(0,len(img[0])):
		foundEdge = False
		for i in range(0,len(img)):
			if img[i][j] != 0:
				foundEdge = True
				break
		if not foundEdge:
			return j

def findRightInnerBorder(img, end=0):
	for j in range(len(img[0])-1,-1,-1):
		foundEdge = False
		for i in range(len(img)-1,-1,-1):
			if img[i][j] != 0:
				foundEdge = True
				break
		if not foundEdge:
			return j

def findTopInnerBorder(img, start=0):
	for i in range(0,len(img)):
		foundEdge = False
		for j in range(0,len(img[0])):
			if img[i][j] != 0:
				foundEdge = True
				break
		if not foundEdge:
			return i

def findBottomInnerBorder(img, end=0):
	for i in range(len(img)-1,-1,-1):
		foundEdge = False
		for j in range(len(img[0])-1,-1,-1):
			if img[i][j] != 0:
				foundEdge = True
				break
		if not foundEdge:
			return i

def crop_leftRight(img):
	left = findLeftOuterBorder(img)
	right = findRightOuterBorder(img)
	return img[:,left:right]

def crop_topBottom(img):
	top = findTopOuterBorder(img)
	bottom = findBottomOuterBorder(img)
	return img[top:bottom]

def crop_shape(img):
	#img = crop_topBottom(img)
	#if len(img) > 0:
	#	return crop_topBottom(img)
	#return img[0:1,0:1]
	return crop_leftRight(crop_topBottom(img))

def thicken(img):
	blur = cv2.GaussianBlur(img,(3,3),0)
	val, img = cv2.threshold(blur, 1, 255, cv2.THRESH_BINARY)
	return img

def print_info(img, text=""):
	x, y = img.shape
	if text != "":
		print(text)
	print("x:",x)
	print("y:",y)

def list_to_files(images, name="result"):
	for i in range(len(images)):
		cv2.imwrite(name+str(i)+".jpg",images[i])

img = cv2.imread("image.jpg", 0)
blurred = cv2.GaussianBlur(img,(7,7),0)
edges = cv2.Canny(blurred,100,200) # fiddle with this to improve results
img = thicken(np.array(edges))
img = crop_shape(img)


cv2.imwrite("test.jpg",np.invert(img))


horizontalImages = []
tempshape = (0,0)
while True:
	topInner = findTopInnerBorder(img)
	tempImg = crop_shape(img[:topInner,:])
	img = crop_shape(img[topInner:,:])
	tempx, tempy = tempImg.shape
	if tempx > 10 and tempy > 10:
		horizontalImages.append(tempImg)
	if img.shape[0] <= 10 or tempshape == img.shape:
		break
	tempshape = img.shape

list_to_files(horizontalImages, "horizontalImage")

images = []
tempshape = (0,0)
for image in horizontalImages:
	tempx, tempy = tempImg.shape
	while tempx > 10 and tempy > 10:
		leftInner = findLeftInnerBorder(image)
		image = crop_shape(image[:,leftInner:])
		tempImg = crop_shape(image[:,:leftInner])
		tempx, tempy = tempImg.shape
		if tempx > 10 and tempy > 10:
			images.append(tempImg)
		if image.shape[0] <= 10 or tempshape == image.shape:
			break
		tempshape = image.shape

list_to_files(images, "finalImage")

#"""