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
        
def add_inventory(dictionary,item1, item2, item3):
    dictionary.append({"name_product" : item1, "price" : item2, "stock" : item3})
    print(f"Se agregó correctamente: {dictionary[-1]}")

def show_inventory(dictionary):
    if not dictionary:
        print("No hay productos en el inventario\n")
    else:
        for i,item in enumerate(dictionary):
            print(f"|Producto #{i+1}|Nombre:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}")

def search_inventory(itemionary,search):
    selected_product = None
    product_index= 0
    for j, inv in enumerate(itemionary):
        if inv["name_product"] == search:
            selected_product = inv
            product_index = j
        
    if selected_product is None:
        print("El producto no está registrado en la base de datos")
        return None
    else:
        print(f"El usuario se encuentra en la posición {j+1} de la base de datos \n")
        return inv[j]

def update_inventory(dictionary,search, name, new_price=None, new_stock=None):
    
    search["price"] = new_price
    search["stock"] = new_stock
    print(f"Se actualizó correctamente: {search}")

def delete_inventory(dictionary,item1):
    for j, inv in enumerate(dictionary):
        if inv["name_product"] == item1:
            selected_product = inv
            product_index = j
    dictionary.remove(j)
    print(f"Se eliminó correctamente el producto {dictionary["name_product"]}")

def calculate_stadistics(dictionary,item1, item2, item3):
    #**Estadísticas del inventario:**
    total_units = 0.0
    total_value = 0.0
    subtotal = 0.0
    #most_expensive_product
    #max_stock_product 
    for item in dictionary:

        if (item["price"]!= None) and (item["stock"]!= None):

            total_units += item["stock"]
            subtotal= (lambda p: p["stock"] * p["price"])
            print(f"Nombre del Producto:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}|subtotal:{subtotal}")
            total_value += subtotal
        else:
            print(f"Nombre del Producto:{item["name_product"]}|Precio:{item["unitary_price"]}|Cantidad:{item["stock"]}|subtotal:None")
    # # print(f"unidades Totales: {total_units}")
    # # print(f"Valor total del inventario: {total_value}")
    most_expensive_product_key = max(dictionary, key= lambda item: item["price"])
    most_expensive_product_value= dictionary[most_expensive_product_key]
    # # print(f"El producto {most_expensive_product_key} posee el mayor precio con un total de:$ {most_expensive_product_value}")
    max_stock_product_key = max(dictionary, key= lambda item: item["stock"])
    max_stock_product_value= dictionary[max_stock_product_key]
    # # print(f"El producto {max_stock_product_key} posee el mayor precio con un total de: {max_stock_product_value} unidades")
    metrics_tuple = (total_units, total_value, most_expensive_product_key, most_expensive_product_value, max_stock_product_key, max_stock_product_value)
    return metrics_tuple