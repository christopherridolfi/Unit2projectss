class School:
    def __init__(self,numbofstudents,numofdesks,course):
        self.numberOfStudents = numbofstudents
        self.numberOfDesks = numofdesks
        self.Course = course

room205 = School(16,20,"grade 12 Computer Science")
print(room205.numberOfDesks)
room211 = School(19,19,"grade 11 Computer Science")
print(room211.numberOfDesks)

class Car:
    def __init__(self,numofdoor,numofwheel):
        self.numberOfdoor = numofdoor
        self.numberofwheel = numofwheel

coupe = Car(2, 4)
print(coupe.numberOfdoor)
