import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Dataset for Data Analytics.xlsx")

revenue_by_source = df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False)

revenue_in_thousands = revenue_by_source / 1000

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#1d3557' if i < 2 else '#4a4e69' for i in range(len(revenue_by_source))]

bars = ax.bar(revenue_in_thousands.index, revenue_in_thousands.values, color=colors, width=0.55)

ax.set_ylim(0, 320)

for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

ax.tick_params(axis='both', which='both', length=0, labelsize=11, colors='#333333')

ax.grid(axis='y', linestyle='--', alpha=0.3, color='#cccccc')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f"${height:.1f}K",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),  # Small vertical offset points
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1d3557')

plt.title("Instagram & Email Drive 42.5% of Revenue; Strategic Pivot Suggested for Lower Channels",
          fontsize=13, fontweight='bold', pad=20, loc='center', color='#1d3557')
ax.set_ylabel("Revenue (in Thousands of USD)", fontsize=11, color='#555555', labelpad=10)

plt.tight_layout()
plt.savefig('referral_source_revenue_clean.png', dpi=300)
print("Boardroom-ready chart saved as 'referral_source_revenue_clean.png'")