import sys
path = "D:\Python 2.7.9\libsvm-3.16\python"
sys.path.append(path)
from svmutil import *  
import Image  
   
model = [] 
MAX = 100.0 
MAXID = -1  
NUM = 30
path = "./input/37.png" 

for i in range(1, NUM):  
  model.append(svm_load_model('./datamodel/model_' + str(i)))  
 
img_org = Image.open(path)  
img = img_org.resize((36,36), Image.NEAREST)  
pixdata = img.load() 
line = "1 "  
tmpfile = open("tmpfile", "wb")  
for i in range(0, 1296):  
  line += str(i + 1)  
  if pixdata[i / 36, i % 36][0] == 255:  
    line += ":0 "  
  else:  
    line += ":1 "  
tmpfile.write(line + "\n")  
tmpfile.close()  

for i in range(1, NUM - 1):  
  test_label, test_matrix = svm_read_problem("tmpfile")  
  label, acc, val = svm_predict(test_label, test_matrix, model[i - 1])  
  print i, ":", val[0][0]
  if abs(val[0][0] - 1.0) < MAX:  
    MAX = abs(val[0][0] - 1.0)  
    MAXID = i  
  
print "probably is: ", MAXID