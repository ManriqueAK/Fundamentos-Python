productos = ["Cuadernos" , "Esferos" , "Lápices" , "Borradores" , "Sacapuntas" , "Marcadores"]
precios = [3500 , 1200, 900, 500 , 2000 , 3000]
cantidades = [45 , 120 , 200 , 150  , 50 , 20]
print(f"Productos: {productos}\nPrecios: {precios}\nCantidades: {cantidades}")
print(f"Inventario: {len(productos)} productos disponibles\n")

print(type(productos)) # Muestra el tipo de dato de la variable productos, osea que siempre devolverá "list"

print(type(productos[2])) # Muestra el tipo de dato del elemento de la lista productos indicado en el índice, y puede ser cualquier tipo de dato: string, int, flotat, bool, list, etc.
