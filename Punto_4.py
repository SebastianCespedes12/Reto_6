def Calculo_vueltas (P:int, M:int, H:int,B:int) ->int :
  Vueltas_final = B-(300*P+ 3300*M +350*H)
  return Vueltas_final

if __name__ == "__main__":
  P= int(input("Cantidad de panes: "))
  M= int(input("Cantidad de bolsas de leche: "))
  H= int(input("Cantidad de huevos: "))
  B= int(input("Billete de: "))
  Vueltas = Calculo_vueltas (P,M,H,B) 
  print(f"Me dan de vueltas o debo: {Vueltas}")