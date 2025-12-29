scan =  "These+notes#reveal9Newton seeking-out an(lunderlying structure to/the\\pyramid:the unit of measurement?used>by its builders."
clean = ''

for x in scan:
    if x.isalpha() or x.isspace():
       clean += x
    else:
        clean = clean + ' '
print(clean)
