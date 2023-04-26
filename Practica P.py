
R1 = int(input("ingrese el valor del primer resistor : ")) # solo numeros enteros
R2 = int(input("ingrese el valor del segundo resistor : ")) # solo numeros enteros

RTS = R1+R2 # formula para calcular resistencias en serie
RTP = ((R1*R2)/(R1 + R2)) # formula para calcular resistencias en paralelo

print("La resistencia total si estan en serie es ", RTS)
print("La resistencia total si estan en paralelo es ", RTP)