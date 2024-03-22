from math import pi
def Calculo_area (r:float, a:float, b:float)->float :
  Area = (a*b)+(2*(pi*r**2))
  return Area 

def Calculo_perimetro (r,a,b) ->float :
  Perimetro = (2*(a+b))+(2*(2*pi*r))
  return Perimetro

if __name__ == "__main__":
  r =float(input("Radio de circulos: "))
  a =float(input("Altura del rectangulo: "))
  b =float(input("Largo del rectangulo: "))
  Area_total = Calculo_area(r,a,b)
  Perimetro_total = Calculo_perimetro(r,a,b)
  print("El Perimetro es: "+ str(Perimetro_total)+ ", El area es: " + str(Area_total))