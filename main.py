import numpy as np



def main():
	print("Hello from llm-ocm!")
	M = [1, 2, 3, 4]

	# Transformer en tableau NumPy
	M = np.array(M)

	# Afficher la matrice
	print(M.reshape(2, 2))


if __name__ == "__main__":
    main()
