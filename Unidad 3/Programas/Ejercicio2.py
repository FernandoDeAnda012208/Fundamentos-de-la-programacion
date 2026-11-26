total = float(input("Ingrese el total de la compra: "))

if total >= 1000:
    pagoConDescuento = total * 0.9
    print("Se otorgo un descuento del 10%")
    print("El pago con descuento es:", pagoConDescuento)
    print("Se descontaron:", total - pagoConDescuento)
else:
    print("No se otorgo ningun descuento")
    print("El pago sin descuento es:", total)