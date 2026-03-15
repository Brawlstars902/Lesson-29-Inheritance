class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def displayP(self):
        print('Name: ',self.name)
        print('ID:  ',self.id)

class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary=salary
        self.post=post
        super().__init__(name, id)

    def displayE(self):
        print('Name: ',self.name)
        print('ID:  ',self.id)
        print('Salary: ',self.salary)
        print('Post: ',self.post)

R=Employee('Arhaan',436,'$50000','intern')
P=Person('Eddie',71329)

print('\nAccessing Datafiles of Person: ')
P.displayP()

print('\nAccessing Datafiles of Employee: ')
R.displayE()

print()