class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def isMinor(self):
       if self.age <= 18:
           return True
       else:
           return False

new_person = Person("Sam Smith", 32)
print(new_person.isMinor())



class Classroom:
   def __init__(self, numberOfStudents, numberofDesks, course):
       self.numberOfStudents = numberOfStudents
       self.numberOfDesks = numberofDesks
       self.course = course

   def __str__(self):
       return "There are "+ str(self.numberOfDesks)+ " desks in "+ self.course

room205 = Classroom(16, 20, "Grade 12 Computer Science")
print(room205)


class Classroom:
   def __init__(self, numberOfStudents, numberofDesks, course):
       self.numberOfStudents = numberOfStudents
       self.numberOfDesks = numberofDesks
       self.course = course

   def __len__(self):
       return self.numberOfStudents

room205 = Classroom(16, 20, "Grade 12 Computer Science")
print(len(room205))


class Banks:
    def __init__(self,name,manager,numberOfBusses):
        self.name = name
        self.manager = manager
        self.numberOfBusses = numberOfBusses

    def __str__(self):
        return self.name + " has the manager name" + self.manager

tangerine = Banks("Tangerine","Nolan",11)
print(tangerine)

