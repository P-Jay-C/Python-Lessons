import openpyxl



with open('text.txt','r') as rf:
    with open('text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)