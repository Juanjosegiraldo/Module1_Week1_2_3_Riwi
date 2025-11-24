# PRODUCT REGISTRATION
#Autor Juan Jose Giraldo Muñoz

print(f"###PRODUCT REGISTRATION###") # Print in console a title

#I Initialize variables

#Lists
product_name = []
product_price = []
quantity = []
cost = []

#String
name= ""

#float
price = 0.0
unit_cost =0.0
total_cost = 0.0

#int
quant = 0
total_units = 0
option = 0
option_menu = 0
i = 0

try: # Attempt to execute code that may raise an error

    while True:
        # Repeat until a valid condition is met
        option = int(input(f"""
    Ingrese:
    1 para agregar un producto
    2 para calcular unidades totales
    3 para calcular costo total
    4 para salir: \n""")) #Option Menu with 4 possible options

        if option==1: #Enter if that condition is met

            name = input(f"\ningrese nombre del producto: ") # product name request 
            product_name.append(name) # Add product to a list

            while True:

                try:
                    price = float(input("ingrese el precio: ")) # # product price request 
                except ValueError: # Handle invalid numeric input
                    print("Debe ingresar un número válido")
                    continue # return to the beginning of the while loop if price isn't number
                if price >= 0: # Check if the value is greater than or equal to zero
                    product_price.append(price)
                    break # exit of the while loop
                else: # Execute this block if the condition is not met
                    print("Debe ingresar un número mayor o igual a 0")

            while True:
                try:
                    quant = int(input(f"ingrese la cantidad en unidades del producto: ")) # request for product quantities
                except ValueError: 
                    print("Debe ingresar un número válido")
                    continue #the cycle starts again to request a value

                # Check that the value entered is greater than 0
                if quant >= 0: # If it is correct, add it to the list
                    quantity.append(quant) 
                    break
                else: # otherwise, request the value again.
                    print("Debe ingresar un número mayor o igual a 0")
                
                
        elif option ==2:
            for i in range(len(quantity)): #It is guaranteed that the entire list will be traversed by setting the size of the list.
                total_units = total_units + quantity[i] # An accumulator is used to add each of the elements in a list
            print(f"Unidades en total: {total_units}") # the total costs are printed

        elif option ==3:
            # Let's create a for loop that goes through the elements of a list and calculates the costs.
            for i in range(len(quantity)): 
                unit_cost = quantity[i] * product_price[i]
                cost.append(unit_cost)
                total_cost = total_cost + cost[i]
            option_menu=0        
            while option_menu ==0:
                option_menu= int(input(f"""
    Ingrese 1 para saber el costo unitario por producto y el costo total en general.
    ingrese 2 para saber solo el costo total en general: """, )) # The user is asked which costs they want to view.
                    
                if(option_menu==1):
                    print("")
                    for i in range(len(product_name)):
                        #All registered products are printed with their name, price, quantity, unit cost, and total cost.
                        print(f"Producto {product_name[i]} | Precio: $ {product_price[i]} | Cantidad: {quantity[i]} | Total: $ {cost[i]} ")
                    print("")
                    print(f"El costo total de todos los productos es: $ {total_cost}")

                elif(option_menu==2):
                    # the total cost is printed
                    print(f"El costo total de todos los productos es: $ {total_cost}")

                else:
                    # If you do not enter valid data, return and you will be asked to enter the value.
                    print("Ingresó valor inválido")
                    print("")
                    option_menu=0

        elif option ==4:
            # It says goodbye and ends the cycle and the code.
            print("Gracias por elegirnos, que tengas un buen día")
            break
        else:
            print("Ingresó valor inválido")
except KeyboardInterrupt: #If the user interrupts the code with a key combination, the exception is handled correctly.
    print("\nSe interrumpió el programa con Ctrl+C")

##general comment##

#When the program starts, the variables and lists are declared and initialized.
#If the user interrupts the code with a key combination, the exception is handled correctly.
#The code has a menu with four available options (1-4). If you enter a different value, 
#you will be asked to re-enter a value within the range. Option 1 allows you to add a product, 
#option 2 calculates total units, option 3 calculates total cost (There is another submenu that 
# asks if you want to see the unit cost of each product) and option 4 is for exiting.