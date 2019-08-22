# CRNN in Python3 and Pytorch1.2
Continue from [crnn.pytorch by meijieru](https://github.com/meijieru/crnn.pytorch) (python2, pytorch0.x) 

### Demo
1. download weights ([Dropbox](https://www.dropbox.com/s/dboqjk20qjkpta3/crnn.pth?dl=0)) into `./data/`.
```
python3 demo.py
```

### Train 
#### Dataset
1. Create Dataset follow [origin guide](https://github.com/bgshih/crnn#train-a-new-model).
    - copy the file to `tool/origin_createDataset.py`
    - create a helper `createDataset.py`
    - migrate to python3
2. Implement the method to read imagelist and labellist in `createDataset.py`
```
python3 createDataset.py
```