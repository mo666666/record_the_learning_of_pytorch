# -*- coding: utf-8 -*-
"""
# @file name  : 1_split_dataset.py
# @author     : tingsongyu
# @date       : 2019-09-07 10:08:00
# @brief      : 将数据集划分为训练集，验证集，测试集
"""

import os
import random
import shutil


def makedir(new_dir):
    if not os.path.exists(new_dir):  # 看文件夹存不存在，如果存在，则循环创建文件夹
        os.makedirs(new_dir)


if __name__ == '__main__':

    random.seed(1)

    dataset_dir = os.path.join("..", "..", "data", "RMB_data")
    split_dir = os.path.join("..", "..", "data", "rmb_split")
    train_dir = os.path.join(split_dir, "train")
    valid_dir = os.path.join(split_dir, "valid")
    test_dir = os.path.join(split_dir, "test")
    # print(os.path.abspath(split_dir))

    train_pct = 0.8
    valid_pct = 0.1
    test_pct = 0.1

    for root, dirs, files in os.walk(dataset_dir):  # root 代表URL，dirs代表root下的文件夹名组成的列表，files代表该目录下不能打开的文件夹
        # print(root, dirs, files)
        for sub_dir in dirs:  # 洗数据集下所有的图片
            imgs = os.listdir(os.path.join(root, sub_dir))  # 返回路径下的所有文件（以列表的形式返回）
            imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
            # print(imgs)
            random.shuffle(imgs)  # 将列表中所有文件都重新排列一次
            img_count = len(imgs)
            train_point = int(img_count * train_pct)
            valid_point = int(img_count * (train_pct + valid_pct))
            for i in range(img_count):
                if i < train_point:
                    out_dir = os.path.join(train_dir, sub_dir)
                elif i < valid_point:
                    out_dir = os.path.join(valid_dir, sub_dir)
                else:
                    out_dir = os.path.join(test_dir, sub_dir)
                makedir(out_dir)

                target_path = os.path.join(out_dir, imgs[i])
                src_path = os.path.join(dataset_dir, sub_dir, imgs[i])

                shutil.copy(src_path, target_path)

            print('Class:{}, train:{}, valid:{}, test:{}'.format(sub_dir, train_point, valid_point - train_point,
                                                                 img_count - valid_point))
