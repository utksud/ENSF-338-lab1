import json
import matplotlib.pyplot as plt
import numpy as np

with open('internetdata.json', 'r') as f:
    data = json.load(f)

low_income_countries = []
high_income_countries = []

for country in data:
    income = country.get('incomeperperson')
    internet_rate = country.get('internetuserate')

    if income is not None and internet_rate is not None:
        if income < 10000:
            low_income_countries.append(internet_rate)
        else:
            high_income_countries.append(internet_rate)

print(f"Number of low-income countries (income < $10,000): {len(low_income_countries)}")
print(f"Number of high-income countries (income >= $10,000): {len(high_income_countries)}")

mean_low = np.mean(low_income_countries)
median_low = np.median(low_income_countries)
std_low = np.std(low_income_countries)
min_low = np.min(low_income_countries)
max_low = np.max(low_income_countries)

mean_high = np.mean(high_income_countries)
median_high = np.median(high_income_countries)
std_high = np.std(high_income_countries)
min_high = np.min(high_income_countries)
max_high = np.max(high_income_countries)

plt.figure(figsize=(10, 6))
plt.hist(low_income_countries, bins=15, color='skyblue',
         edgecolor='black', alpha=0.8)
plt.title('Internet Usage Distribution\nLow-Income Countries (Income < $10,000)',
          fontsize=14, fontweight='bold')
plt.xlabel('Internet Usage Rate (%)', fontsize=12)
plt.ylabel('Number of Countries', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.xlim(0, 100)

stats_text = (
    f"Count: {len(low_income_countries)}\n"
    f"Mean: {mean_low:.1f}%\n"
    f"Median: {median_low:.1f}%\n"
    f"Std Dev: {std_low:.1f}%\n"
    f"Min: {min_low:.1f}%\n"
    f"Max: {max_low:.1f}%"
)

plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes,
         fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('hist1.png', dpi=300, bbox_inches='tight')
print("Saved: hist1.png (low-income countries)")
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(high_income_countries, bins=15, color='lightcoral',
         edgecolor='black', alpha=0.8)
plt.title('Internet Usage Distribution\nHigh-Income Countries (Income >= $10,000)',
          fontsize=14, fontweight='bold')
plt.xlabel('Internet Usage Rate (%)', fontsize=12)
plt.ylabel('Number of Countries', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.xlim(0, 100)

stats_text = (
    f"Count: {len(high_income_countries)}\n"
    f"Mean: {mean_high:.1f}%\n"
    f"Median: {median_high:.1f}%\n"
    f"Std Dev: {std_high:.1f}%\n"
    f"Min: {min_high:.1f}%\n"
    f"Max: {max_high:.1f}%"
)

plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes,
         fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('hist2.png', dpi=300, bbox_inches='tight')
print("Saved: hist2.png (high-income countries)")
plt.show()

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)
print("Low-income countries (income < $10,000):")
print(f"  Number of countries: {len(low_income_countries)}")
print(f"  Average internet usage: {mean_low:.2f}%")
print(f"  Median internet usage: {median_low:.2f}%")
print(f"  Standard deviation: {std_low:.2f}%")
print(f"  Range: {min_low:.2f}% to {max_low:.2f}%")
print()
print("High-income countries (income >= $10,000):")
print(f"  Number of countries: {len(high_income_countries)}")
print(f"  Average internet usage: {mean_high:.2f}%")
print(f"  Median internet usage: {median_high:.2f}%")
print(f"  Standard deviation: {std_high:.2f}%")
print(f"  Range: {min_high:.2f}% to {max_high:.2f}%")
print()
print(f"Difference in means: {mean_high - mean_low:.2f}%")
print(f"Mean internet usage is {((mean_high - mean_low)/mean_low)*100:.1f}% higher in high-income countries")
print("=" * 60)
