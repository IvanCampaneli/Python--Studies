nome = 'Ivan Campaneli'
altura = 1.80 
peso = 118
imc = peso / (altura * altura)

#print('Nome:', nome)
#print('Altura:', altura)
#print('Peso:', peso)
#print('IMC:', imc)

#ou

#print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é:', imc)

#ou

#"f-strings" formatação string

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
