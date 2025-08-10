from BibliotecaUsac.Biblioteca import Biblioteca
from BibliotecaUsac.LibrioDigital import LibroDigital
from BibliotecaUsac.LibroFisico import LibroFisico


def menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Registrar nuevo libro físico")
    print("2. Registrar nuevo libro digital")
    print("3. Listar todos los materiales")
    print("4. Prestar material")
    print("5. Devolver material")
    print("6. Mostrar información de un material")
    print("7. Salir")
    return input("Seleccione una opción: ")

def main():
    biblioteca = Biblioteca()
    while True:
        opcion = menu()
        if opcion == "1":
            titulo = input("Ingrese tu titulo: ")
            autor = input("Ingrese tu autor: ")
            num_ejemplar = int(input("Ingrese el numero de ejemplar: "))
            libro = LibroFisico(titulo,autor, num_ejemplar)
            biblioteca.agregarMaterial(libro)
            print("Libro agregado correctamente")

        elif opcion == "2":
            titulo = input("Ingrese tu titulo: ")
            autor = input("Ingrese tu autor: ")
            peso = float(input("Ingrese el peso (MB): "))
            libro = LibroDigital(titulo, autor, peso)
            biblioteca.agregarMaterial(libro)
            print("Libro agregado correctamente")

        elif opcion == "3":
            print("\n-----Listado de Material------")
            for material in biblioteca.listarMaterial():
                print(f"{material._codigo} - {material._titulo} ({type(material).__name__})")

        elif opcion == "4":
            codigo = input("Ingrese el código del material a prestar: ")
            if biblioteca.prestarMaterial(codigo):
                print("Material prestado con éxito")
            else:
                print("No se pudo prestar el material (no disponible o no encontrado)")

        elif opcion == "5":
            codigo = input("Ingrese el código del material a devolver: ")
            if biblioteca.devolverMaterial(codigo):
                print("Material devuelto con éxito")
            else:
                print("No se pudo devolver el material (no prestado o no encontrado)")

        elif opcion == "6":
            codigo = input("Ingrese el código del material a consultar: ")
            material = biblioteca.buscarMaterialPorCodigo(codigo)
            if material:
                print("\n=== Información del Material ===")
                print(material.mostrarInfo())
            else:
                print("Material no encontrado")

        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()