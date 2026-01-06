###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, "r") as file1:
   with open(position_file, "w") as file2:
      for line in file1:
         if job_title in line:
            file2.write(line)