import docx

f = open('E:\\computer\\name.csv', 'r')
ls = f.read().strip('\n').split('\n')
f.close()

# 生成txt文件
for name in ls:
    f2 = open('E:\\computer\\txt\\'+name+'.txt', 'w')
    f2.close()

# 生成word文件
doc = docx.Document()
for name in ls:
    doc.save('E:\\computer\\word\\'+name+'.docx')
