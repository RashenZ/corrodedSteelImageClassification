from os import listdir
from os.path import isfile, join

def retrieve_files():
    trainingPath = "TrainingSet/"
    files = [f for f in listdir(trainingPath) if isfile(join(trainingPath, f))]
    print(files)

if __name__ == "__main__":
    retrieve_files()
    pass