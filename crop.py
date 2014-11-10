import cv2

def cropImage(imgfilename,xs,ys):
	img = cv2.imread(imgfilename)
	crop_img = img[ys[0]:ys[1],xs[0]:xs[1]] 
	return crop_img
	
if __name__ == "__main__":
	from os import listdir
	from os.path import isfile,join
	readpath = "./read"
	files = [f for f in listdir(readpath) if isfile(join(readpath,f)) and (".jpg" in f)]
	print files
	#returned = cropImage(join(readpath,files[0]),[108,2250],[84,3490])
	#cv2.imshow("cropped",returned)
	#cv2.waitKey(0)
	
	
	writepath = "./write"
	for file in files:
		croped = cropImage(join(readpath,file),[108,2200],[84,3490])
		cv2.imwrite(join(writepath,file),croped)
		print file
	