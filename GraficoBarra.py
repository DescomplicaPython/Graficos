import matplotlib.pyplot as plt

# Gráfico de Barras
# Cria uma nova figura (janela) com um tamanho de 5x5 polegadas
plt.figure(figsize=(5, 5))
# Define as categorias (rótulos)
categories = ['Categoria 1', 'Categoria 2', 'Categoria 3']
values = [10, 15, 5]  # Valores dos gráfico
colors = ['#141F35', '#435657', '#EF5319']  # Define uma lista de cores
# Cria um gráfico de barras usando as categorias e valores definidos anteriormente
plt.bar(categories, values, color=colors)
plt.title("Gráfico de Barras")  # Define o título do gráfico
plt.xlabel("Categorias")  # Define o rótulo do eixo X
plt.ylabel("Valores")  # Define o rótulo do eixo Y
plt.show()  # Exibe o gráfico na janela criada