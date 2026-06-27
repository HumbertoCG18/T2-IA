
main.py recebe apenas o path do arquivo de teste como argumento\
ex: python .\src\main.py .\entradas\arquivoDeTeste1.txt

Dependendo do n número de duplas, pode ser necessário alterar os 
parâmetros do algoritmo

n <=15

    T = 100.0
    T_MIN = 1e-3          
    FATOR_RESFRIAMENTO = 0.9990
    ITERACOES_MAX = 200000
    LIMITE_ESTAGNACAO = 200000

n = 20
    
    T = 75.0
    T_MIN = 1e-3
    FATOR_RESFRIAMENTO = 0.9999
    ITERACOES_MAX = 500000
    LIMITE_ESTAGNACAO = 300000

h=20 encontrado 7 vezes em 10 testes

utilizando esses mesmos parâmetros, é possível encontrar
consistentemente h=75 para n=25 e h=90 para n=30


   