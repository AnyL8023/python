# -*- coding: utf8 -*-

import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# originFileListPath = "C:\Users\Administrator\Desktop\searchCar"
originFileListPath = raw_input("imput json files path : ")
saveFilePath =originFileListPath+"\\result.json"#保存文件


allFileNum = 0
allFileList = []

def getPath(level, path):
    global allFileNum
    global allFileList
    '''''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
            # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print 'read : '+path+'\\' * (int(dirList[0]))+dl
            # 打印目录下的所有文件夹和文件，目录级别+1
            getPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print 'read : '+path+'\\' * (int(dirList[0]))+fl
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1
        allFileList.append(path+'\\' * (int(dirList[0]))+fl)


def readFile(filePath):
    f = open(filePath)  # 读取文件
    lines = f.readlines()
    print "read : ",filePath," , content : ",lines
    f.close()
    return  lines

def writeFile(filePath,lines):
    f = file(filePath, "a+")
    # f.writelines(lines)
    for line in lines:
        f.write(formatJson(line))
    print "save : ", filePath, " , content : ", lines
    f.write("\r")
    f.close()

def formatJson(line):
    return  json.dumps(json.loads(line,strict=False),indent=4, sort_keys=False, ensure_ascii=False)


getPath(1, originFileListPath)
for filePath in allFileList:
    lines = readFile(filePath)
    writeFile(saveFilePath,lines)

print "********************file count = ",allFileNum,"***************************"
