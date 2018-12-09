class Employee:
    sNo = 0
    name = ""
    addr = ""

    def __init__(self, no, name, addr):
        self.sNo = no
        self.name = name
        self.addr = addr

    def getEmployeeDetail(self):
        return self.name


obj = Employee(1, "Nagaraj", "chennai");

print obj.getEmployeeDetail();



# !/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
