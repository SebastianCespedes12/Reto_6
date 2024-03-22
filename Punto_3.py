def calculo_cantidad_de_carne (N:int, M:int, K:int)->int:
  return 6*N + 7*M + K

if __name__ == "__main__":
  N = int(input("Cantidad de gallinas: "))
  M = int(input("Cantidad de gallos: "))
  K = int(input("Cantidad de pollitos: "))
  Carne_total = calculo_cantidad_de_carne(N,M,K)
  print(f"La cantidad de carne es: {Carne_total} kilos")

