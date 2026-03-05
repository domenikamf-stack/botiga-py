DESCUENTO_ROPA = 0.90
RECARGA = 1.15
EDAD_MINIMA = 18
CHEQUE_JOVEN = 5
# Usamos nombres especificos como 'DESCUENTO_ROPA', ya que, si el negocio 
# decide cambiar su descuento, se podra modificar solo la linea que tendra
# un cambio.

def calcular_precio(precio, tipo): 

    if tipo == "ROBA": 
        return precio * DESCUENTO_ROPA # descuento del 10% 

    elif tipo == "ELECTRONICA": 
        return precio * RECARGA # recarga del 15% 

def descuento_edad(precio, edad):
    if edad < EDAD_MINIMA: 
        return precio - CHEQUE_JOVEN # cheque joven de 5 euros
    
# Esta función busca que los clients que sean menores de 18  años puedan
# acceder a un descuento 

def calcular_precio_total(precio_base, tipo_producto, edad_cliente):

    precio_impuesto = calcular_precio(precio_base, tipo_producto)
    precio_total = descuento_edad(precio_impuesto, edad_cliente)

    precio_total=max (0, precio_total)

    print("El total es:")
    return precio_total

# La función obtener_precio_por_tipo la usamos para asegurar que los 
# cálculos de productos sean correctos y sin que afecten la edad."

calcular_precio_total(100, "ROBA", 15) 
calcular_precio_total(200, "ELECTRONICA", 40) 

