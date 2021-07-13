#mian xiang dui xiang 

#类和实例
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

chai = Student('chai', 100)
print(chai.get_grade())

#====================
#访问限制
class Student2(Student):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        if gender =='male' or 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')


bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('ce shi shi bai1')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('ce shi shi bai2')
    else:
        print('ce shi cheng gong!')

#====================
#继承和多态



#=========================
#实例属性和类属性
class Student3(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student3.count +=1

if Student3.count != 0:
    print('ce shi shi bai3')
else:
    bart = Student3('Bart')
    if Student3.count != 1:
        print('ce shi shi bai3-2', Student3.count)
    else:
        lisa = Student3('Bart')
        if Student3.count != 2:
            print('ce shi shi bai-3-!')
        else:
            print('Students:', Student3.count)
            print('ce shi tong guo3')

#====================
#使用@property
class Screen(object):
    
    @property
    def wh(self):
        return self.width, self.height

    @wh.setter
    def wh(self, value1, value2):
        self.width = value1
        self.height = value2
    
    @property
    def resolution(self):
        return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution = ',  s.resolution)
if s.resolution == 786432:
    print('ce shi tong guo4!')
else:
    print('ce shi shi bai!')

#========================
#使用枚举类
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student4(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student4('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('ce shi tong guo5!')
else:
    print('ce shi shi bai')