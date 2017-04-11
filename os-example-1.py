'''
内建的 open / file 函数用于创建, 打开和编辑文件, 如 下例 所示.
而 os 模块提供了重命名和删除文件所需的函数
'''

import os
import string
def replace(file, search_for, replace_with):
    # replace strings in a text file
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"
    try:
        # remove old temp file, if any
        os.remove(temp)
    except os.error:
        pass
    
    fi = open(file)
    fo = open(temp, "w")
    for s in fi.readlines():
        fo.write(string.replace(s, search_for, replace_with))
    
    fi.close()    
    fo.close() 
    try: # remove old backup file, if any 
        os.remove(back)
    except os.error: 
        pass # rename original to backup...
    
    os.rename(file, back) # ...and temporary to original os.rename(temp,file)
    
    
# # try it out!
file = "samples/sample.txt"
replace(file, "hello", "tjena")
replace(file, "tjena", "hello")