import matplotlib.pyplot as plt

# Gráfico de Pizza
plt.figure(figsize=(5, 5)) # Cria uma nova figura (janela) com um tamanho de 5x5 polegadas
labels = ['A', 'B', 'C', 'D'] # Define as categorias (rótulos)
sizes = [15, 30, 45, 10] # Tamanhos dos segmentos (em porcentagem)
# Cria o gráfico de pizza 
# 'autopct' é usado para formatar a porcentagem em cada segmento
# 'startangle' define o ângulo de início da primeira fatia
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Gráfico de Pizza") # Define o título do gráfico
plt.show() # Exibe o gráfico na janela criada