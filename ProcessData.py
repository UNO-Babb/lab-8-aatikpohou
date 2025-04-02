#ProcessData.py
#Name:
#Date:
#Assignment:

def makeID(first, last, num):
  if len(last) < 5:
    last = last + "XXXXXX"
    last = last[0:5]
  
  last3 = num[-3:]

  id = first[0] + last + last3 
  return id 

def makeMajorYear(major, year):
  first3 = major[0:3]
  year = year.upper()
  if year == "FRESHMAN":
    yearAb = "FR"
  elif year == "SOPHOMORE":
    yearAb = "SO"
  elif year == "JUNIOR":
    yearAb = "JR"
  elif year == "SENIOR":
    yearAb = "SR"
  majorYear = first3 + "-" + yearAb
  return majorYear

7
def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


  #Process each line of the input file and output to the CSV file
  for Student in inFile:

    #Student = "Antwan Dougherty AntwanDougherty@yahoo.com 443-13-3556 03/28/1996 Freshman Philosophy"
    StudentData = Student.split()
    firstName = StudentData[0]
    lastName = StudentData[1]
    StudentID = StudentData[3]
    year = StudentData[5]
    major = StudentData[6]
    userID = makeID(firstName, lastName, StudentID)
    majorYear = makeMajorYear(major, year)
    StudentOutput = lastName + ", " + firstName + "," + userID + "," + majorYear + "\n" 
    outFile.write(StudentOutput)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
