import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

# Literature values
literature_data = {
    'CH3OH': [0.41, 1.82, 2.61, 3.65, 4.3],
    'NH3': [0.24, 0.58, 0.75, 1.03, 1.48],
    'H2CO': [0.03, 0.06, 0.08, 0.14, 0.2],
    'C2H6': [0.11, 0.36, 0.65, 0.87, 1.41],
    'CH4': [0.21, 0.41, 0.78, 1.29, 2.1],
}

categories = list(literature_data.keys())
values = [literature_data[cat] for cat in categories]

# Observed mixing ratios (mean, error)
observed_data = {
    'CH3OH': (0.45, 0.03),
    'NH3': (0.6, 0.05),
    'H2CO': (0.26, 0.02),
    'C2H6': (0.208, 0.005),
    'CH4': (0.22, 0.03),
}
observed_colors = ['magenta', 'green', 'blue']

# color palette for boxplots
colors = sns.color_palette("hls", n_colors=len(categories))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Boxplot
sns.boxplot(data=values, ax=ax, width=0.2, showfliers=False, palette= colors, fill=True, linecolor= 'auto',linewidth=1)

# Plot observed mixing ratios with error bars
for i, (cat, (mean, err)) in enumerate(observed_data.items()):
    color = colors[i]
    ax.errorbar(i+0.2, mean, yerr=err, fmt='o', markersize=7, color=color, capsize=3, capthick=1, elinewidth=1, label=f'Observed ({cat})')

# formatting of plot
ax.set_yscale("log")
ax.set_ylim(0.01, 10)
ax.set_xlim(-0.5, len(categories)-0.5)
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.set_ylabel("Mixing ratios [%]", fontsize=15)
ax.set_xticklabels(categories, fontsize=12)
ax.tick_params(axis='x', pad=-20)
for i, cat in enumerate(categories):
    ax.axvline(i+0.5, color='black', linestyle= 'dashed', linewidth=0.5, alpha=0.5)

plt.show()