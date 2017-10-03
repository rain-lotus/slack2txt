# 2017/10/01
# by rain
# argument: ' Path of directory containing json/*.* '

import glob
import json
import sys
import re

argvs = sys.argv

# フォルダの名前を持ってくる（力技）
title = argvs[1].split('/')[len(argvs[1].split('/'))-2]

# フォルダ内のjsonを読み込んでtextだけ抽出してtxtに保存
files = glob.glob(argvs[1])
f2 = open('{}.txt'.format(title), 'w')

for file in files:
    f = open(file,'r')
    jsonData = json.load(f)
    f.close()
    for i in range(len(jsonData)): 
        text = jsonData[i]["text"]
        f2.write(text)
        f2.write("\n")
    f2.write("\n")
f2.close()

