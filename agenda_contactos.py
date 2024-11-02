




def mostrar_menu():
    print("\nAgenda de contactos")
    print("1. Agregar nuevo contactos")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")

def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto: ")
    apellido = input("Introduzca el apellido del contacto: ")
    telefono = input("Introduzca el telefono del contacto: ")
    email = input("Introduzca el email del contacto: ")
    agenda[nombre] = {"apellido": apellido, "telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} {apellido} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea elinminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado {nombre} en la agenda")

def buscar_contacto(agenda):
    nombre = input("Ingrese el contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Apellido: {agenda[nombre]["apellido"]}")
        print(f"Telefono: {agenda[nombre]["telefono"]}")
        print(f"Email: {agenda[nombre]["email"]}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def lista_de_contactos(agenda):
    if agenda:
        print("\nLista de Contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Apeliido: {info["apellido"]}")
            print(f"Email: {info["email"]}")
            print(f"Telefono: {info["telefono"]}")
            print("-" * 11)

    else:
        print("La agenda aun esta vacia")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            lista_de_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos. Hasta Luego!")
            break
        else:
                print("Por favor seleccione una opcion correcta")

agenda_contactos()