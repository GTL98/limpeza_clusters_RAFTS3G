import time
from Bio import SeqIO
from memoize import memoize


@memoize
def encontrar_cluster():
    """Função responsável por encontrar os cluster onde há pelo menos 1 proteína probiótica."""
    # --- Lista para armazenar as proteínas probióticas --- #
    lista_proteina_bacteria = []
    
    # --- Ler o arquivo FASTA --- #
    for registro in SeqIO.parse('./proteoma_probioticos.faa', 'fasta'):
        # Obter o nome da proteína
        cabecalho = registro.description.split('.1')[1].split('[')

        # Obter a proteína
        proteina = cabecalho[0].strip()

        # Obter a bactéria
        bacteria = cabecalho[1][:-1].strip()

        # Colocar na lista a proteína e a bactéria separadas por vírgula
        lista_proteina_bacteria.append(f'{proteina},{bacteria}')

    # --- Adicionar em uma lista o conteúdo do arquivo temporário dos clusters --- #
    with open('./arquivo_temp.csv', 'r') as csv:
        conteudo = csv.readlines()
        lista_csv = []
        for linha in conteudo:
            lista_csv.append(linha)

    # --- Verificar em quais cluster estão as proteínas probióticas --- #
    lista_temp = []
    for linha_csv in lista_csv:
        for proteina_bacteria in lista_proteina_bacteria:
            if proteina_bacteria in linha_csv:
                lista_temp.append(linha_csv)

    # --- Criar um arquivo temporário com os clusters das proteínas probióticas --- #
    with open('./arquivo_temp_proteinas.csv', 'a') as csv:
        csv.write('cluster,proteina,bacteria,quantidade\n')
        for item in lista_temp:
            csv.write(f'{item}')


# --- Saber quanto tempo levou o processo --- #
ti = time.perf_counter()
encontrar_cluster()
tf = time.perf_counter()
tempo_min = (tf - ti) / 60
print(f'Tempo de espera: {tf - ti:.2f} segundos ({tempo_min:.1f} minutos).')
