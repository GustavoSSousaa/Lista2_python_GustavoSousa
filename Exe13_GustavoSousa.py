#Escreva um programa que solicite um determinado de numeros de dias , em seguida exiba o quanto esse dias equivalem em horas , minutos e segundos
dias=int(input("Digite quantos dias foram :"))
hora = dias*24
minutos = hora*60
segundos = minutos*60
print (dias,"dia ",hora,"horas ",minutos,"minutos ",segundos,"segundos")