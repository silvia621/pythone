class Employee : 
    def __init__(self, nome, cognome, salario) :
        self._nome = nome
        self._cognome = cognome 
        self._salario = salario
    def setName(self, nome) : 
        self._nome = nome
    def setSurname(self, cognome) :
        self._cognome = cognome
    def setSalary(self, salario) :
        self._salary = salario

class Manager(Employee) : #derivo dalla classe Employee
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self._department = reparto
    def __repr__(self) :
        return self._nome + " " + self._cognome + " lavora nel reparto " + self._department + " il suo salario è di " + self._salario
    
luca = Manager("Luca", "Rossi", "70000", "Marketing")
print(luca)