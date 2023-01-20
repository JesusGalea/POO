class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mayoria(self):
        if self.age >= 18:
            print(self.name, "tiene", self.age, ". Es mayor de edad")
        else:
            print(self.name, "tiene", self.age, ". Es menor de edad")


Sarita = Persona("Sarita", 22)

Sarita.mayoria()