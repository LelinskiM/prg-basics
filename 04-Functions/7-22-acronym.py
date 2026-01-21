def f(names):
    acronym = ""
    for name in names.split():
        acronym += name[0]
    return acronym

print(f("Internet of Things")) #returns "IoT"
print(f("For Your Information")) #returns "FYI"
print(f("Python")) #returns "P"