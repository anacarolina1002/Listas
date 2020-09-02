minhaLista = ["Eduardo","Julia","Ana",10]
print(minhaLista)

#Acesso ao item por posição
print("Acesso ao item por posição positiva:",(minhaLista[0]))

#Acesso indexado por posição(-1 é a última posição da tabela)
print("Acesso indexado negativo: ",(minhaLista[-1]))

#Intervalo de itens
print("Intervalo de itens sem o item de início:",(minhaLista[:2]))

#Intervalo de itens
print("Intervalo de itens sem o item final:",(minhaLista[1:]))

#Intervalo de itens indexados negativamente
print("Intervalo de itens sem o item de início:",(minhaLista[-3:-1]))

#Lista com valor do item alterado
minhaLista[3] = "Francine"
print("Lista com valor do item alterado: ",minhaLista)

for i in minhaLista:
    print("Item da lista:", i)
    