import matplotlib.pyplot as plt
import numpy as np

dataset = np.loadtxt("creditcard.csv", delimiter=",", dtype=object)

headers = dataset[0]
strip = lambda s: s.strip('"')
vfunc = np.vectorize(strip)
data = vfunc(dataset[1:]).astype(float)

X = data[:, :-1]
y = data[:, -1]

legal = y == 0
fraud = y == 1

fig, axes = plt.subplots(4, 7, figsize=(22, 12))
fig.suptitle("Rozkłady cech V1–V28", fontsize=15, fontweight="bold")
axes = axes.flatten()

for i in range(28):
	legal_transactions = X[legal, i + 1]
	fraud_transactions = X[fraud, i + 1]

	bins = np.linspace(
		min(legal_transactions.min(), fraud_transactions.min()),
		max(legal_transactions.max(), fraud_transactions.max()),
		40,
	)

	axes[i].hist(
		legal_transactions, bins=bins, color="b", alpha=0.5, density=True, label="legal"
	)
	axes[i].hist(
		fraud_transactions, bins=bins, color="r", alpha=0.5, density=True, label="fraud"
	)
	axes[i].set_title(f"V{i + 1}")
	axes[i].tick_params(axis="x", labelsize=7)
	axes[i].set_yticks([])

fig.legend(labels=["legal", "fraud"])
plt.tight_layout()
plt.savefig("graphs/feature_distribution.png")
