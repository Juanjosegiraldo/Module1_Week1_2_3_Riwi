def solicitude_string(message):
    while True:
        try:
            valor = input(message)
            if not valor.strip():
                raise ValueError("El texto no puede estar vacío.")
            return valor
        except ValueError as e:
                # Print the error message and the loop asks for input again
                print(f"Error: {e}. Inténtelo de nuevo.")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return "__CANCEL__"
        
def solicitude_float(message):
    while True:
        try:
            entrada = input(message).strip()

            # If the user does not enter anything or enters "None"
            if entrada == "" or entrada.lower() == "none":
                return None
            
            # Try to convert to float
            value = float(entrada)
            if value < 0:
                print("El número debe ser mayor o igual a 0.\n")
                continue
            return value # The value is returned only if it is a number and greater than 0

        except ValueError:
            print("Valor inválido. Debe ingresar un número o dejar vacío.\n")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return "__CANCEL__"
        
def solicitude_integer(message):
    while True:
        try:
            entrada = input(message).strip()

            if entrada == "" or entrada.lower() == "none":
                return None
            
            # Try to convert to integer
            value = int(entrada)
            if value < 0:
                print("El número debe ser mayor o igual a 0.\n")
                continue
            return value # The value is returned only if it is a number and greater than 0

        except ValueError:
            print("Valor inválido. Debe ingresar un número o dejar vacío.\n")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            return "__CANCEL__"
        
def add_inventory(dictionary,item1, item2, item3):
    dictionary.append({"name_product" : item1, "unitary_price" : item2, "stock" : item3})
    print(f"Se agregó correctamente: {dictionary[-1]}")

def show_inventory(dictionary):
    if not dictionary:
        print("No hay productos en el inventario\n")
    else:
        for i,item in enumerate(dictionary):
            print(f"|Producto #{i+1}|Nombre:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}")

def search_inventory(dictionary,search):
    selected_product = None
    product_index= 0
    for j, inv in enumerate(dictionary):
        if inv["name_product"] == search:
            selected_product = inv
            product_index = j
        
    if selected_product is None:
        print("El producto no está registrado en la base de datos")
        return None
    else:
        print(f"El usuario se encuentra en la posición {product_index+1} de la base de datos \n")
        return selected_product

def update_inventory(dictionary,search, name, new_price=None, new_stock=None):
    
    search["unitary_price"] = new_price
    search["stock"] = new_stock
    print(f"Se actualizó correctamente: {search}")

def delete_inventory(dictionary,item1):
    for j, inv in enumerate(dictionary):
        if inv["name_product"] == item1:
            selected_product = inv
            product_index = j
    dictionary.pop(product_index)
    print(f"Se eliminó correctamente el producto {selected_product["name_product"]}")

def calculate_stadistics(dictionary):
    #**Inventory statistics:**
    total_units = 0.0
    total_value = 0.0
    subtotal = 0.0
    for item in dictionary:

        if (item["unitary_price"]!= None) and (item["stock"]!= None):

            total_units += item["stock"]
            subtotal= (lambda p: p["stock"] * p["unitary_price"])
            print(f"Nombre del Producto:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}|subtotal:{subtotal(item)}")
            total_value += subtotal(item)
        else:
            print(f"Nombre del Producto:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}|subtotal:None")

    most_expensive_product_key = max(dictionary, key= lambda item: item["unitary_price"])
    name_expensive= most_expensive_product_key['name_product']
    price_expensive= most_expensive_product_key['unitary_price']
 
    max_stock_product_key = max(dictionary, key= lambda item: item["stock"])
    name_max_stock = max_stock_product_key['name_product']
    max_stock = max_stock_product_key['stock']

    metrics_tuple = (total_units, total_value, name_expensive, price_expensive, name_max_stock, max_stock)
    return metrics_tuple