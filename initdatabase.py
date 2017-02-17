# -*- coding: utf-8 -*-
import codecs 

start, end = (0x4E00, 0x9FA5) 

with codecs.open("database.txt", "wb", encoding="utf-8") as f: 
  for codepoint in range(int(start), int(end)): 
    f.write(unichr(codepoint)) 