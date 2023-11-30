import os

# --- Obter o primeiro documento que contém os clusters e a quantidade de sequências --- #
# --- (colocar "00_" no começo do nome do documento) --- #
caminho = ''
for arquivo in os.listdir(caminho):
    report = arquivo
    break

# --- Abrir o arquivo --- #
with open(f'{caminho}/{report}', 'r') as tab:
    conteudo = tab.readlines()
    for item in conteudo:
        # O arquivo é separado por tabulação (\t)
        cluster = item.split('\t')
        # Pular a primeira linha
        if 'Cluster' in item:
            pass
        else:
            # Obter os cluster que possuem mais de 2 sequências
            quantidade = int(cluster[1].split('\n')[0])
            if quantidade >= 2:
                with open('cluster.tab', 'a') as tab2:
                    tab2.write(f'Cluster: {cluster[0]}\tQuantidade: {quantidade}\n')
