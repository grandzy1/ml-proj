import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(
	"creditcard.csv", delimiter=",", skiprows=1, quotechar='"', dtype=float
)

time = data[:, 0]
amount = data[:, -2]

fig, ax = plt.subplots(figsize=(10, 5))
fig.suptitle("Rozkład transakcji w czasie", fontsize=15, fontweight="bold")
ax.hist(time, bins=80, density=True)
ax.set_xlabel("Czas (s)")
plt.savefig("graphs/time_distribution.png", dpi=200)

fig, ax = plt.subplots(figsize=(5, 5))
fig.suptitle("Rozkład wartości", fontsize=15, fontweight="bold")
ax.hist(amount, bins=80, density=True)
ax.set_xlabel("Wartość ($)")
plt.savefig("graphs/value_distribution.png", dpi=200)

min_amount, max_amount = min(amount), max(amount)
print(f"Minimalna wartość transakcji: ${min_amount}")
print(f"Maksymalna wartość transakcji: ${max_amount}")
print(f"Średnia wartość transakcji: ${np.mean(amount):.2f}")
print(f"Mediana wartość transakcji: ${np.median(amount):.2f}")
