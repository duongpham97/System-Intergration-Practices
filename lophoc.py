import json
class lophoc:
    def __init__(self,name,student,teacher):
        self.name = name
        self.student = student
        self.teacher = teacher
    def  getClassname(self):
        return self.name;
    def  getStudent(self):
        return self.student
    def getTeacher(self):
        return self.teacher
    def toString(self):
        data = '{\n"Class Name":"%s",\n"Student":"%s",\n"Teacher":"%s"\n}'%(self.name,self.student,self.teacher)
        return data
    def showInfo(self):
        s = self.toString()
        data = json.load(s)
        return data