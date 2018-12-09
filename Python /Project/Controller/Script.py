from Project.Modal.Empolyee import Employee
import json
import time;

class Crud:

    def __init__(self):
        print("=============================")

    def createEmpDetail(self):
        file = open("../Assets/EmpDetail.txt","w")
        file2 = open("../Assets/EmpDetail.txt","r")
        datas = dict(file2.read())

        no = raw_input("Enter The Employee Serail Number")
        name = raw_input("Enter The Name ")
        adder = raw_input("Enter The Address ")
        perf = raw_input("Enter The Preformance")
        pres = raw_input("Enter the Presents")
        abse = raw_input("Enter the Absents")
        objt = Employee()
        objt.setDetail(no, name, adder, perf, pres, abse)
        datas[no] = vars(objt.getDetail())
        file.write(json.dumps(datas))
        file.close()
        file2.close()

    def readDetail(self):
        file2 = open("../Assets/EmpDetail.txt","r")
        datas = dict(json.loads(file2.read()))
        for data in range(datas):
            print(data)
            time.sleep(1)
        file2.close()


print("create Data")
obj = Crud()
obj.createEmpDetail()