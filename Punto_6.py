def Calculo_cantidad_enfermos (D:int, C:int) ->int:
  cantidad_enfermos = (2*C)**D 
  return cantidad_enfermos

if __name__ == "__main__":
  D= int(input("Cantidad de dias que pasaron desde hoy: "))
  C= int(input("Numero actual de contagiados: "))
  cantidad_enfermos_actual = Calculo_cantidad_enfermos(D,C)
  print(f"Cuando pasen {D} dias van a haber: {cantidad_enfermos_actual} enfermos")
