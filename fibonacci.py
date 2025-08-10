nivel = 1

hasta = int(input('Nivel fibonacci: '))

while nivel <= hasta:
  if nivel <= 2:
      inicio = nivel - 1
      print(inicio)
      valor_actual = inicio
      valor_anterior = valor_actual - 1
  else:
    resultado = valor_actual + valor_anterior
    print(resultado)
    valor_anterior = valor_actual
    valor_actual = resultado
  nivel += 1
  