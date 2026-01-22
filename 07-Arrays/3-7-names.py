names=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
LN=""
for name in names:
    if len(name) > len(LN):
        LN = name
print("Longest name:", LN)