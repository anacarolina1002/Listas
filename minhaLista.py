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

#Percorrer a lista
for i in minhaLista:
    print("Item da lista:", i)

#Condição positiva
print("Julia está na lista?")
if "Julia" in minhaLista:
    print("Sim, está!")
else:
    print("Não está!")

#Condição negativa
print("Gabriel está na lista?")
if "Gabriel" in minhaLista:
    print("Sim, está!")
else:
    print("Não está!")

#Verificar quantos itens tem na lista
print("Quantidade de itens na lista: ",len(minhaLista))

#Adiciona item ao final da lista
minhaLista.append("Henrique")
print("minha lista com um novo item no final: ",minhaLista)

#Adiciona item na posição escolhida
minhaLista.insert(2, "Madu")
print("minha lista com item em posição específica: ", minhaLista)

#Remover item específico
minhaLista.remove("Francine")
print("minha lista com item removido: ",minhaLista)

#Remove o índice especificado
minhaLista.pop(4)
print("minha lista com índice removido: ",minhaLista)

#Remove o útlimo índice da lista
minhaLista.pop()
print("minha lista com índice removido: ",minhaLista)

#Atua da mesma forma que o pop
del minhaLista[1]
print("Minha lista com item removido com o del: ", minhaLista)

#del pode apagar toda a lista.
minhaLista.clear()
print("Minha lista vazia com o método clear: ",minhaLista)

minhaLista.insert(0,"hello")
minhaLista.insert(1, "opa")
print("Minha lista com novos itens:", minhaLista)

minhaSegundaLista = minhaLista.copy()
print("Lista que copiou a primeira:", minhaSegundaLista)

minhaTerceiraLista = list(minhaSegundaLista)
print("Lista que copiou a segunda:", minhaTerceiraLista)

minhaSegundaLista.append("Aleatório")
minhaTerceiraLista.insert(0,"Hello")

print("Adicionando novos itens:",minhaSegundaLista)
print("Adicionando novos itens:",minhaTerceiraLista)

print("Quantidade de vezes que repete o hello: ",minhaTerceiraLista.count("Hello"))

#Juntando listas
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print("Juntando listas: ", minhaQuartaLista)

#Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ", minhaQuartaLista.index("hello"))