import os
import time
from Bio import SeqIO
from memoize import memoize


@memoize
def juntar_fasta():
    """Função responsável por juntar os proteomas em um único arquivo FASTA."""
    # --- Lista com as pastas que possuem os proteomas --- #
    lista_pastas = [
        'Bacteroides',
        'Bifidobacterium',
        'Lacticaseibacillus',
        'Lactiplantibacillus',
        'Lactobacillus',
        'Levilactobacillus',
        'Ligilactobacillus',
        'Limosilactobacillus',
        'Prevotella',
        'Ruminococcus'
        ]
    
    # --- Iterar sobre cada arquivo presente nas pastas e juntar todas as entradas em um arquivo FASTA ---#
    for pasta in lista_pastas:
        for arquivo in os.listdir(f'./{pasta}'):
            # Ler o arquivo
            for registro in SeqIO.parse(f'./{pasta}/{arquivo}', 'fasta'):
                # Obter o nome da proteína
                descricao = registro.description.split('[')
                
                # Obter o nome da bactéria
                bacteria = ' '.join(arquivo[:-4].split('_'))
                
                # Criar o novo cabeçalho 
                descricao_especie = f'{descricao[0]}[{bacteria}]'
                
                # Escrever o arquivo multifasta
                with open('proteoma_bacterias.faa', 'a') as faa:
                    fasta = f'''>{descricao_especie}
{registro.seq}
'''
                    faa.write(fasta)
    print('Arquivo criado!')


# --- Saber quanto tempo levou o processo --- #
ti = time.perf_counter()
juntar_fasta()
tf = time.perf_counter()
tempo_min = (tf - ti) / 60
print(f'Tempo de espera: {tf - ti:.2f} segundos ({tempo_min:.1f} minutos).')
