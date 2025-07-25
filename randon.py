#exercicio 1

#print(len(input("Digite seu nome: ")))


#exercicio 2 soma de valores
#print ("ano que você nasceu + sua idade")
#print(int(input("Sua idade: ")) + int(input("ano de nascimento: ")))

#multiplicar calorias queimadas e dias de exercicio na semana
#print("calorias queimadas na semana")
#dias_de_treino = int(input("quantos dias você treina na semana?"))
#total_horas = float(input("quantas horas?"))
#total_horas = dias_de_treino * total_horas
#print(f"você treina {total_horas} horas por semana")

#calorias
print("calorias gastas na semana total")
dias_de_treino = int(input("quantos dias você treina na semana?"))
horas_exercicio = float(input("quantos minutos por dia?"))
total_horas = dias_de_treino * horas_exercicio
caloria_por_hora = 8
caloria_basal = 12000
calorias_treino = total_horas * caloria_por_hora
caloria_total_semana = calorias_treino + caloria_basal  
print(f"gasta {caloria_total_semana} calorias por semana")