# Limpeza Clusters RAFTS3G

---
O algoritomo presente nesse repositório serve para obter as proteínas probióticas obtidas da clusterização feita pela ferramenta [RAFTS3G](https://sourceforge.net/projects/rafts-g/).

## Passo 1: Instalar as bibliotecas
  - As bibliotecas utilizadas estão presentes no arquivo **requirements.txt**.
    ```
    Instalação: pip -r requirements.txt
    ```

## Passo 2: Criar o arquivo multiFASTA
  - As pastas com os arquivos dos proteomas devem estar na mesma pasta dos algoritmos. O arquivo usado será o **juntar_fasta.py**. O arquivo criado será o `proteoma_bacterias.faa`. Quando o arquivo estiver pronto, adicionar manualmente ao final as sequências presentes no arquivo `proteoma_probioticos.faa`.

## Passo 3: Utilizar o RAFTS3G

## Passo 4: Obter os clusters
  -
