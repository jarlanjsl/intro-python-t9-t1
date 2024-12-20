import os, csv
from gdown import download
from typing import List, Tuple

# Definir a função download_from_drive
def download_dataset(url: str, filename: str)-> None:
    id_link = url.split('/')[5]
    link = f'https://drive.google.com/uc?id={id_link}'
    download(link, filename, quiet=False)
    return None

def preencher_matriz_contratos(filename: str) -> Tuple[int, int, float, List[List[List[float]]]]:
    with open(filename, 'r') as arquivo:
        # Ler todas as linhas
        arquivo01 = open(filename,'r')
        linhas = arquivo01.readlines()
      
        # Ler a primeira linha e armazenar as variáveis
        primeira_linha = arquivo.readline().strip().split()
        m = int(primeira_linha[0])
        n = int(primeira_linha[1])
        t = float(primeira_linha[2])

        # Ler linhas restantes
        linhas_restantes = linhas[1:]

    # Inicializar matriz de contratos
    matriz_contratos = [[[float('inf') for _ in range(m+1)] for _ in range(m+1)] for _ in range(n)]

    # Preencher a matriz com as linhas restantes
    for linha in linhas_restantes:
        # Separar os valores da linha, e atribuir tipagem
        profundidade, mes_inicio_linha, mes_final_coluna, valor = linha.split()
        profundidade = int(profundidade) - 1
        mes_inicio_linha = int(mes_inicio_linha)
        mes_final_coluna = int(mes_final_coluna)
        valor = float(valor)

        matriz_contratos[profundidade][mes_inicio_linha][mes_final_coluna] = valor

    return m, n, t, matriz_contratos  

def imprimir_matriz(matriz_contratos: List[List[List[float]]]) -> None:
    for linha in matriz_contratos:
        for elemento in linha:
            print(elemento)
        print()

def exportar_csv(dados: List[List], nome_arquivo: str) -> None:
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerows(dados)
    print(f"{nome_arquivo} exportado com sucesso!")