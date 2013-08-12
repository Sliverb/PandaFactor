import os, csv

############ All you need to modify is below ############
# Full path and name to your csv file
defaultDirectory = os.getcwd()
csv_name = "data.csv"
csv_filepathname=os.path.join(defaultDirectory, csv_name)

BusFName = "James"
BusLName = "Shaw"
BusEmail = "business"
BusMask = 1
BusDOB = "1985-11-17"

SchFName = "Emily"
SchLName = "Haines"
SchEmail = "school"
SchMask = 2
SchDOB = "1974-01-25"

StuFName = "Joshua"
StuLName = "Winstead"
StuEmail = "student"
StuMask = 4
StuDOB = "1987-12-17"

Phone = "(555) 555-5555"
LastLoginAt = "2013-08-07"
LastLogin = "2013-08-07 17:41:20.401000"
isActive = 1
isSuperUser = 0
Address = ""
isAdmin = 1
password = "pbkdf2_sha256$10000$8Vg9ZXHAMPmO$pMk5rLQleqCX3PFSlA96iBJixN5VzquyVPSKc8bwWUU="


############ All you need to modify is above ############
f = open(csv_filepathname, 'w')
dataWriter = csv.writer(f, delimiter=',', quotechar='"')

##Business
for x in range(1, 50):
    dataWriter.writerow([BusFName + str(x), BusLName + str(x), Phone, BusMask, LastLoginAt, isActive, BusEmail + str(x) + "@test.com", isSuperUser, BusDOB, LastLogin, Address, isAdmin, password, x + 3])
	
##School
for x in range(50, 100):
    dataWriter.writerow([SchFName + str(x), SchLName + str(x), Phone, SchMask, LastLoginAt, isActive, BusEmail + str(x) + "@test.com", isSuperUser, SchDOB, LastLogin, Address, isAdmin, password, x + 3])

##Student
for x in range(100, 150):
    dataWriter.writerow([StuFName + str(x), StuLName + str(x), Phone, StuMask, LastLoginAt, isActive, BusEmail + str(x) + "@test.com", isSuperUser, StuDOB, LastLogin, Address, isAdmin, password, x + 3])

f.close()
