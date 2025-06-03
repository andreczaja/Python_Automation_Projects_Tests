import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # Carregue seu dataset
df = pd.read_csv('wine_quality_classification.csv')

# Selecione as colunas numéricas que você quer analisar
numeric_cols = ['fixed_acidity', 'residual_sugar', 'alcohol', 'density']

# Crie os scatter plots coloridos
sns.pairplot(df[numeric_cols + ['quality_label']], hue='quality_label')
plt.suptitle("Relação entre pares de variáveis numéricas, colorido por quality_label", y=1.02)
plt.show()