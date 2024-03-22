def Calculo_interes_compuesto (i:float, n:float, c:float) :
  Valor_futuro = c*(1+i/100)**n
  return Valor_futuro

if __name__ == "__main__":
  c = float(input("Valor del prestamo: "))
  i = float(input("Tasa de interes de: "))
  n = float(input("Cantidad de meses: "))
  Valor_final = Calculo_interes_compuesto (i,n,c)
  print("Valor final del prestamo es: "+str(Valor_final))