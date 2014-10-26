import cv2

def cropImage(imgfilename,xs,ys):
	img = cv2.imread(imgfilename)
	crop_img = img[xs[0]:xs[1],ys[0]:ys[1]] 
	return crop_img
	
if __name__ = "__main__":
	from os import listdir
	from os.path import isfile,join
	readpath = "./read"
	files = [f for f in listdir(readpath) if isfile(join(readpath,f))]
	returned = cropImage(files[2],[100,900],[100,900])
	cv2.imshow("cropped",returned)
	cv2.waitkey(0)
	return
	
	writepath = "./write"
	for file in files:
		croped = cropImage(files[2],[100,900],[100,900])
		cv2.imwrite(join(writepath,file)
	