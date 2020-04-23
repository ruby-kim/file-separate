# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


if __name__ == "__main__":
    path = os.getcwd()
    print("\n* Check your path:", path, "\n")

    folderList = os.listdir(path)
    print("* Folder list:", folderList, "\n")

    excludeList = [
        ".idea",
        "main.py",
        "한국어-영어 번역 말뭉치",
        "기계독해"
        # Input what you want
    ]
    print("* Except list:", excludeList, "\n")

    for folder in folderList:
        if folder in excludeList:
            continue
        else:
            currentPath = path+"/"+folder
            fileList = os.listdir(currentPath)
            print("     Current path:", currentPath)
            print("     Organize files...")
            for file in fileList:
                print(file)
                target = file[4:8]
                targetPath = currentPath+"/"+target
                if not os.path.isdir(targetPath):
                    os.mkdir(targetPath)
                shutil.move(currentPath + "/" + file, targetPath + "/" + file)
            print("     Finish! Check", folder, "folder\n")
