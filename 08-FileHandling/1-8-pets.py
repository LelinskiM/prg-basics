def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_split = file_content.split()

x=0

for i in file_split:
   x+=1

print(file_content)
print(x)