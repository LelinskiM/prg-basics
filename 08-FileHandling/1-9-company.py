###
# Prints employees employed in a specified position.
#

# Employee List

file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

# Position
job_title = 'Software Engineer'

with open("it_company.csv", "r") as file:
   for line in file_name:
      if job_title in file_name:
         print(file_name.splitlines)



def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('it_company.csv')
file_lines = file_content.splitlines()

for i in file_lines:
   if job_title in file_lines:
      print(file_lines)