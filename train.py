import Image  
import os  
  
file = []  
NUM = 35

for i in range(1, NUM):  
  file.append(open('dataocr/ocr_' + str(i), 'wb'))  

for i in range(1, NUM): 
  rootpath = "./datatrain/" + str(i) 
  for item in os.listdir(rootpath):  
    path = os.path.join(rootpath, item)
    if os.path.isfile(path) and path.endswith(".png"):  
      img_org = Image.open(path)  
      img = img_org.resize((36, 36), Image.NEAREST)  
      pixdata = img.load()  
      '''
      width = img.size[0]
      height = img.size[1]
      no = no + 1
      for x in range(width):
        for y in range(height):
          print no, ": ", x, " ", y, ": ", pixdata[x,y]
      '''
      # 1  
      line = "1 "  
      for k in range(0, 1296):  
        line += str(k + 1)  
        if pixdata[k / 36, k % 36][0] == 255:  
          line += ":0 "  
        else:  
          line += ":1 "  
      file[i - 1].write(line + "\n") 

      # -1 
      for j in range(1, i):  
        line = "-1 "  
        for k in range(0, 1296):  
          line += str(k + 1)
          if pixdata[k / 36,k % 36][0] == 255:  
            line += ":0 "  
          else:  
            line += ":1 "  
        file[j - 1].write(line + "\n")   
      for j in range(i + 1, NUM):  
        line = "-1 "  
        for k in range(0, 1296):  
          line += str(k + 1)  
          if pixdata[k / 36, k % 36][0] == 255:  
            line += ":0 "  
          else:  
            line += ":1 "  
        file[j - 1].write(line + "\n")  

for i in file:  
  i.close