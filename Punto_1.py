import math
def Calculo_volumen (r1:float, r2:float, h:float) ->float:
  Volumen = (4/3 * math.pi * r1**3)+((math.pi* r2**2* h)/3)
  return Volumen

def Calculo_area_superficial (r1, r2, h) ->float:
  Area = (4*math.pi * r1**2)+((math.pi * r2**2)+(math.pi*r2* ((r2**2 + h**2) **0.5)))
  return Area

if __name__ == "__main__":
  r1 =float(input("Radio de esfera: "))
  r2 =float(input("Radio de cono: "))
  h =float(input("Altura de cono: "))
  Volumen_figura = Calculo_volumen(r1,r2,h)
  Area_superficial = Calculo_area_superficial(r1,r2,h)
  print("El volumen es: " + str(Volumen_figura) + ", el area superficial es: " + str(Area_superficial))

