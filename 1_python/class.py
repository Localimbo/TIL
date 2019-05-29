class Paper:
    def burn(self):
        return True

class CoffeCup(Paper) :        # 종이의 특징을 가지고 있음. paper의 상속
    content = None
    def burn(self):
        return True
    def pour(self):
        if self.content :
            return True
        else :
            return False

my_cup = CoffeCup()
my_cup.content = 'Americano'
my_cup.pour()

your_cup = CoffeCup()



tissue = Paper()
print(tissue.burn())

#####################################
class Fourth():
    late = '09:10'
    finish = '18:00'
    title = 'Deep learning.......'

class Student(Fourth):
    def set_values(self, name, age) :
        self.name = name
        self.age = age

#student1 = Student('랄랄랄',33)
#print(student1.title)

s = Student()
Student.set_values(s, '영은', 10)
print(s.name)

s.set_values('보림', 15)
print(s.name)