import numpy as np
from scipy import stats

# Dados
x = np.array([400, 450, 550, 600, 700, 750])
y = np.array([4000, 5000, 5400, 5900, 6400, 7000])

# Regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Imprimir os resultados
print("Coeficiente angular (slope):", slope)
print("Coeficiente linear (intercept):", intercept)
print("Coeficiente de determinação (R-squared):", r_value**2)
print("P-valor:", p_value)
