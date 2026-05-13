str=input()
out=""
for i in str:
    if i=="A":
        out+="D3"
    elif i=="'":
        out+=i
    elif i==" ":
        out+="&"
    elif i=="B":
        out+="D2"
    elif i=="C":
        out+="D1"
    elif i=="D":
        out+="D0"
    elif i=="+":
        out+="|"
print(out)