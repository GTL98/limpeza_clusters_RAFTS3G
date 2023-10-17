from Bio import SeqIO
from csv import reader


# --- Lista para armazenar qual cluster estão as proteínas probióticas --- #
lista_clusters = []

# --- Abrir o arquivo temporário com os cluster das proteínas probióticas --- #
with open('./arquivo_temp_proteinas.csv') as arquivo:
    leitor = reader(arquivo)
    for linha in leitor:
        lista_clusters.append(linha[0])
    lista_clusters.remove('cluster')

# --- Pasta de onde estão os clusters --- #
caminho = '../RAFTS3GClusters'

# --- Iterar sobre cada cluster que possui pelo menos 1 proteína probiótica --- #
lista_registros = []
lista_registros_temp = []
for cluster in lista_clusters:
    for registro in SeqIO.parse(f'{caminho}/Cluster_{cluster}.fasta', 'fasta'):
        cabecalho = registro.description.split('|')[1].split('.1')[1].strip()
        lista_registros_temp.append(cabecalho)
    lista_registros.append(lista_registros_temp[-1])

# --- Armazenar o cluster e a proteína probiótica --- #
dic = {cluster: proteina for cluster, proteina in zip(lista_clusters, lista_registros)}

# --- Escrever em um arquivo o cluster e a proteína probiótica --- #
with open('./clusters_probioticos.csv', 'a') as arquivo:
    for chave, valor in dic.items():
        arquivo.write(f'{chave},{valor}\n')
