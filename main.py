from lib import download_dataset
from lib import preencher_matriz_contratos
from lib import imprimir_matriz
from lib import exportar_csv

def main():
    
    # Download do dataset
    url = "https://drive.google.com/file/d/1YFPo-k9yyzitXp6HTfCfbselD1DUSJ4K/view?usp=drive_link"
    filename = 'dataset/entrada.txt'
    download_dataset(url,filename)

    # Preencher a matriz de contratos
    m, n, t, matriz = preencher_matriz_contratos(filename)
    
    # Imprimir os resultados
    print(m, n, t, "\n")
    imprimir_matriz(matriz)

    # Exportar a matriz de contratos
    file_csv = "dataset/contratos.csv"
    exportar_csv(matriz, file_csv)
    
if __name__ == "__main__":
    main()