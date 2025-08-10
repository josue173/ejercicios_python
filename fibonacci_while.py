nivel = 1

hasta = int(input('Nivel fibonacci: '))

while nivel <= hasta:
  if nivel <= 2:
      inicio = nivel - 1
      print(inicio)                     # Cuando nivel = 2
      valor_actual = inicio             # Actual = 1
      valor_anterior = valor_actual - 1 # Anterior = 0
  else:
    resultado = valor_actual + valor_anterior # Al inicio es 1 + 0
    print(resultado)
    valor_anterior = valor_actual
    valor_actual = resultado
  nivel += 1