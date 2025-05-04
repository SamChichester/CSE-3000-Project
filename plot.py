import matplotlib.pyplot as plt

charts = [
    (70, 30),
    (94, 6),
    (68, 32)
]

labels = ['Male', 'Female']
colors = ['skyblue', 'orange']

fig, axs = plt.subplots(1, 3, figsize=(12, 4))

for i, (val1, val2) in enumerate(charts):
    axs[i].bar(labels, [val1, val2], color=colors)
    axs[i].set_ylim(0, 100)
    axs[i].set_ylabel('Percentage')

axs[0].set_title(f'DALL-E')
axs[1].set_title(f'Firefly')
axs[2].set_title(f'Gemini')

plt.tight_layout()
plt.show()
