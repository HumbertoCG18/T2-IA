import sys
import json

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

def printTabelas():
    """Exibe as matrizes de preferências formatadas no terminal"""
    print("=== MATRIZ DE PREFERÊNCIAS: ESCOLA A ===")
    for idx, prefs in enumerate(prefEscolaA):
        print(f"Aluno A{idx + 1}: {prefs}")
        
    print("\n=== MATRIZ DE PREFERÊNCIAS: ESCOLA B ===")
    for idx, prefs in enumerate(prefEscolaB):
        print(f"Aluno B{idx + 1}: {prefs}")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        leituraArquivo(path)
        printTabelas() 
