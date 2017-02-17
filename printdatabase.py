# -*- coding: utf-8 -*-
import os
import codecs
import StringIO
import Image, ImageFont, ImageDraw
import pygame

pygame.init()

'''
start,end = (0x4E00, 0x9FA5) 
with codecs.open("database.txt", "wb", encoding="utf-8") as f: 
  for codepoint in range(int(start),int(end)): 
    f.write(unichr(codepoint)) 
'''

f = open('database.txt','rb')
fread = f.read()
text = fread.decode('utf-8')

im = Image.new("RGB", (1000, 1000), (255, 255, 255))
font = pygame.font.Font(os.path.join("fonts", "msyh.ttc"), 22)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))

sio = StringIO.StringIO()
pygame.image.save(rtext, sio)
sio.seek(0)
line = Image.open(sio)
im.paste(line, (10, 5))
im.show()
im.save("database.png")