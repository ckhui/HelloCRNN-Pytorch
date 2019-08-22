# CRNN in Python3 and Pytorch1.2
Continue from [crnn.pytorch by meijieru](https://github.com/meijieru/crnn.pytorch) (python2, pytorch0.x) 

#### Demo
1. download weights ([Dropbox](https://www.dropbox.com/s/dboqjk20qjkpta3/crnn.pth?dl=0)) into `./data/`.
```
python3 demo.py
```

#### Train 
1. Create Dataset follow [origin guide](https://github.com/bgshih/crnn#train-a-new-model).
    - 
```
python train.py --adadelta --trainRoot {train_path} --valRoot {val_path} --cuda
```