d={1:'s',26:'w',3:'h',4:'u'}   #dictionaries ae unordered, there are no indexes, only keys and values.
new_d={k:v for k,v in d.items() if k!=1}
d.pop(26)
del d[3]
print(d)
print(new_d)