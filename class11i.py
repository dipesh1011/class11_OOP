#Student Management System using classes
class student:
    def getdata(self):
        self.name=input("Enter Student Name:")
        self.sem=input("Enter Semester:")
        self.sid=input("Enter Student Id:")
        self.per=float(input("Enter percent:"))
    def showdata(self):
        print("*************************")
        print("Student Name:",self.name)
        print("Semester:",self.sem)
        print("SId:",self.sid)
        print("Percentage:",self.per)
    def check(self):
        if(self.per > 60):
            print("Congratulations!! You have first division.")
        else:
            print("No, first division")

s1=student()
s1.getdata()
s1.showdata()
s1.check()