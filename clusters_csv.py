import time
from Bio import SeqIO
from memoize import memoize


@memoize
def clusters_csv():
    """Função responsável por criar o arquivo temporário com os clusters e proteínas."""
    # --- Adicionar o cabeçalho ao arquivo --- #
    with open('arquivo_temp.csv', 'a') as csv:
        csv.write('cluster,proteina,bacteria,quantidade')

    # --- Pasta com os arquivos dos clusters --- #
    caminho = '../RAFTS3G/RAFTS3GClusters'

    # --- Ler o arquivo que contém os cluster e a quantidade de sequências --- #
    with open('./cluster.tab', 'r') as tab:
        conteudo = tab.readlines()
        for item in conteudo:
            item_split = item.split('\t')
            cluster = item_split[0].split(':')[1].strip()
            lista_proteinas = []
            lista_bacterias = []

            # Iterar sobre cada registro de cada arquivo cluster
            for registro in SeqIO.parse(f'{caminho}/Cluster_{cluster}.fasta', 'fasta'):
                # Limpar o cabeçalho para obter somente a proteína e a bactéria
                cabecalho = registro.description.split('|')[1].split('.')[1]
                cabecalho_temp = f'@{cabecalho}'
                cabecalho_temp = cabecalho_temp.replace('MULTISPECIES: ', '')
                cabecalho = cabecalho_temp.split('@1')[1].split('[')
                proteina = cabecalho[0].strip()
                lista_proteinas.append(proteina)
                bacteria = cabecalho[1][:-1]
                lista_bacterias.append(bacteria)

            # --- Criar dicionários para armazenar as proteínas, quantidade e as bactérias que possuem essas proteínas
            dic_proteina = {i: lista_proteinas.count(i) for i in lista_proteinas}
            dic_bacterias = {bacteria: proteina for bacteria, proteina in zip(lista_bacterias, lista_proteinas)}

            # --- Adicionar ao arquivo temporário o cluster, a proteína, a bactéria e a quantidade de sequências no cluster --- #
            with open('arquivo_temp.csv', 'a') as csv:
                for chave, valor in dic_bacterias.items():
                    csv.write(f'\n{cluster},{valor},{chave},{dic_proteina[valor]}')


# --- Saber quanto tempo levou o processo --- #
ti = time.perf_counter()
clusters_csv()
tf = time.perf_counter()
tempo_min = (tf - ti) / 60
print('Arquivo pronto!')
print(f'Tempo de espera: {tf - ti} ({tempo_min:.1f} minutos).')
