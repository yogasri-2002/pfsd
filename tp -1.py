class Students:
    '''def init(self,StudentId,StFiname,StLaname,Course,Year,GPA,University,Email,Mobile):
        self.StudentId=StudentId
        self.StFiname=StFiname
        self.StLaname=StLaname
        self.Course=Course
        self.Year=year
        self.GPA=GPA
        self.University=University
        self.Email=Email
        self.Mobile=mobile'''
    def setStudentId(self , StudentId):
        self.StudentId=StudentId
    def getStudentId(self):
        return self.StudentId
    def setStFiname(self , StFiname):
        self.StFiname=StFiname
    def getStFiname(self):
        return self.StFiname
    def setStLaname(self , StLaname):
        self.StLaname=StLaname
    def getStLaname(self):
        return self.StLaname
    def setCourse(self , Course):
        self.Course=Course
    def getCourse(self):
        return self.Course
    def setYear(self , Year):
        self.Year=Year
    def getYear(self):
        return self.Year
    def setGPA(self , GPA):
        self.GPA=GPA
    def getGPA(self):
        return self.GPA
    def setUniversity(self , University):
        self.University=University
    def getUniversity(self):
        return self.University
    def setEmail(self , Email):
        self.Email=Email
    def getEmail(self):
        return self.Email
    def setMobile(self , Mobile):
        self.Mobile=Mobile
    def getMobile(self):
        return self.Mobile
d=Students()
d.setStudentId(2000080056)
d.setStFiname("Lella")
d.setStLaname("yoga sri ")
d.setCourse("AI&DS")
d.setYear(3)
d.setGPA(9.2)
d.setUniversity("KLU")
d.setEmail("sweety84g@gmail.com")
d.setMobile(1234567890)
print(d.getStudentId())
print(d.getStFiname())
print(d.getStLaname())
print(d.getCourse())
print(d.getYear())
print(d.getGPA())
print(d.getUniversity())
print(d.getEmail())
print(d.getMobile())