from tool.origin_createDataset import createDataset

def getImageListAndLabelList(txt):
    """
        txt: a txt file that contain ImagesFullPath and Label
    """
    with open(txt, 'r') as f:
        lines = f.readlines()
    images = [line.rstrip() for line in lines]
    labels = [line.split("_")[-1].replace(".jpg","") for line in lines]
    return images, labels


if __name__ == "__main__":
    txt = "/home/rnd/Documents/CRNN Training/train.txt"
    outputPath = "./data/dataset/"

    imageList, labelList =  getImageListAndLabelList(txt)
    createDataset(outputPath, imageList, labelList, checkValid=True)
    pass