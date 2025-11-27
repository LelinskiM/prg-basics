###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

      # Name of the file to write to
file_name = 'seven_wonders.txt'
seven_wonders.sort()

# Sort data alphabetically
file_content = read_from_file('seven_wonders.txt')
split_file = file_content.split()
sorted_file = sorted(split_file)
print(sorted_file)

# Write data to the file
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item+"\n")
