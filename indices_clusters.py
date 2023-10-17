from csv import reader


def indices_clusters(funcao_proteina: str):
    """Função responsável por obter os clusters e atribuir a sua respectiva função."""
    # --- Abrir o arquivo que contém os cluster e as proteínas probióticas --- #
    with open('./clusters_probioticos.csv', 'r') as arquivo:
        leitor = reader(arquivo)
        lista = []
        for linha in leitor:
            # Obter o cluster de cada proteína probiótica
            if funcao_proteina in linha[1]:
                lista.append(linha[0])

    # --- Obter a função de cada proteína --- #
    titulo = ''
    if funcao_proteina == 'carbono':
        titulo = 'Metabolismo do carbono e transporte de carboidratos'
    elif funcao_proteina == 'estresse':
        titulo = 'Resistência ao estresse'
    elif funcao_proteina == 'tolerancia':
        titulo = 'Tolerância ao suco gástrico'
    elif funcao_proteina == 'adesao':
        titulo = 'Capacidade de adesão'
    elif funcao_proteina == 'bacteriocina':
        titulo = 'Bacteriocinas'
    elif funcao_proteina == 'folico':
        titulo = 'Biossíntese do ácido fólico'
    elif funcao_proteina == 'EPS':
        titulo = 'Biossíntese do EPS'
    elif funcao_proteina == 'beta galactosidase':
        titulo = 'Beta galactosidase'
    elif funcao_proteina == 'manosidase':
        titulo = 'Manosidase'
    elif funcao_proteina == 'sialidase':
        titulo = 'Sialidase'
    elif funcao_proteina == 'fucosidase':
        titulo = 'Fucosidase'
    elif funcao_proteina == 'fosfolipase':
        titulo = 'Fosfolipase'
    elif funcao_proteina == 'biliar':
        titulo = 'Resistência ao ácido biliar'
    elif funcao_proteina == 'hypothetical':
        titulo = 'Proteínas hipotéticas'

    # --- Escrever em um arquivo TXT a quantidade de proteínas com a função, o cluster e qual a função --- #
    with open('./indices_clusters.txt', 'a') as txt:
        txt.write(f'{titulo}\n')
        txt.write('\tQuantidade:\n')
        txt.write(f'\t\t- {len(lista)}\n')
        txt.write('\tClusters:\n')
        for item in lista:
            txt.write(f'\t\t- {item}\n')
        txt.write('#####\n\n')


# --- Lista com as funções de cada proteína --- #
lista_proteinas = [
    'carbono',
    'estresse',
    'tolerancia',
    'adesao',
    'bacteriocina',
    'folico',
    'EPS',
    'beta galactosidase',
    'manosidase',
    'sialidase',
    'fucosidase',
    'fosfolipase',
    'biliar',
    'hypothetical'
]
for proteina in lista_proteinas:
    indices_clusters(proteina)
