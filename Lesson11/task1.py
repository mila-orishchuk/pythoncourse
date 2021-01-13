'''
School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
should only be available to the teacher.

'''


class Person:
    def __init__(self, person_data):
        self.name = person_data.get('name')
        self.surname = person_data.get('surname')
        self.age = person_data.get('age')
        self.gender = person_data.get('gender')

    def talk(self):
        print("Hello, I'm", self.name, self.surname, "and I'm", self.age)

    def walk(self):
        print(self.name, "can walk")


class Student(Person):
    skills = []

    def learn(self, skill):
        self.skills.append(skill)

    def print_skills(self):
        print(self.name, self.surname, "knows", *self.skills)


class Teacher(Person):
    def __init__(self, person_data):
        super().__init__(person_data)
        self.salary = person_data.get('salary')
        self.ratio = person_data.get('ratio') or 1

    def count_salary(self):
        return self.salary * self.ratio


if __name__ == '__main__':
    person = Person({'name': "Carl", 'surname': "Johnson",
                     'age': 26, 'gender': 'male'})
    person.talk()
    person.walk()
    student = Student({'name': "Nina", 'surname': "Manson",
                       'age': 13, 'gender': 'female'})
    student.learn('python')
    student.print_skills()
    teacher = Teacher({'name': "Egor", 'surname': "Azimov",
                       'age': 38, 'gender': 'male', 'salary': 300, 'ratio': 2.5})
    print(teacher.count_salary())
