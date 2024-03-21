# Reto 6

>## 1.Una función matemática para calcular el volumen y el área superficial

>Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
	
```python
from math import pi
def Calculo_volumen (r1:float, r2:float, h:float) ->float:
	Volumen = (4/3 * pi * r1**3)+((pi* r2**2* h)/3)
	return Volumen

def Calculo_area_superficial (r1, r2, h) ->float:
	Area = (4*pi*r1**2)+((pi*r2**2)+(pi*r2*((r2**2+h**2)**0.5)))
	return Area

if __name__ == "__main__":
	r1 =float(input("Radio de esfera: "))
	r2 =float(input("Radio de cono: "))
	h =float(input("Altura de cono: "))
	Volumen_figura = Calculo_volumen(r1,r2,h)
	Area_superficial = Calculo_area_superficial(r1,r2,h)
	print("El volumen es: " + str(Volumen_figura) + ", el area superficial es: " + str(Area_superficial))
```

>Revise como utilizar el valor de pi usando import math y math.pi

```python
import math
x =math.pi
print(x)
# 3.1415...
```
>## 2.Una función matemática para calcular el área y el perimetro. 

>Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b. 

```python
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
```

>Revise como utilizar el valor de pi usando import math y math.pi

```python
import math
x =math.pi
print(x)
# 3.1415...
```
>## 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def calculo_cantidad_de_carne (N:int, M:int, K:int)->int:
  return 6*N + 7*M + K
```
>## 4.Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

>## 5.Haga un programa que utilice una función para calcular el valor de un préstamo c usando interés compuesto del i por n meses.

```python
def Calculo_interes_compuesto (i:float, n:float, c:float) :
  Valor_futuro = c*(1+i/100)**n
  return Valor_futuro

if __name__ == "__main__":
  c = float(input("Valor del prestamo: "))
  i = float(input("Tasa de interes de: "))
  n = float(input("Cantidad de meses: "))
  Valor_final = Calculo_interes_compuesto (i,n,c)
  print("Valor final del prestamo es: "+str(Valor_final))
```

>## 6.El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def Calculo_cantidad_enfermos (D:int, C:int) ->int:
  cantidad_enfermos = (2*C)**D 
  return cantidad_enfermos

if __name__ == "__main__":
  D= int(input("Cantidad de dias que pasaron desde hoy: "))
  C= int(input("Numero actual de contagiados: "))
  cantidad_enfermos_actual = Calculo_cantidad_enfermos(D,C)
  print(f"Cuando pasen {D} dias van a haber: {cantidad_enfermos_actual} enfermos")
```

>## 7.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
>El promedio

```python
def Calculo_promedio (a:float,b:float,c:float,d:float,e:float) :
  return(a+b+c+d+e)/5
```

>La mediana

```python
def Calculo_mediana (a,b,c,d,e) :
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
        elif d<=c and d<=e :
            n3=d
        elif e<=c and e<=d :
            n3=e
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
        elif d<=b and d<=e :
            n3=d
        elif e<=b and e<=d :
            n3=e
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
        elif c<=b and c<=e :
            n3=c
        elif e<=b and e<=c :
            n3=e
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
        elif c<=b and c<=d :
            n3=c
        elif d<=b and d<=c :
            n3=d
  return n3
# Tambien con b,c,d,e (ver archivo adjunto: punto_7.py)
```

>El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

```python
def Calculo_promedio_multiplicativo(a,b,c,d,e):
  return ((a*b*c*d*e)**1/5)
```

>Ordenar los números de forma ascendente

```python
def Ordenar_numeros_ascendente (a,b,c,d,e):
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  return n1, n2, n3, n4, n5
# Tambien con b,c,d,e =n1 (ver archivo adjunto: punto_7.py)
```

>Ordenar los números de forma descendente

```python
def ordenar_numero_descendente (a,b,c,d,e):
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  return n5, n4, n3, n2, n1
# Tambien con b,c,d,e =n1 (ver archivo adjunto: punto_7.py)
```

>La potencia del mayor número elevado al menor número

```python
def calculo_potencia_mayor_numero_elevado_al_menor_número (a,b,c,d,e) :
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  return n5**n1
# Tambien con b,c,d,e =n1 (ver archivo adjunto: punto_7.py)
```

>La raíz cúbica del menor número

```python
def calculo_raíz_cúbica_del_menor_número (a,b,c,d,e) :
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  return n1**(1/3)
# Tambien con b,c,d,e =n1 (ver archivo adjunto: punto_7.py)
```

>## 8.Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
from Punto_7 import *
```

>## 9.Consultar qué es y cómo funciona pip en python.

>## 10.Consultar qué es y cómo funciona pip en python.
