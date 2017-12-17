from skimage import io
import numpy as np


def extract_images(fpath):
    coll = io.ImageCollection(fpath)

    img = np.array(())
    img_new = coll[0]
    img_new = img_new.reshape(-1, 65536)

    for i in range(1, len(coll)):
        img = coll[i]
        # 扁平化像素矩阵
        img = img.reshape(-1, 65536)
        # 组合图像特征数据形成训练集
        img_new = np.r_[img_new, img]
    return img_new


i = 1
i = str(i)

path = 'F:/PYthon_codes/my_program/data_new/*.jpg'

train_images = extract_images(path)
print(train_images.shape)
train_labels = np.ones(100)
for i in range(80, 100):
    train_labels[i] = 0
print(train_labels.shape)
