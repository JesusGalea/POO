"1 – Realizar un programa que conste de una clasellamadaAlumno que tengacomoatributos el nombre y la nota del alumno. "
"Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si"
"ha aprobado o no. "

class Alumno:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def nota(self):
        if self.grade >= 5:
            print(self.name, "ha aprobado con un: ", self.grade)
        else:
            print(self.name, "ha suspendido con un: ", self.grade)


Sara = Alumno ("Sara", 4.5)

Sara.nota()