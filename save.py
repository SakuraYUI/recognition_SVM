# -*- coding: utf-8 -*-
import sys
path = "D:\Python 2.7.9\libsvm-3.16\python"
sys.path.append(path)
from svmutil import *  
import Image  
import random  

NUM = 30

for i in range(1, NUM):  
	train_label, train_matrix = svm_read_problem('./dataocr/ocr_' + str(i))   
  	model = svm_train(train_label, train_matrix, '-c 3 -g 0.015625')  
  	svm_save_model('./datamodel/model_' + str(i), model) 