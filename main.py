from os import listdir
from os.path import isfile, join
# Imports PIL module  
from PIL import Image 


def retrieve_files():
	trainingPathLabel0 = "./Dataset/Training Set/label0/"
	trainingPathLabel1 = "./Dataset/Training Set/label1/"
	trainingPathLabel2 = "./Dataset/Training Set/label2/"
	# files = [f for f in listdir(trainingPath) if isfile(join(trainingPath, f))]
	# print(files)

	entries = listdir(trainingPathLabel0)
	print(entries)

	for file in entries:
		print(file)
		# open method used to open different extension image file 
		im = Image.open(trainingPathLabel0 + file)
		print(im)
		print(list(im.getdata()))
		exit(3)

	# This method will show image in any image viewer  

if __name__ == "__main__":
    retrieve_files()
    pass