# -*- coding: utf8 -*-

import glob
import os
import shutil
import utility

def convert(in_dir, out_dir, title):
    index = 0
    new_dir_path_recursive = 'Resources\\' + title + '\\' + title + 'SlideTexture'
    in_dir += '\\'
    out_dir = out_dir + '\\' + new_dir_path_recursive + '\\'

    list = glob.glob(in_dir + '*.png')
    print('before')
    print(list)

    # ファイルを複製
    for file in list:
        name, extension = file.split('.')
        copyed_file_path = name + '-copy.' + extension
        shutil.copy2(file, copyed_file_path)

    list = glob.glob(in_dir + '*.png')

    # 出力先ディレクトリを作成
    os.makedirs(out_dir)

    # ファイル名一括置換
    for file in list:
        if index < 10:
            os.rename(file, out_dir + title + '-00' + str(index) + '.png')
        elif index < 100:
            os.rename(file, out_dir + title + '-0' + str(index) + '.png')
        else:
            os.rename(file, out_dir + title + '-' + str(index) + '.png')
        index += 1

    list = glob.glob(out_dir + '*')
    print('after')
    print(list)


if __name__ == "__main__":
    in_dir = utility.get_current_path() + '\\VRCLTSlidePic'
    out_dir = utility.get_current_path() + '\\VRCLTSlidePic'
    convert(in_dir, out_dir, 'Test')