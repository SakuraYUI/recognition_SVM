import sys
path = "D:\Python 2.7.9\libsvm-3.16\python"
sys.path.append(path)
from svmutil import *  
import random  
  
def test(y, x, c, g):  
  count = len(y[0])  
  correct_rate = 0.0  
  # n-fold cross-validation  
  for i in range(0, 10):  
    marr = []  
    tarr = []  
    answers = []  
    for k in range(count*i/10, count*(i+1)*10):  
      answers.append(0)  
  
    for k in range(1, 11):  
      # training sets  
      yy = []  
      xx = []  
      for j in range(0, count*i/10):  
        yy.append(y[k - 1][j])  
        xx.append(x[k - 1][j])  
      for j in range(count*(i + 1)/10, count):  
        yy.append(y[k - 1][j])  
        xx.append(x[k - 1][j])  
      m = svm_train(yy, xx, '-c ' + str(c) + ' -g ' + str(g))  
      marr.append(m)  
      yyy = []  
      xxx = []  
      for j in range(count*i/10, count*(i+1)/10):  
        yyy.append(y[k - 1][j])  
        if y[k - 1][j] == 1:  
          answers[j - count*i/10] = k  
        xxx.append(x[k - 1][j])  
      # test sets  
      tarr.append((yyy, xxx))  
  
      print answers  
      # predicting  
      correct_count = 0  
      for j in range(0, len(tarr[0][0])):  
        max = 10000.0  
        maxidx = -1  
      for k in range(1, 11):  
        label, acc, val = svm_predict(tarr[k - 1][0][j:j+1], tarr[k - 1][1][j:j+1], marr[k - 1])  
    if abs(val[0][0] - 1.0) < max:  
      max = abs(val[0][0] - 1.0)  
      maxid = k  
      print "probably is", maxid, " answer is", answers[j]    
      if answers[j] == maxid:  
        correct_count += 1  
    correct_rate += float(correct_count) / len(tarr[0][0])  
  
  correct_rate /= 10  
  print 'c=',c,'g=',g,'avg_correct_rate=',correct_rate  
  return correct_rate  
  
def main():  
  yarr = []  
  xarr = []  
  for i in range(1, 11):  
    y, x = svm_read_problem('./dataocr/ocr_' + str(i))  
    yarr.append(y)  
    xarr.append(x)  
  #shuffle  
  arr = []  
  for i in range(0, len(yarr[0])):  
    arr.append(i)  
  random.shuffle(arr)  
  print "RANDOM ARR:",arr  

  count = len(yarr[0])  
  for i in range(1, 11):  
    yy = []  
    xx = []  
    y = yarr[i - 1]  
    x = xarr[i - 1]  
    for j in range(0, count):  
      yy.append(y[arr[j]])  
      xx.append(x[arr[j]]) 
    yarr[i - 1] = yy  
    xarr[i - 1] = xx  

  # grid search  
  maxcorrect = -1  
  cpos = 0  
  gpos = 0  
  for c in range(1, 16, 1):  
    for gg in range(0, 256, 1):  
      g = gg * 1.0 / 256  
      ret = test(yarr, xarr, c, g)  
      if ret > maxcorrect:  
        maxcorrect = ret  
        cpos = c  
        gpos = g  
    print "current c=",cpos,"g=",gpos,"maxcorrect=",maxcorrect   
  print "c=",cpos,"g=",gpos,"maxcorrect=",maxcorrect  
  #test(yarr, xarr, 3, 1.0 / 64)  

if __name__ == '__main__':  
  main() 
 