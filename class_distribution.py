import matplotlib.pyplot as plt
import numpy as np

dataset = np.loadtxt("creditcard.csv", delimiter=",", dtype=object)

headers = dataset[0]
data = dataset[1:]

classes = ["legal", "fraud"]
y = data[:, -1]
unique_y, counts = np.unique(y, return_counts=True)
strip = lambda s: s.strip('"')
vfunc = np.vectorize(strip)
unique_y = vfunc(unique_y)

fig, ax = plt.subplots(1, 2)
fig.suptitle("Rozkład klas", fontsize=15, fontweight="bold")

percentage = counts / counts.sum() * 100
bars = ax[0].bar(x=classes, height=counts, color=["b", "r"], label=classes)
ax[0].bar_label(bars)
ax[0].set_title("Liczba transakcji (skala logarytmiczna)")
ax[0].set_ylabel("Liczba próbek")
ax[0].set_yscale("log")
ax[1].pie(
	x=percentage,
	labels=[f"{x:.2f}%" for x in percentage],
	colors=["b", "r"],
	explode=(0, 0.1),
)
fig.legend(labels=classes)
plt.tight_layout()
plt.savefig("graphs/class_distribution.png", dpi=200)
