#!/usr/bin/python
# -*- coding: utf8 -*-
import xlrd
from xlutils.copy import copy
import re

class TrainingData():

    #训练集合文件
    read_cfg = 'read.cfg'
    #训练集合分隔符
    read_split = " "
    #训练集合列表
    training_list = []
    #训练数据
    training_data = {}

    # 测试集合文件
    test_cfg = 'test.cfg'
    # 测试集合分隔符
    test_split = " "
    # 测试集合列表
    test_list = []

    #excel表格
    training_bk = None
    #sheet表
    training_sheet = None
    #行数
    training_nrows = None

    def __init__(self):
        f = open(self.read_cfg)#读取即将进行训练的配置文件
        lines = f.readlines()
        for line in lines:
            datas = line.split(self.read_split)
            self.training_list.append(datas)
        f = open(self.test_cfg)  # 读取即将进行测试的配置文件
        lines = f.readlines()
        for line in lines:
            datas = line.split(self.test_split)
            self.test_list.append(datas)

    def trainingData(self,file_name,sheet_name,column_car_type_index,column_car_brand_index,start_row=1):
        file_name = unicode(file_name,"utf-8")
        sheet_name = unicode(sheet_name,"utf-8")
        column_car_type_index = int(column_car_type_index)
        column_car_brand_index = int(column_car_brand_index)
        start_row = int(start_row)

        print "read file: %s"%(file_name)
        self.training_bk = xlrd.open_workbook(file_name)
        try:
            self.training_sheet = self.training_bk.sheet_by_name(sheet_name)
        except:
            print "no sheet in %s named Sheet1" % sheet_name

        self.training_nrows = self.training_sheet.nrows
        print "training datas nrows %d" % (self.training_nrows)

        for i in range(start_row, self.training_nrows):
            row_data = self.training_sheet.row_values(i)
            car_type = row_data[column_car_type_index].split(" ")[0]
            car_brand = row_data[column_car_brand_index]
            # print "get file: %s , sheet: %s , row: %d , car_type: %s , tcar_brand: %s" % (file_name,sheet_name,i,car_type, car_brand)
            if car_brand!=u"":
                self.training_data[car_type] = car_brand
                origin_car_type = car_type
                car_type = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\-]", "", car_type)
                if car_type!=u"" and car_type!=origin_car_type:
                    print "get file: %s , sheet: %s , row: %d , car_type: %s , tcar_brand: %s" % (file_name, sheet_name, i, car_type, car_brand)
                    self.training_data[car_type] = car_brand

    def training(self):
        for data in self.training_list:
            file_name = data[0]
            sheet_name = data[1]
            column_car_type_index = data[2]
            column_car_brand_index = data[3]
            start_row = data[4]
            self.trainingData(file_name,sheet_name,column_car_type_index,column_car_brand_index,start_row)

    def getTrainingDataSet(self):
        return self.training_data

    def testTrainingData(self,file_name,sheet_name,sheet_index,column_car_type_index,column_car_brand_index,start_row=1):
        file_name = unicode(file_name, "utf-8")
        sheet_name = unicode(sheet_name, "utf-8")
        sheet_index = int(sheet_index)
        column_car_type_index = int(column_car_type_index)
        column_car_brand_index = int(column_car_brand_index)
        start_row = int(start_row)

        test_bk_r = xlrd.open_workbook(file_name)
        test_bk_w = copy(test_bk_r)
        try:
            test_sheet_r = test_bk_r.sheet_by_name(sheet_name)
            test_sheet_w = test_bk_w.get_sheet(sheet_index)
        except:
            print "no sheet in %s named Sheet1" % sheet_name

        # 获取行数
        test_nrows = test_sheet_r.nrows
        print "testing data nrows %d" % (test_nrows)

        file_name = file_name.replace(".xlsx", "")
        file_name = file_name + "-" + sheet_name + ".xls"
        test_training_data = []
        for i in range(start_row, test_nrows):
            row_data = test_sheet_r.row_values(i)
            car_type = row_data[column_car_type_index].split(" ")[0]
            car_brand = None
            try:
                car_brand = self.training_data[car_type]
            except:
                try:
                    car_type = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\-]", "",car_type)
                    car_brand = self.training_data[car_type]
                except:
                    pass
            test_sheet_w.write(i, column_car_brand_index, car_brand)
            print "save file: %s , sheet: %s , row: %d , car_type: %s , car_brand: %s" % (file_name,sheet_name,i,car_type,car_brand)

        test_bk_w.save(file_name)

    def run(self):
        for data in self.test_list:
            file_name = data[0]
            sheet_name = data[1]
            sheet_index = data[2]
            column_car_type_index = data[3]
            column_car_brand_index = data[4]
            start_row = data[5]
            self.testTrainingData(file_name,sheet_name,sheet_index,column_car_type_index,column_car_brand_index,start_row)

trainingData = TrainingData()
trainingData.training()
trainingData.run()
