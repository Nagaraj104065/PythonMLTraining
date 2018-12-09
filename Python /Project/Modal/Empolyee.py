class Employee:

    sNo = 0
    name = ""
    addr = ""
    performance = 0
    presents = 0
    absents = 0
    detail = ""

    def __init__(self):
        print("object created")

    def setNo(self, no):
        self.sNo = no

    def setName(self, name):
        self.name = name

    def setAddr(self, addr):
        self.addr = addr

    def setPerformance(self, perf):
        self.performance = perf

    def setDetail(self, no, name, addrs, perf, pre, abss):
        self.setNo(no)
        self.setName(name)
        self.setAddr(addrs)
        self.setPerformance(perf)
        self.presents = pre
        self.absents = abss
        self.detail = ""+self.sNo+","+self.name+","+self.addr+","+self.performance+","+self.presents+","+self.absents+""

    def getDetail(self):
        return self
