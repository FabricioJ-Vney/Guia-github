class Mascota:
    def __init__(self, nombre, especie, edad, vacunado):
        self.nombre = nombre        
        self.especie = especie       
        self.edad = edad             
        self.vacunado = vacunado     
        print(f"Se ha creado la mascota {self.nombre}!")

    def mostrar_info(self):
        print("\n--- Información de la Mascota ---")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        if self.vacunado:
            print("Vacunado: Sí")
        else:
            print("Vacunado: No")

    def vacunar(self):
        if not self.vacunado: 
            self.vacunado = True
            print(f"¡{self.nombre} vacunado")
        else: 
            print(f"{self.nombre} ya estaba vacunado.")

class Veterinaria:
    def __init__(self):
        self.lista_de_mascotas = [] 
        print("Secreado el objeto Veterinaria.")

    def agregar_mascota(self, mascota_objeto):
        self.lista_de_mascotas.append(mascota_objeto)
        print(f"{mascota_objeto.nombre} ha sido agregado a la veterinaria.")

    def mostrar_mascotas(self):
        print("\n===== MASCOTAS EN LA VETERINARIA =====")
        if not self.lista_de_mascotas: 
            print("No hay mascotas registradas en la veterinaria.")
            return 

        for mascota_actual in self.lista_de_mascotas:
            mascota_actual.mostrar_info() 
            print("---------------------------------") 


print("\n--- Creando Mascotas ---")
mascota1 = Mascota("Rex", "Perro", 5, False)  
mascota2 = Mascota("Mochi", "Gato", 2, True)   
mascota3 = Mascota("Niorkis", "Gato", 1, False)

print("\n--- Creando Veterinaria y Agregando Mascotas ---")
mi_veterinaria = Veterinaria() 

mi_veterinaria.agregar_mascota(mascota1)
mi_veterinaria.agregar_mascota(mascota2)
mi_veterinaria.agregar_mascota(mascota3)

print("\n--- MOSTRANDO MASCOTAS ANTES DE VACUNAR (A REX) ---")
mi_veterinaria.mostrar_mascotas()

print("\n--- Vacunando a una Mascota ---")
mascota1.vacunar()
mascota2.vacunar()

print("\n--- MOSTRANDO MASCOTAS DESPUÉS DE VACUNAR (A REX) ---")
mi_veterinaria.mostrar_mascotas()