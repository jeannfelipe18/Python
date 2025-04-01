#class Person:
#    nome = ""
#    idade = 0

    #def get_Info(self):
        #print(f"Nome: {self.nome}, Idade: {self.idade}")

#p = Person()
#p.nome = 'Victor'
#p.idade = 19
#p.get_Info()

#class Person:

#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade

#    def __str__(self):
#        return f'{self.nome} tem {self.idade} anos'

#class Student(Person):
#    def __init__(self, nome, idade, matricula):
#        super().__init__(nome, idade)
#        self.matricula = matricula

#    def get_Info(self):
#        print(f"{self.nome} tem {self.idade} anos e sua matricula e {self.matricula}")

#p = Person('Victor', 19)
#p.display_info()

#s = Student('Yasmin', 20, '123456')
#s.display_info()

class Empregado:
 
    def __init__(self, nome, idade, matricula, salario):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.salario = salario

e = Empregado('Victor', 20, '212519', '1300,00')
e.display_info()