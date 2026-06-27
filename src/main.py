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


def h(solucao):
    custo_total = 0
    for i in range(total):
        aluno_A = i
        aluno_B = solucao[i]

        try:
            rank_A = prefEscolaA[aluno_A].index(aluno_B)
        except ValueError:
            rank_A = total

        try:
            rank_B = prefEscolaB[aluno_B].index(aluno_A)
        except ValueError:
            rank_B = total

        custo_total += (rank_A + rank_B)

    return custo_total


def executaSimulatedAnnealing(modo="final"):
    global solucaoAtual, solucaoVizinha

    T = 100.0
    T_MIN = 1e-3          # temperatura mínima, pq ele tava travando em 5e-324
    FATOR_RESFRIAMENTO = 0.9999
    ITERACOES_MAX = 200000
    LIMITE_ESTAGNACAO = 50000

    print(f"Simulated Annealing\nDimensão: {total}\n")
    inicializa()

    historico_h = []
    melhor_h = h(solucaoAtual)
    melhorSolucao = solucaoAtual.copy()
    iteracoes_sem_melhora = 0

    for t in range(1, ITERACOES_MAX + 1):
        valorSolucaoAtual = h(solucaoAtual)
        historico_h.append(valorSolucaoAtual)

        if valorSolucaoAtual < melhor_h:
            melhor_h = valorSolucaoAtual
            melhorSolucao = solucaoAtual.copy()
            iteracoes_sem_melhora = 0
        else:
            iteracoes_sem_melhora += 1

        if modo == "passo":
            print(f"Ciclo: {t} - Temperatura: {T:.6f} - Solução Atual - h={valorSolucaoAtual}")
        elif modo == "final" and t % 1000 == 0:
            print(f"Ciclo: {t} - h={valorSolucaoAtual} (melhor até agora: {melhor_h})")

        if valorSolucaoAtual == 0:
            if modo == "passo":
                print("Solução ótima encontrada (h=0).")
            break

        if iteracoes_sem_melhora >= LIMITE_ESTAGNACAO:
            if modo == "passo":
                print(f"\nSem melhora por {LIMITE_ESTAGNACAO} iterações. Encerrando.")
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
                if modo == "passo":
                    print("Aceitou uma solução pior...")
                solucaoAtual = solucaoVizinha.copy()

        T = max(T * FATOR_RESFRIAMENTO, T_MIN)

        if modo == "passo":
            input("Pressione Enter para continuar...")

    print(f"\nMelhor solução encontrada - h={melhor_h}")
    print(f"Solução codificada: {melhorSolucao}")
    print("Solução decodificada (par escola A -> escola B):")
    for i, par in enumerate(melhorSolucao):
        print(f"  Aluno A{i + 1} -- Aluno B{par + 1}")

    return historico_h


def perguntaModo():
    print("Escolha o modo de execução:")
    print("  1 - Passo a passo (pausa a cada iteração)")
    print("  2 - Final (executa direto e mostra só o resultado)")

    while True:
        escolha = input("Digite 1 ou 2: ").strip()
        if escolha == "1":
            return "passo"
        elif escolha == "2":
            return "final"
        else:
            print("Opção inválida. Digite 1 ou 2.")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        leituraArquivo(path)
        modo = perguntaModo()
        executaSimulatedAnnealing(modo)
    else:
        print("Uso: python main.py <arquivo_entrada>")
        sys.exit(1)
