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
2. Implement own method to read imagelist and labellist in `createDataset.py`
```
python3 createDataset.py
```
3. This will create `data.mdb` and `lock.mdb`

```
Errors:
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
TypeError: Won't implicitly convert Unicode to bytes; use .encode()
```
fixed by migrate to python3, with [1](https://github.com/ckhui/HelloCRNN-Pytorch/commit/35e4ce3249850c6aa5d073d379e7348a388d3180#diff-c3e48fa72f247192cd5dbd41ad6eae03), [2](https://github.com/ckhui/HelloCRNN-Pytorch/commit/3da4e5535e863ec6f4200bbdae8425969b8c4a76#diff-c3e48fa72f247192cd5dbd41ad6eae03)