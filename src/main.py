from pathlib import Path
import sys

diretorio_script = Path(__file__).parent
diretorio_raiz = diretorio_script.parent
diretorio_saidas = diretorio_raiz / "saidas"
diretorio_entradas = diretorio_raiz / "entradas"

if len(sys.argv) < 2:
    print("Uso: python main.py <nome_arquivo_entrada>")
    sys.exit(1)
nome_arquivo_entrada = sys.argv[1]
print(f"Processando arquivo de entrada: {nome_arquivo_entrada}")

def ler_arquivo(caminho):
    # Lê todas as linhas do arquivo
    with open(caminho, "r", encoding="utf-8") as f:
        linhas_brutas = f.readlines()

    # Limpa cada linha (remove quebras/espaços das pontas)
    # e descarta linhas vazias
    linhas = []
    for linha in linhas_brutas:
        linha_limpa = linha.strip()
        if linha_limpa != "":
            linhas.append(linha_limpa)

    # A PRIMEIRA linha é o número de duplas
    n = int(linhas[0])

    # Separa os dois blocos de alunos
    linhas_A = linhas[1 : 1 + n]          # n linhas logo após o cabeçalho
    linhas_B = linhas[1 + n : 1 + 2 * n]  # as n linhas seguintes

    # --- Escola A ---
    preferencias_A = []
    for linha in linhas_A:
        pedacos = linha.split()                # "2 3 4" -> ["2","3","4"]
        ids = pedacos[1:]                      # descarta o ID (primeiro)
        preferencias = [int(x) for x in ids]   # texto -> número inteiro
        preferencias_A.append(preferencias)

    # --- Escola B --- (mesma lógica)
    preferencias_B = []
    for linha in linhas_B:
        pedacos = linha.split()
        ids = pedacos[1:]
        preferencias = [int(x) for x in ids]
        preferencias_B.append(preferencias)

    return n, preferencias_A, preferencias_B

try:
    arquivo_entrada = diretorio_entradas / nome_arquivo_entrada
    n, preferencias_A, preferencias_B = ler_arquivo(arquivo_entrada)
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo_entrada}' não encontrado.")
    sys.exit(1)

# --- Conferência: confirme que a leitura funcionou ---
print(f"Número de duplas (n): {n}")
print(f"Preferências A: {preferencias_A}")
print(f"Preferências B: {preferencias_B}")