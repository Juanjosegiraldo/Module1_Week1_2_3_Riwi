# **Historia de usuario - Semana 2**

## **Control de flujo y manejo de listas en el inventario**

# autor: Juan Jose Giraldo Muñoz

dic_inventory=[{"name" : "playstation 5",
              "unitary_price":1500000,
              "stock":7},
              {"name" : "sombrero elegante",
              "unitary_price":50000,
              "stock":103},
              {"name" : "star wars LEGO",
              "unitary_price":200000,
              "stock":2},
              {"name" : "caminadora",
              "unitary_price":13000000,
              "stock":5}]

def menu1():
        try:
            option = int(input("""\nIngrese 1 para agregar un artículo
    \nIngrese 2 para mostrar los articulos del inventario
    \nIngrese 3 para calcular las estadisticas
    \nIngrese 4 para salir:\n"""))
            if option >=1 and option <=4:
                return option
        except ValueError:
            print("Ingresó valor inválido")
            return None
        except KeyboardInterrupt:
            print("Entrada cancelada por el usuario")
            return None
    
def solicitude_string(message):
    while True:
        try:
            valor = input(message)
            if not valor.strip():
                raise ValueError("El texto no puede estar vacío.")
            return valor
        except ValueError as e:
                # Imprime el mensaje de error y el bucle vuelve a pedir la entrada
                print(f"Error: {e}. Inténtelo de nuevo.")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return None

def solicitude_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Ingresó valor inválido, intente de nuevo.\n")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return None

def opt1(element1, element2, index ,list, final_list):
    final_list.append({
        "name_product": element1,
        "price": list[index]["price"],
        "quantity": element2
    })
    list[index]["stock"] = list[index]["stock"] - element2
    return list, final_list

def opt2(dic):
    for  index,i in enumerate(dic):
        print(f"|Producto #{index}|name:{i["name"]}|Price:{i["unitary_price"]}|Stock:{i["stock"]}")


def opt3(dic):
    total_price_inventory=0
    for  index,i in enumerate(dic):
        total_price = 0
        total_price = i["unitary_price"]*i["stock"]
        total_price_inventory += total_price 
        print(f"|Producto #{index+1}|name:{i["name"]}|Price:{i["unitary_price"]}|Stock:{i["stock"]}|Precio total: ${total_price}")    
    print(f"El precio total de todos los artículos del inventario es de: ${total_price_inventory}")

print("\nBienvenido al inventario M2S2\n")
option = -1
try: 
    while option != 0:
        option = menu1()

        if option == None:
            print("Se interrumpió la ejecución del programa con Ctrl C")
            option = 0

        elif option == 1:
            product = solicitude_string(f"Ingrese el nombre del articulo: ")
            price = solicitude_float(f"Ingrese el precio unitario del articulo: ")
            stock = solicitude_float(f"Ingrese la cantidad de artículos: ")

            dic_inventory.append({"name": product, "unitary_price": price, "stock" : stock})
            print(f"se agregó correctamente: {dic_inventory[-1]}")

        elif option == 2:
            opt2(dic_inventory)
            
        elif option == 3:
            opt3(dic_inventory)

        elif option == 4:
            option = 0
except KeyboardInterrupt:
    print("Se interrumpió el programa con ctrl C")