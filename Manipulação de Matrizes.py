import numpy as np

def processar_dados_cientificos():
    matriz_a = np.random.randint(1, 10, (3, 3))
    matriz_b = np.eye(3) * 5  
    
    print("Matriz A:\n", matriz_a)
    print("\nMatriz B (Diagonal):\n", matriz_b)

    resultado_dot = np.dot(matriz_a, matriz_b)
    print("\nResultado da Multiplicação de Matrizes (A . B):")
    print(resultado_dot)

    min_val = matriz_a.min()
    max_val = matriz_a.max()
    matriz_normalizada = (matriz_a - min_val) / (max_val - min_val)
    
    print("\nMatriz A Normalizada (Valores entre 0 e 1):")
    print(np.round(matriz_normalizada, 2))

    np.save('resultado_processamento.npy', resultado_dot)
    print("\n[LOG]: Resultados exportados com sucesso.")

if __name__ == "__main__":
    processar_dados_cientificos()
    
 # Alteração para o Pull Request