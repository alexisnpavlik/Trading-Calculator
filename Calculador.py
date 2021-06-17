def tranding_futuros():
    pass


def trading_nomal():
    eleccion=input("""¿Que quieres calcular?
    
1- Ganancia entre dos precios 
2- Crecimiento del activo

3- Menu anterior

Elijo la numero: """)
    while True:
        if eleccion=="1":
            print("\nIngresa los valores")
            precio_compra=int(input("Cual es el precio de compra: "))
            precio_venta=int(input("Cual es el precio de venta: "))
            usdt=int(input("Cantidad de USDT invertidos: "))
            gancia=((usdt/precio_compra)*precio_venta)-usdt
            print(f"Tu ganancia aproximada es del {round((precio_venta-precio_compra)/precio_compra*100,2)}% o sea de {round(gancia,3)} USDT")
        elif eleccion =="2":
            print("Ingresa los valores")
            precio_inicial=float(input("Cual es el precio inicial: "))
            precio_final=float(input("Cual es el precio final: ")) 
            creciminto=round((precio_final-precio_inicial)/precio_inicial*100,2)
            print(f"El crecimiento del activo fue de: {creciminto} %")
        elif eleccion=="3":
            break
        else:
            print("Ingresa una opcion correcta")
            eleccion=input("""¿Que quieres calcular?
    
1- Ganancia entre dos precios 
2- Crecimiento del activo

3- Menu anterior

Elijo la numero: """)


def run():
    tipo_de_operacion=input("""¿Donde estas operando? Selecciona la opcion correcta

1- Trading Normal
2- Futuros

3- Finalizar ejecución

Elijo la numero: """)
    while True:
        if tipo_de_operacion=="1":
            print("Elegiste Trading Normal")
            trading_nomal()
        elif tipo_de_operacion=="2":
            print("Elegiste Futuros")
        elif tipo_de_operacion=="3":
            break
        else:
            print("Ingresa una opcion correcta")
            tipo_de_operacion=input("""¿Donde estas operando? Selecciona la opcion correcta

1- Trading Normal
2- Futuros

3- Finalizar ejecución

Elijo la numero: """)

if __name__=='__main__':
    run()