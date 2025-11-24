# **User Story - Week 2**

## **Flow control and list management in inventory**

# autor: Juan Jose Giraldo Muñoz

#We initialize the dictionary with data.
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
    #We create our menu of 4 options in a function, 
    # exceptions are handled to ensure that the user correctly enters the allowed values.
    while True:    
        try:
            option = int(input("""\nIngrese 1 para agregar un artículo
    \nIngrese 2 para mostrar los articulos del inventario
    \nIngrese 3 para calcular las estadisticas
    \nIngrese 4 para salir:\n"""))
            if option >=1 and option <=4:
                return option
        except ValueError:
            print("Ingresó valor inválido, intente de nuevo")
        except KeyboardInterrupt:
            print("Entrada cancelada por el usuario")
            return None
    
def solicitude_string(message):
    #function that receives as a parameter the message 
    # that will be displayed to the user to enter an input and returns a string
    while True:
        try:
            valor = input(message)
            if not valor.strip(): # Blank spaces are removed and the variable is evaluated to see if it is empty.
                raise ValueError("El texto no puede estar vacío.") # A ValueError exception is thrown indicating that empty entries are not accepted.
            return valor
        except ValueError as e:
                # Imprime el mensaje de error y el bucle vuelve a pedir la entrada
                print(f"Error: {e}. Inténtelo de nuevo.")
        except KeyboardInterrupt: #The attempt to cancel the program is controlled with an exception.
            print("\nEntrada cancelada por el usuario.")
            return None

def solicitude_float(message):
    #returns a float greater than or equal to 0, returns None if the operation is canceled
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("El número debe ser mayor o igual a 0.\n")
                continue
            return value # The value is returned only if it is a number and greater than 0
        except ValueError:
            print("Ingresó valor inválido, intente de nuevo.\n")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return None

def add_product(element1, element2, element3, list):
    # The dictionary elements are added with the same key-value structure.
    list.append({
        "name": element1,
        "unitary_price": element2,
        "stock": element3
    })
    print(f"Se agregó correctamente: {list[-1]}") #print the last position in the list

def show_inventory(list_dic):

    if not list_dic: #we validate if the inventory has items
        print("El inventario está vacío\n")
    
    else:
        for  index,i in enumerate(list_dic): #We print the elements of the dictionaries in each position of the list.
            print(f"|Producto #{index}|name:{i["name"]}|Price:{i["unitary_price"]}|Stock:{i["stock"]}")


def calculate_stadistics(dic):

    if not dic: #we validate if the inventory has items
        print("El inventario está vacío\n")
    
    else:
        #We initialize variables to 0 to ensure accurate operations without residual data.
        total_price_inventory=0.0
        total_price = 0.0
        total_stock = 0.0
        for  index,i in enumerate(dic):
            total_stock += i["stock"] #We accumulate all the quantities of the products in a variable.
            total_price = i["unitary_price"]*i["stock"] # operation to determine the unit cost
            total_price_inventory += total_price # We accumulate all the costs of the products in a variable
            print(f"|Producto #{index+1}|name:{i["name"]}|Price:{i["unitary_price"]}|Stock:{i["stock"]}|Precio total: ${total_price}")
        print(f"\nLa cantidad total de todos los artículos del inventario es de: {total_stock}") 
        print(f"El precio total de todos los artículos del inventario es de: ${total_price_inventory}")

print("\nBienvenido al inventario M2S2\n")
option = -1
try: 
    while option != 0: #The cycle is only broken if option is equal to 0.
        option = menu1() #we use a function to display a menu of options

        if option == None:
            print("Se interrumpió la ejecución del programa con Ctrl C")
            option = 0

        elif option == 1:
            product = solicitude_string(f"Ingrese el nombre del articulo: ")
            if (product==None):
                print("Se interrumpió la ejecución del programa con Ctrl C")
                option = 0
                continue
            else:
                price = solicitude_float(f"Ingrese el precio unitario del articulo: ")
                if (price==None):
                    print("Se interrumpió la ejecución del programa con Ctrl C")
                    option = 0
                    continue
                else:
                    stock = solicitude_float(f"Ingrese la cantidad de artículos: ")
                    if (price==None):
                        print("Se interrumpió la ejecución del programa con Ctrl C")
                        option = 0
                        continue
                    else:
                        #When all three values have been validated, 
                        # the function that adds a product to the list is called.
                        add_product(product, price, stock, dic_inventory)

        elif option == 2:
            show_inventory(dic_inventory)
            
        elif option == 3:
            calculate_stadistics(dic_inventory)

        elif option == 4:
            option = 0 #Assigning 0 to the variable option ends the program because it exits the While loop.

except KeyboardInterrupt:
    print("Se interrumpió el programa con ctrl C")

##Final Comment:

#The program has a list of dictionaries with data from an inventory product already loaded. 
# It has a menu with four options, each option calling a function that performs an operation 
# and prints or returns a value:
# Option 1: adds an item.
# Option 2: displays the items in the inventory.
# Option 3: calculates statistics.
# Option 4: exits.
#Exceptions are handled for both erroneous values and keyboard interruptions.