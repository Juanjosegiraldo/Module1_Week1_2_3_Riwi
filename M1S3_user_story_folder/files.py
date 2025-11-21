import csv
import os # Necesario para obtener el directorio actual y manejar rutas

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda la lista de diccionarios 'inventario' en un archivo CSV.

    Args:
        inventario (list): Lista de diccionarios con claves 'nombre', 'precio', 'cantidad'.
        ruta (str): Ruta completa del archivo CSV a guardar.
        incluir_header (bool): Si es True, incluye el encabezado 'nombre,precio,cantidad'.
    """
    # 1. Validar que el inventario no esté vacío
    if not inventario:
        print("⚠️ Advertencia: El inventario está vacío. No se guardará el archivo CSV.")
        return

    # Definir el encabezado esperado
    campos = ['nombre', 'precio', 'cantidad']

    try:
        # 2. Manejar la escritura y permisos con try/except
        # Abre el archivo en modo escritura ('w', newline='' para evitar líneas en blanco)
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Crea el objeto DictWriter
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=',')

            # 3. Incluir el encabezado si se solicita
            if incluir_header:
                escritor.writeheader()

            # Escribe las filas del inventario
            escritor.writerows(inventario)

        # 4. Mensaje de éxito
        print(f"✅ Inventario guardado en: {ruta}")

    except PermissionError:
        print(f"❌ Error de Permiso: No se pudo escribir en la ruta '{ruta}'. Revise sus permisos.")
    except Exception as e:
        # Captura otros posibles errores de I/O (ej. ruta inválida)
        print(f"❌ Error al guardar el archivo: {e}")

# ---
# Ejemplo de uso (simulación en otro archivo o al final del módulo)
# ---

# Inventario de ejemplo (Lista de Diccionarios)
inventario_ejemplo = [
    {'nombre': 'Manzanas', 'precio': 1.5, 'cantidad': 50},
    {'nombre': 'Peras', 'precio': 2.0, 'cantidad': 30},
    {'nombre': 'Naranjas', 'precio': 1.2, 'cantidad': 80}
]

# Definir la ruta de salida (guarda en el mismo directorio del script)
ruta_archivo = os.path.join(os.getcwd(), 'inventario_salida.csv')

# Llamar a la función
guardar_csv(inventario_ejemplo, ruta_archivo)

# Ejemplo con inventario vacío para probar la validación
# guardar_csv([], os.path.join(os.getcwd(), 'inventario_vacio.csv'))









def cargar_csv(ruta, inventario_actual):
    """
    Carga un archivo CSV, valida sus filas y gestiona la fusión o reemplazo 
    con el inventario actual.

    Args:
        ruta (str): Ruta del archivo CSV a cargar.
        inventario_actual (list): La lista de diccionarios del inventario actual.

    Returns:
        tuple: (inventario_resultante, resumen_operacion)
    """
    productos_cargados = []
    filas_invalidas_contador = 0
    campos_esperados = ['nombre', 'precio', 'cantidad']

    try:
        # 1. Manejo de errores de Archivo
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.reader(archivo_csv, delimiter=',')

            # 2. Validar Encabezado
            try:
                header = next(lector)
            except StopIteration:
                print(f"❌ Error: El archivo '{ruta}' está vacío.")
                # Retorna el inventario actual sin cambios
                return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': 0}

            # Normalizar el encabezado para una validación estricta
            normalized_header = [h.strip().lower() for h in header]
            if normalized_header != campos_esperados:
                print(f"❌ Error de Encabezado: La primera fila no coincide con 'nombre,precio,cantidad'.")
                return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': 0}

            # 3. Procesar las Filas de Datos
            for i, fila in enumerate(lector):
                # Validar exactamente 3 columnas
                if len(fila) != 3:
                    filas_invalidas_contador += 1
                    continue
                
                nombre_str = fila[0].strip()
                precio_str = fila[1].strip()
                cantidad_str = fila[2].strip()

                try:
                    # Validar nombre no vacío
                    if not nombre_str:
                         raise ValueError("El nombre del producto no puede estar vacío.")

                    # Validar y convertir Precio (float, no negativo)
                    precio_float = float(precio_str)
                    if precio_float < 0:
                        raise ValueError("El precio no puede ser negativo.")

                    # Validar y convertir Cantidad (int, no negativo)
                    # Verifica que no contenga punto decimal para ser un entero estricto
                    if '.' in cantidad_str:
                         raise ValueError("La cantidad debe ser un número entero (sin decimales).")
                    cantidad_int = int(cantidad_str)
                    if cantidad_int < 0:
                        raise ValueError("La cantidad no puede ser negativa.")

                    # Si todo es válido, añadir a la lista de productos cargados
                    productos_cargados.append({
                        'nombre': nombre_str,
                        'precio': precio_float,
                        'cantidad': cantidad_int
                    })

                except ValueError:
                    # Error de conversión (float/int) o validación (negativo/vacío)
                    filas_invalidas_contador += 1
                except Exception:
                    # Otros errores inesperados en la fila
                    filas_invalidas_contador += 1
                    
    except FileNotFoundError:
        print(f"❌ Error: Archivo no encontrado en la ruta: '{ruta}'")
        return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': 0}
    except UnicodeDecodeError:
        print(f"❌ Error de Codificación: No se pudo leer el archivo. Asegúrese de que esté en UTF-8.")
        return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': 0}
    except Exception as e:
        print(f"❌ Error Genérico al cargar el archivo: {e}")
        return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': 0}

    # Si no se cargó nada, terminar la operación.
    if not productos_cargados:
        print(f"⚠️ El archivo se leyó, pero ninguna fila fue válida. {filas_invalidas_contador} filas inválidas omitidas.")
        return inventario_actual, {'action': 'Ninguna', 'loaded': 0, 'invalid': filas_invalidas_contador}

    # 4. Procesar Sobreescritura / Fusión (Preguntar al Usuario)
    print(f"\nSe encontraron {len(productos_cargados)} productos válidos para cargar.")
    while True:
        respuesta = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
        if respuesta in ('S', 'N'):
            break
        print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.")
        
    accion_realizada = ''
    inventario_resultante = []
    
    if respuesta == 'S':
        # Política S: Reemplazo Total
        inventario_resultante = productos_cargados
        accion_realizada = 'REEMPLAZO TOTAL'
    else:
        # Política N: Fusión por nombre
        accion_realizada = 'FUSIÓN (Actualiza Cantidad y Precio)'
        print("\n  **Política de Fusión**: Si un producto existe, se SUMARÁ la cantidad y se ACTUALIZARÁ el precio al nuevo valor.")
        
        # Convertir el inventario actual a un diccionario para búsqueda O(1)
        inventario_dict = {p['nombre']: p for p in inventario_actual}

        for producto_nuevo in productos_cargados:
            nombre = producto_nuevo['nombre']
            
            if nombre in inventario_dict:
                # Actualizar (Sumar Cantidad, Sobrescribir Precio)
                producto_existente = inventario_dict[nombre]
                producto_existente['cantidad'] += producto_nuevo['cantidad']
                producto_existente['precio'] = producto_nuevo['precio'] # Precio más reciente
            else:
                # Añadir nuevo producto
                inventario_dict[nombre] = producto_nuevo

        # Convertir el diccionario fusionado de vuelta a una lista
        inventario_resultante = list(inventario_dict.values())
        
    # 5. Retornar el resultado y el resumen
    resumen = {
        'action': accion_realizada,
        'loaded': len(productos_cargados),
        'invalid': filas_invalidas_contador
    }
    
    return inventario_resultante, resumen