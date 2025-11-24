import csv
import os # Necesario para obtener el directorio actual y manejar rutas

def guardar_csv(inventary, file_path, include_header=True):
    """
    Saves the list of dictionaries "inventory" in a CSV file.

    Args:
        inventory (list): List of dictionaries with keys "name_product", "unitary_price", "stock".
        path (str): Full path of the CSV file to save.
        include_header (bool): If True, includes the header "name_product,unitary_price,stock".
    
    """
    # Validate that the inventory is not empty
    if not inventary:
        print("El inventario está vacío. No se guardará el archivo CSV.")
        return

    # Define the expected header
    headers = ['name_product', 'unitary_price', 'stock']

    try:
        # Handle writing and permissions with try/except
        # Open the file in write mode (‘w’, newline=‘’ to avoid blank lines)
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            # Create the DictWriter object
            spamwriter = csv.DictWriter(csv_file, fieldnames=headers, delimiter=',')

            # Include the header if requested
            if include_header:
                spamwriter.writeheader()

            # Write down the inventory lines
            spamwriter.writerows(inventary)

        # Succesfull message
        print(f"Inventario guardado en: {file_path}")

    except PermissionError:
        print(f"Permiso inválido: No se pudo escribir en la ruta: {file_path}")
    except Exception as e:
        # Catch other possible I/O errors (e.g., invalid path)
        print(f"Error al guardar el archivo: {e}")




def cargar_csv_sencillo(path_file):
    """
      Easily load a CSV file into a list of dictionaries.
    The first row (header) is automatically used as dictionary keys.

    Args:
        path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries with the file's contents.
    """
    valid_products = []
    expected_headers = ['name_product', 'unitary_price', 'stock']
    value_error_counter= 0
    key_error_counter = 0
    
    
    try:
        # Open the file in read mode (‘r’)
        with open(path_file, mode='r', newline='', encoding='utf-8') as csv_file:
            # Use csv.DictReader
            # DictReader automatically takes the first row as field names (keys)
            lector_dict = csv.DictReader(csv_file, delimiter=',')

            if lector_dict.fieldnames != expected_headers:
                print(f"Error: Encabezado incorrecto. Los encabezados esperados son: {expected_headers}")
                return []
            
            # Process each row
            for line in lector_dict:
                try:
                    # Validation that keys exist (DictReader handles this if the CSV is correct)

                    name = (line.get('name_product') or '').strip()
                    price_str = (line.get('unitary_price') or '').strip()
                    stock_str = (line.get('stock') or '').strip()

                    # Check if any vital fields were left empty due to a missing column
                    if not stock_str or not price_str or not name:
                        # If a required value was empty, we count it as a missing column/data error.
                        # The conversion to int/float will do this, but we make it explicit for the counter:
                        if not stock_str:
                            raise KeyError("Falta el valor de stock (columna incompleta).")

                    # Conversion and Validation of Types/Positives
                    
                    # Name not empty
                    if not name:
                         raise ValueError("Nombre vacío.")

                    # Price (float y > 0)
                    price_float = float(price_str)
                    if price_float <= 0:
                        raise ValueError("Precio no positivo.")

                    # Stock (int and > 0)
                    stock_int = int(stock_str)
                    if stock_int <= 0:
                        raise ValueError("Cantidad no positiva.")
                        
                    # If everything is valid, add to the list
                    valid_products.append({
                        expected_headers[0] : name,
                        expected_headers[1]: price_float,
                        expected_headers[2]: stock_int
                    })

                except ValueError:
                    # If there is an error in conversion or validation, the row is skipped.
                    value_error_counter += 1
                    pass
                except KeyError:
                    # If any of the keys (name, price, stock) are missing from the row
                    key_error_counter +=1
                    pass
                    
        print(f"Archivo '{path_file}' cargado. Registros de productos válidos: {len(valid_products)}.")
        print(f"Cantidad de errores por valores no válidos: {value_error_counter}")
        print(f"Cantidad de errores por falta de valores por columna: {key_error_counter}")
        print(f"Cantidad de errores en total: {value_error_counter+key_error_counter}")
        return valid_products
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta: '{path_file}'")
        return []
    except UnicodeDecodeError:
        print(f"Error: Problema con la codificación del archivo. ¿Es UTF-8?")
        return []
    except Exception as e:
        print(f"Error inesperado durante la carga: {e}")
        return []
