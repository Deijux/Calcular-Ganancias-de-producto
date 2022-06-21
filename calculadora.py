import time

def intro():
    print("-------------------- Calcular ganancias ventas ---------------------")
    print("---------------------------- Bienvenido ----------------------------")
    print("-------- Asegure de usar el punto para especificar los miles -------")

intro()

def operacion():
    pre_ven = float(input("¿Cual es el precio del producto en venta? : "))
    pre_pro = float(input("¿Cual es el precio del producto por el proveedor? : "))
    ven_mes = int(input("¿Cuantos producos del mismo se vendió? : "))
    
    rest = (pre_ven)-(pre_pro)
    marg_gan = (rest)*(ven_mes)
    print("Su margen de ganancia de los " +str(ven_mes) + " productos es: {:.3f}".format(marg_gan))
    
    time.sleep(5)
    
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    
    decs = input("¿Quieres hacer otro calculo? (si, no): ")
    if decs == "si":
        return operacion()
    elif decs == "no":
        print("Gracias por utilizarme, ten un buen día :D")
        time.sleep(5)

operacion()
