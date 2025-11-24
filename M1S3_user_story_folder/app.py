## Historia de usuario - Semana 3

#Autor: Juan Jose Giraldo Muñoz

#we import Python modules
import services
import files
import os

#Messages are printed in Spanish, a program aimed at Spanish-speaking users.
print("Bienvenido al inventario avanzado con colecciones y persistencia en archivos")

#we initialize variables
option = -1
dictionary_inventory = []
dictionary_returned = []
load_option = ""
file_name_path = "inventory_file.csv"

while option !=0:
    try:
        #menu with 9 options
        option = int(input("""\nIngrese 1 para agregar un producto en el inventario.
    \nIngrese 2 para mostrar los productos del inventario.
    \nIngrese 3 para actualizar un producto del inventario.
    \nIngrese 4 para buscar un producto del inventario.
    \nIngrese 5 para eliminar un producto del inventario.                  
    \nIngrese 6 para generar estadísticas como el precio total de cada producto, 
el precio total de todo el inventario, producto con mayor precio y
producto con mayor stock
    \nIngrese 7 para guardar archivo
    \nIngrese 8 para cargar en archivo CSV    
    \nIngrese 9 para salir:\n"""))
        if option >=1 and option <=9:
            match option: # control structure that allows a value to be compared against multiple patterns.
                
                case 1:
                    # Different functions are used to request values from the user.
                    product = services.solicitude_string(f"Ingrese el nombre del articulo: ")
                    if product == None: # The user can cancel the entry and return to the menu with Ctrl+C
                        continue
                    else:
                        price = services.solicitude_float(f"Ingrese el precio unitario del articulo: ")
                        if price == "__CANCEL__":
                            continue
                        else:
                            stock = services.solicitude_integer(f"Ingrese la cantidad de artículos: ")
                            if stock == "__CANCEL__":
                                continue
                            else: #A product is added only if all conditions are met.
                                services.add_inventory(dictionary_inventory, product, price, stock)

                case 2:
                    #we display the product data with a function
                    services.show_inventory(dictionary_inventory) 

                case 3:
                    # To update a product, we first check whether it exists in the inventory.
                    update_product = services.solicitude_string(f"Ingrese el nombre del articulo que desa actualizar: ")
                    search_product= services.search_inventory(dictionary_inventory,update_product) 

                    if search_product is not None: #Only if the product exists, we request the values to be updated.
                    
                        update_price = services.solicitude_float(f"Ingrese el precio unitario del articulo que desea actualizar: ")
                        if update_price == "__CANCEL__":
                            continue
                        else:
                            update_stock = services.solicitude_integer(f"Ingrese la cantidad del artículo que desea actualizar: ")
                            if update_stock == "__CANCEL__":
                                continue
                            else:
                                # If the variables entered are valid, they are sent to a function that updates the product data.
                                services.update_inventory(dictionary_inventory,search_product,update_product, update_price, update_stock)

                case 4:
                    #We use a function to identify whether the product exists in inventory and obtain its location and details.
                    search_product = services.solicitude_string(f"Ingrese el nombre del articulo que desea buscar: ")
                    searched_dict = services.search_inventory(dictionary_inventory,search_product)  
                    if searched_dict != None:
                        print(f"{searched_dict}")
                case 5:
                    # We search to see if the product exists, then we delete all data for that product.
                    eliminate_product = services.solicitude_string(f"Ingrese el nombre del articulo que desea eliminar: ")
                    search_product= services.search_inventory(dictionary_inventory,eliminate_product)
                    
                    if search_product is not None:
                        services.delete_inventory(dictionary_inventory,eliminate_product)
                        continue
                        

                case 6:
                    #if the inventory has data, we calculate metrics and statistics
                    if not dictionary_inventory:
                        print("el inventario está vacío")
                    else:
                        metric_tuple = services.calculate_stadistics(dictionary_inventory)
                        print(f"unidades Totales: {metric_tuple[0]}")
                        print(f"Valor total del inventario: {metric_tuple[1]}")
                        print(f"El producto {metric_tuple[2]} posee el mayor precio con un total de:$ {metric_tuple[3]}")
                        print(f"El producto {metric_tuple[4]} posee la mayor cantidad con un total de: {metric_tuple[5]} unidades")
                case 7:

                    # Define the output path (save in the same directory as the script)
                    file_path = os.path.join(os.getcwd(), file_name_path)

                    # Call the function
                    files.guardar_csv(dictionary_inventory, file_name_path)
                case 8:
                    dictionary_returned = files.cargar_csv_sencillo(file_name_path)

                    if dictionary_returned:
                        while True:
                            try:
                                # We ask if you want to overwrite or merge the data.
                                load_option = services.solicitude_string("¿Desea sobrescribir el inventario actual? (S/N): ")
                                if load_option == "__CANCEL__":
                                    break

                                if load_option.lower() =="s":
                                    dictionary_inventory = dictionary_returned
                                    print("\nContenido de la lista de diccionarios cargados:")
                                    for item in dictionary_inventory:
                                        print(item)
                                    break
                                elif load_option.lower() == "n":
                                    for loaded in dictionary_returned:
                                        for actual in dictionary_inventory:
                                            if loaded["name_product"] == actual["name_product"]:
                                                actual["unitary_price"]= loaded["unitary_price"]
                                                actual["stock"]= actual["stock"]+loaded["stock"]
                                                print(f"Se actualizó el producto: |Nombre:{actual["name_product"]}|Precio:{actual["unitary_price"]}|cantidad:{actual["stock"]} ")
                                    break

                                else:
                                    print("Ingresó valor diferente de s y de n, intente de nuevo")
                            except KeyboardInterrupt:
                                print("\nSe canceló la operación")
                                break

                case 9:
                    option=0
        else:
            print("Ingresó valor fuera del rango, intente de nuevo")
            option = -1
    # we handle invalid value validations and keyboard interruptions
    except ValueError:
        print("Ingresó valor inválido, intente de nuevo")
    except KeyboardInterrupt:
        print("Se interrumpió el programa con control C ")
        option = 0
    