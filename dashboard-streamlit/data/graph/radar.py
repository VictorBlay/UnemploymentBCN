import matplotlib.pyplot as plt
import seaborn as sns
from data.get_data import anual_pop_gender, neighborhood, anual_pop, unemploy_gender, unemploy_neigh, unemploy_demand, meses

plt.figure(figsize=(15,18))
plt.hist([b["0-4"] for b in anual_pop_gender])

plt.pie([b for b in anual_pop_gender])
