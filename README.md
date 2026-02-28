DESCUENTO_ROPA = 0.90
RECARGA = 1.15
EDAD_MINIMA = 18
CHEQUE_JOVEN = 5

def calcular_precio(precio, tipo): 

    if tipo == "ROBA": 
        return precio * DESCUENTO_ROPA # descompte del 10% 

    elif tipo == "ELECTRONICA": 
        return precio * RECARGA # recàrrec del 15% 

def descuento_edad(precio, edad):
    if edad < EDAD_MINIMA: 
        return precio - CHEQUE_JOVEN # xec jove de 5 euros

def calcular_precio_total(precio_base, tipo_producto, edad_cliente):

    precio_impuesto = calcular_precio(precio_base, tipo_producto)
    precio_total = descuento_edad(precio_impuesto, edad_cliente)

    precio_total=max (0, precio_total)

    print("El total es:")
    return precio_total
 
calcular_precio_total(100, "ROBA", 15) 
calcular_precio_total(200, "ELECTRONICA", 40) 
         

 
