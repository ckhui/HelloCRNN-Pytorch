from tool.origin_createDataset import createDataset

def generateDateset(imgList):
    """
        imgList: a txt file that contain ImagesFullPath and Label
    """
    with open(imgList, 'r') as f:
        lines = f.readlines()
    images = lines
    labels = [line.split("_")[-1].replace(".jpg","") for line in lines]
    createDataset()