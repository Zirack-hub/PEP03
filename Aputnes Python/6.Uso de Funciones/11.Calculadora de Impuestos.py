def calcular_total_pago(pago_sin_impuesto, impuesto):
        return (pago_sin_impuesto + (pago_sin_impuesto * impuesto) / 100)

pago_sin_impuesto = float(input('Proporciona el pago sin impuestos: '))
impuesto = float(input('Proporciona el porcentaje de impuestos: '))
resultado = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {resultado}')