# -*- coding: utf-8 -*-
import os
import codecs
import StringIO
import Image, ImageFont, ImageDraw
import pygame
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

pygame.init()
start, end = (0x4E00, 0x9FA5) 
with codecs.open("database.txt", "wb", encoding="utf-8") as f: 
  for codepoint in range(int(start), int(end)): 
    f.write(unichr(codepoint)) 

DATADIR = 'database'
if not os.path.exists(DATADIR): 
  os.mkdir(DATADIR) 

i = 0
for codepoint in range(int(start), int(end)): 
  i = i + 1  
  rootpath = "./datatrain/" + str(i)
  os.makedirs(rootpath) 
  word = unichr(codepoint)

  im = Image.new("RGB", (360, 360), (255, 255, 255))
  font = pygame.font.Font("./fonts/simsun.ttc", 360)
  rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) 
  sio = StringIO.StringIO()
  pygame.image.save(rtext, sio)
  sio.seek(0)
  line = Image.open(sio)
  im.paste(line, (0, 0))
  path = rootpath + "/simkai.png"
  im.save(path)
  print i, line.size

  im = Image.new("RGB", (360, 360), (255, 255, 255))
  font = pygame.font.Font("./fonts/Deng.ttf", 360)
  rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) 
  sio = StringIO.StringIO()
  pygame.image.save(rtext, sio)
  sio.seek(0)
  line = Image.open(sio)
  im.paste(line, (0, 0))
  path = rootpath + "/Deng.png"
  im.save(path)
  print i, line.size

  im = Image.new("RGB", (360, 360), (255, 255, 255))
  font = pygame.font.Font("./fonts/simhei.ttf", 360)
  rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) 
  sio = StringIO.StringIO()
  pygame.image.save(rtext, sio)
  sio.seek(0)
  line = Image.open(sio)
  im.paste(line, (0, 0))
  path = rootpath + "/simhei.png"
  im.save(path)
  print i, line.size

  im = Image.new("RGB", (360, 360), (255, 255, 255))
  font = pygame.font.Font("./fonts/simsun.ttc", 360)
  rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) 
  sio = StringIO.StringIO()
  pygame.image.save(rtext, sio)
  sio.seek(0)
  line = Image.open(sio)
  im.paste(line, (0, 0))
  path = rootpath + "/simsun.png"
  im.save(path)
  print i, line.size