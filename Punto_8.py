from Punto_7 import *
if __name__ == "__main__":
  a:float=float(input("Ingrese primer numero: "))
  b:float=float(input("Ingrese segundo numero: "))
  c:float=float(input("Ingrese tercer numero: "))
  d:float=float(input("Ingrese cuarto numero: "))
  e:float=float(input("Ingrese quinto numero: "))

Promedio = Calculo_promedio (a,b,c,d,e)
Mediana = Calculo_mediana (a,b,c,d,e)
Promedio_multiplicativo = Calculo_promedio_multiplicativo (a,b,c,d,e)
Forma_ascendente = Ordenar_numeros_ascendente (a,b,c,d,e)
Forma_descendente = ordenar_numero_descendente (a,b,c,d,e)
potencia_del_mayor_número_elevado_al_menor_número = calculo_potencia_mayor_numero_elevado_al_menor_número (a,b,c,d,e)
raiz_cubica_del_menor_numero = calculo_raíz_cúbica_del_menor_número (a,b,c,d,e)

print(Promedio) 
print(Mediana)
print(Promedio_multiplicativo)
print(Forma_ascendente)
print(Forma_descendente)
print(potencia_del_mayor_número_elevado_al_menor_número)
print(raiz_cubica_del_menor_numero)