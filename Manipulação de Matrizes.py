import numpy as np

matriz = np.random.randint(1, 51, (5, 5))

print("Matriz Original:")
print(matriz)

print(f"\nSoma total: {np.sum(matriz)}")
print(f"Média dos elementos: {np.mean(matriz)}")

matriz_filtrada = np.where(matriz > 30, 0, matriz)

print("\nMatriz modificada (Valores > 30 viraram 0):")
print(matriz_filtrada)

print("\nMatriz Transposta:")
print(matriz.T)