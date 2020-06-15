from os import listdir
from os.path import isfile, join

def retrieve_files():
    path = "TrainingSet/label0"
    filename_labelZero = [f for f in listdir(path) if isfile(join(path, f))]
    path = "TrainingSet/label1"
    filename_labelOne = [f for f in listdir(path) if isfile(join(path, f))]
    path = "TrainingSet/label2"
    filename_labelTwo = [f for f in listdir(path) if isfile(join(path, f))]
    
    pass
    
if __name__ == "__main__":
    retrieve_files()
    pass