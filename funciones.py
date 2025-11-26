
from collections import Counter
#in this funtion we'll try to calculate how is the most important sell and what is the total amount of the all sales
def calcular(inventario):
    try:
        total_inventario = 0
        unidades_totales = 0
        for i in inventario:
            datos_para_conteo = {}
            for venta in inventario:
                datos_para_conteo[venta["producto"]] = datos_para_conteo.get(venta["producto"], 0) + venta["cantidad"]

            # Usamos Counter para obtener los 3 elementos más comunes (más vendidos)
            top_3_counter = Counter(datos_para_conteo).most_common(3)
            unidades_totales = unidades_totales + i['cantidad']
            precio_total = i['precio'] * i['cantidad']
            total_inventario = total_inventario + precio_total
            cantidad = len(inventario)
            producto_mas_caro = max(inventario, key=lambda producto: producto['precio'])
            mayor_stock = max(inventario, key=lambda producto: producto['cantidad'])
        print("\n🏆 Top 3 Usando collections.Counter:")
        print(top_3_counter)
        print(f"the total of products in cash is:", total_inventario)
        print(f"the most sell product is",mayor_stock)
    except IOError:
        print(f"❌ you should to write a correct value")
def mostrar(inventario):
    try:    
        for item in inventario:
           #titulo, autor,categoria,precio,cantidad
           print(f"title: {item['title']} | author: {item['author']} | category: {item['category']}  | price: {item['price']}  | amount: {item['amount']}")
    except IOError:
        print(f"❌ you should to write a correct value")

def agregar(titulo, autor,categoria,precio,cantidad):
    try:
        usuario = {}
        usuario['title'] = titulo
        usuario['author'] = autor
        usuario['category'] = categoria
        usuario['price'] = precio
        usuario['amount'] = cantidad
        
        return usuario
    except IOError:
        print(f"❌ you should to write a correct value")
#cliente, producto vendido,cantidad, fecha y descuento (si aplica)
def agregar1(cliente, producto,cantidad,fecha,precio):
    try:
        usuario = {}
        usuario['custumer'] = cliente
        usuario['title'] = producto
        usuario['amount'] = cantidad
        usuario['date'] = fecha
        usuario['price'] = precio
        
        return usuario
    except IOError:
        print(f"❌ you should to write a correct value")

def buscar(inventario,nombre_buscado):
    try:
        for producto in inventario:
            if producto["nombre"].lower() == nombre_buscado:
                print("\n✅ Product founded:")
                print(f"   Nombre: {producto['nombre']}")
                return producto
            else:
                print("product non-existent")
    except IOError:
        print(f"❌ you should to write a correct value")


def eliminar(inventario):
    try:
        nombre_a_eliminar = input("write the title that you want to remove")
        elemento_encontrado = None
        for producto in inventario:
            if producto["title"] == nombre_a_eliminar:
                elemento_encontrado = producto
                break
        if elemento_encontrado:
            inventario.remove(elemento_encontrado)
            print(f"✅ Dicionary wiht name '{nombre_a_eliminar}' removed.")
        else:
            print(f"❌ Dicionary wiht name '{nombre_a_eliminar}' did not find.")
    except IOError:
        print(f"❌ you should to write a correct value")

def actualizar(inventario):
    # 1. Solicitar el nombre del producto a actualizar
    nombre_a_buscar = input("Ingrese el nombre del titulo que desea actualizar: ")

    # Variable para rastrear si se encontró el producto
    producto_encontrado = False

    # 2. Iterar sobre la lista para encontrar el diccionario
    for item in inventario:
        # Comparamos el valor de 'nombre' del diccionario actual con la entrada del usuario
        if item['title'].lower() == nombre_a_buscar.lower(): 
            
            producto_encontrado = True
            
            print(f"\nProducto '{nombre_a_buscar}' encontrado. Ingrese los nuevos datos:")
            
            # 3. Solicitar los nuevos datos al usuario
            # Usamos float() e int() para asegurar que los datos sean numéricos
            try:
                titulo = input(f"el titulo actual es {item['title']}. Ingrese el nuevo titulo: ")
                autor = input(f"author actual es {item['author']}. Ingrese el nuevo autor: ")
                categoria = input(f"la categoria actual es {item['category']}. Ingrese el la nueva categoria: ")
                nuevo_precio = float(input(f"Precio actual es {item['price']}. Ingrese el nuevo precio: "))
                nueva_cantidad = int(input(f"cantidad actual es {item['amount']}. Ingrese el la nueva cantidad: "))
                
                item['title'] = titulo
                item['author'] = autor
                item['category'] = categoria
                item['price'] = nuevo_precio
                item['amount'] = nueva_cantidad
                
                print("\n✅ ¡Producto actualizado con éxito!")
                print(f"Nuevo registro: {item}")
                
            except ValueError:
                print("\n❌ Error: El stock debe ser un número entero y el precio un número decimal. No se pudo actualizar.")

            # Salir del bucle una vez que el producto ha sido encontrado y procesado
            break 

    # 5. Manejar el caso de que no se encuentre el producto
    if not producto_encontrado:
        print(f"\n⚠️ Advertencia: No se encontró ningún producto con el nombre '{nombre_a_buscar}'.")

    # 6. Mostrar la lista completa después de la operación
    print("\n--- Lista de diccionarios final ---")
    print(inventario)
