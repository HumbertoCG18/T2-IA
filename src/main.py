import sys
import random
import math

def leituraArquivo(path):
    global total, prefEscolaA, prefEscolaB
    
    with open(path, 'r') as f:
        linhas = f.readlines()
    
    primeiraLinha = linhas[0].split(']')[-1].strip()
    total = int(primeiraLinha)
    
    prefEscolaA = []
    prefEscolaB = []
    
    for i in range(1, total + 1):
        linhaLimpa = linhas[i].split(']')[-1].strip()
        partes = linhaLimpa.split()
        preferencias = [int(x) - 1 for x in partes[1:]]
        prefEscolaA.append(preferencias)
        
    for i in range(total + 1, (total * 2) + 1):
        linhaLimpa = linhas[i].split(']')[-1].strip()
        partes = linhaLimpa.split()
        preferencias = [int(x) - 1 for x in partes[1:]]
        prefEscolaB.append(preferencias)

    print(f"Arquivo lido. Total de duplas: {total}\n")

# posiciona aleatoriamente os alunos da escola B
def inicializa():
    global solucaoAtual, solucaoVizinha
    solucaoAtual = list(range(total))
    random.shuffle(solucaoAtual)
    solucaoVizinha = solucaoAtual.copy()

# faz o swap 
def geraSolucaoVizinha():
    global solucaoAtual, solucaoVizinha
    solucaoVizinha = solucaoAtual.copy()
    
    q1 = random.randint(0, total - 1)
    q2 = random.randint(0, total - 1)
    while q1 == q2:
        q2 = random.randint(0, total - 1)
        
    solucaoVizinha[q1], solucaoVizinha[q2] = solucaoVizinha[q2], solucaoVizinha[q1]

# heuristica de vdd ainda n implementada (função temporária para testes)
def h(solucao):
    return sum(abs(i - solucao[i]) for i in range(total))

def executaSimulatedAnnealing():
    global solucaoAtual, solucaoVizinha
    
    T = 1000000.0
    iteracoes = 200000
    
    print(f"Simulated Annealing\nDimensão: {total}\n")
    inicializa()
    
    for t in range(1, iteracoes + 1):
        valorSolucaoAtual = h(solucaoAtual)
        print(f"Ciclo: {t}- Temperatura: {T} - Solução Atual - h={valorSolucaoAtual}")
        
        if valorSolucaoAtual == 0:
            break
            
        geraSolucaoVizinha()
        valorSolucaoVizinha = h(solucaoVizinha)
        
        energia = valorSolucaoVizinha - valorSolucaoAtual
        if energia <= 0:
            solucaoAtual = solucaoVizinha.copy()
        else:
            probabilidade = math.exp(-energia / T)
            valor = random.random()
            if valor < probabilidade:
                print("Aceitou uma solução pior...")
                solucaoAtual = solucaoVizinha.copy()
                
        T = T * 0.6

    print(f"Solução Atual - h={h(solucaoAtual)}")
    print(solucaoAtual)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        leituraArquivo(path)
        executaSimulatedAnnealing()
