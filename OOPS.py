#1.CAR
# class car:
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f"brand:{self.brand},color:{self.color},year:{self.year}") 

# car1=car("toyota","red",2023)
# car1.display_info()
# car2=car("honda","black",2022)
# car2.display_info()  
# car3=car("hyundai","white",2019)
# car3.display_info()

# car1.brand="bmw"
# car1.display_info()

#2.DOG

# class Dog:
#     def __init__(self,color,breed):
#         self.breed=breed
#         self.color=color
#     def bark(self):
#         print(f":{self.color} colored {self.breed} barks")

# dog1=Dog("brown","germansheppard")
# dog2=Dog("black","dobberman")
# dog3=Dog("white","labrador")
# dog1.bark()
# dog2.bark()  
# dog3.bark()

# dog1.breed="cane corse"
# dog1.bark()

#3.STUDENT  
# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def marks(self):
#         if self.mark>=90:
#            print("GRADE:A")
#         elif self.mark>=70:
#              print("GRADE:B")

#         elif self.mark>=50:
#             print("GRADE:C")
             
#         else:
#             print("failed")
#     def student_info(self):
#         print(f"name:{self.name} marks:{self.mark}")       

# student1=Student("Nikhil",99) 
# student2=Student("sajitha",89)
# student1.student_info()
# student1.marks()          
                
#4 COMPANY
# class Employee:
#     company="abc company"

#     def __init__(self,name,position,age):
#         self.name=name
#         self.position=position
        

# emp1=Employee("Nikhil","manager")
# emp2=Employee("John","CEO") 

# print(emp1.name)
# print(emp2.name)
# print(emp1.position)
# print(emp2.position)


#INNER CLASS
# class Employee:
  
#     class Company:
#         def __init__(self,cname,location):
#                self.cname=cname
#                self.location=location

         
#     def __init__(self,name,salary,cname,location):
#         self.name=name
#         self.salary=salary
#         self.company=Employee.Company(cname,location) 
        

#     def display_employee(self):
#         print(f"Name:{self.name}, Salary:{self.salary}, Company:{self.company.cname}, Location:{self.company.location}")
       
       
        
      
# emp=Employee("john",50000,"xyz corp","London")
# emp.display_employee()

#TIGHTLY COUPLED
# class Company:
#     def __init__(self, cname, location):
#         self.name = cname
#         self.location = location
# class Employee:
#  def __init__(self, name, salary, cname, location):
#         self.name = name
#         self.salary = salary
#         self.company = Company(cname, location) 
# def display_employee(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company.cname}, Location: {self.company.location}")
# emp = Employee("John", 50000, "XYZ Corp", "London")
# emp.display_employee()
        
    
        



        
        