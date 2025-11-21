## Historia de usuario - Semana 3

import services

print("Bienvenido al inventario avanzado con colecciones y persistencia en archivos")
option = -1
dictionary_inventory = []

while option !=0:
    try:
        
        option = int(input("""\nIngrese 1 para agregar un producto en el inventario.
    \nIngrese 2 para mostrar los productos del inventario.
    \nIngrese 3 para actualizar un producto del inventario.
    \nIngrese 4 para buscar un producto del inventario.
    \nIngrese 5 para eliminar un producto del inventario.                  
    \nIngrese 6 para generar estadísticas como el precio total de cada producto, el precio total de todo el inventario
    \nIngrese 7 para guardar archivo
    \nIngrese 8 para guardar en archivo CSV    
    \nIngrese 9 para salir:\n"""))
        if option >=1 and option <=7:
            match option:
                case None:
                    option= 0
                case 1:
                    product = services.solicitude_string(f"Ingrese el nombre del articulo: ")
                    price = services.solicitude_float(f"Ingrese el precio unitario del articulo: ")
                    stock = services.solicitude_float(f"Ingrese la cantidad de artículos: ")
                    services.add_inventory(dictionary_inventory, product, price, stock)

                case 2:
                    services.show_inventory(dictionary_inventory) 

                case 3:

                    update_product = services.solicitude_string(f"Ingrese el nombre del articulo que desa actualizar: ")
                    search_product= services.search_inventory(dictionary_inventory,update_product) 

                    if search_product is not None:
                    
                        update_price = services.solicitude_float(f"Ingrese el precio unitario del articulo que desea actualizar: ")
                        update_stock = services.solicitude_float(f"Ingrese la cantidad del artículo que desea actualizar: ")  
                        services.update_inventory(dictionary_inventory,search_product,update_product, update_price, update_stock)

                case 4:
                    search_product = services.solicitude_string(f"Ingrese el nombre del articulo que desea buscar: ")
                    services.search_inventory(dictionary_inventory,search_product)  

                case 5:
                    eliminate_product = services.solicitude_string(f"Ingrese el nombre del articulo que desea eliminar: ")
                    search_product= services.search_inventory(dictionary_inventory,update_product)
                    
                    if search_product is not None:
                        services.delete_inventory(dictionary_inventory,eliminate_product)

                case 6:
                    metric_tuple = services.calculate_stadistics(dictionary_inventory)
                    print(f"unidades Totales: {metric_tuple[0]}")
                    print(f"Valor total del inventario: {metric_tuple[1]}")
                    print(f"El producto {metric_tuple[2]} posee el mayor precio con un total de:$ {metric_tuple[3]}")
                    print(f"El producto {metric_tuple[4]} posee el mayor precio con un total de: {metric_tuple[5]} unidades")
                case 7:
                    print("Guardar")
                case 8:
                    print("Cargar")
                case 9:
                    option=0



    except ValueError:
        print("Ingresó valor inválido")
    except KeyboardInterrupt:
        print("Se interrumpió el programa con control C ")
        option = 0
    