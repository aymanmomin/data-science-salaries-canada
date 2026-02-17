"""
Personal Visualization: Data Scientist Salaries Across Canada (2025)
Data Source: Government of Canada Job Bank + Industry Reports
Created: January 2026
"""

from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np

# Data for Data Scientists in Canada by Province (2025)
# Based on Job Bank data, LinkedIn Salary Insights, and Glassdoor Canada
# NOC 21223: Database analysts and data administrators + NOC 21211: Data Scientists
# Data represents Low, Median, and High wages in CAD/hour

provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
province_names = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
                  'Newfoundland', 'Nova Scotia', 'Ontario', 'Prince Edward Island',
                  'Quebec', 'Saskatchewan']

# Wages in $/hour for Data Scientists
# Data Scientists typically earn 10-15% more than software engineers in tech hubs
low_wages = [38.00, 40.00, 24.00, 28.00,
             30.00, 30.00, 40.00, 26.00, 35.00, 32.00]
median_wages = [55.00, 68.00, 45.00, 48.00,
                45.00, 47.00, 62.00, 40.00, 52.00, 48.00]
high_wages = [110.00, 115.00, 75.00, 80.00,
              72.00, 85.00, 105.00, 70.00, 92.00, 80.00]

# Calculate annual salaries (assuming 40 hours/week, 52 weeks/year = 2080 hours)
annual_multiplier = 2080
low_annual = [w * annual_multiplier / 1000 for w in low_wages]  # in thousands
median_annual = [w * annual_multiplier / 1000 for w in median_wages]
high_annual = [w * annual_multiplier / 1000 for w in high_wages]

# Create figure with better styling
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
plt.style.use('seaborn-v0_8-darkgrid')

# ----- TOP CHART: Median Salaries Bar Chart -----
x_pos = np.arange(len(provinces))
colors = ['#E74C3C' if p == 'AB' else '#3498DB' if p == 'BC' else '#95A5A6'
          for p in provinces]

bars = ax1.bar(x_pos, median_annual, color=colors,
               alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, median_annual)):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'${val:.0f}k',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xlabel('Province', fontsize=12, fontweight='bold')
ax1.set_ylabel('Annual Salary ($1000s CAD)', fontsize=12, fontweight='bold')
ax1.set_title('Median Data Scientist Salaries Across Canada (2025)\n' +
              'BC Leads at $141k/year - High Demand for ML/AI Skills',
              fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(provinces, fontsize=11)
ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
ax1.set_ylim(0, max(median_annual) * 1.15)

# Add legend for highlighted provinces
legend_elements = [
    Patch(facecolor='#E74C3C', label='Alberta (Your Province!)'),
    Patch(facecolor='#3498DB', label='British Columbia (Highest)'),
    Patch(facecolor='#95A5A6', label='Other Provinces')
]
ax1.legend(handles=legend_elements, loc='upper right', fontsize=10)

# ----- BOTTOM CHART: Salary Range Comparison -----
x_pos2 = np.arange(len(provinces))
width = 0.6

# Create the range bars
for i in range(len(provinces)):
    # Highlight AB and BC
    if provinces[i] == 'AB':
        color = '#E74C3C'
        alpha = 0.9
    elif provinces[i] == 'BC':
        color = '#3498DB'
        alpha = 0.9
    else:
        color = '#95A5A6'
        alpha = 0.6

    # Draw line from low to high
    ax2.plot([x_pos2[i], x_pos2[i]], [low_annual[i], high_annual[i]],
             color=color, linewidth=8, alpha=alpha, solid_capstyle='round')

    # Add median marker
    ax2.scatter(x_pos2[i], median_annual[i], color=color, s=150,
                zorder=5, edgecolor='black', linewidth=2)

ax2.set_xlabel('Province', fontsize=12, fontweight='bold')
ax2.set_ylabel('Annual Salary Range ($1000s CAD)',
               fontsize=12, fontweight='bold')
ax2.set_title('Data Scientist Salary Ranges by Province\n' +
              'Complete Spectrum: Junior Analyst to Senior ML Engineer',
              fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(x_pos2)
ax2.set_xticklabels(provinces, fontsize=11)
ax2.grid(True, alpha=0.3, axis='y', linestyle='--')
ax2.set_ylim(0, max(high_annual) * 1.1)

# Add annotations for AB and BC
ab_idx = provinces.index('AB')
bc_idx = provinces.index('BC')
ax2.annotate(f'AB: Strong\nData Scene\n${median_annual[ab_idx]:.0f}k median',
             xy=(ab_idx, median_annual[ab_idx]), xytext=(
                 ab_idx+1.0, median_annual[ab_idx]-20),
             fontsize=9, color='#E74C3C', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2),
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#E74C3C'))

ax2.annotate(f'BC: Tech Hub\nHighest at ${median_annual[bc_idx]:.0f}k',
             xy=(bc_idx, median_annual[bc_idx]), xytext=(
                 bc_idx+0.8, median_annual[bc_idx]+25),
             fontsize=9, color='#3498DB', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#3498DB', lw=2),
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#3498DB'))

# Add data source
fig.text(0.99, 0.01, 'Data Source: Job Bank Canada, LinkedIn Salary Insights, Glassdoor (2025)\n' +
         'NOC 21211/21223: Data Scientists, Database Analysts | Accessed: January 2026',
         ha='right', fontsize=8, style='italic', color='gray')

plt.tight_layout()
plt.savefig('data_science_salaries_canada_2025.png',
            dpi=300, bbox_inches='tight')
print("✅ Visualization saved as 'data_science_salaries_canada_2025.png'")
plt.show()

# Print insights
print("\n" + "="*75)
print("KEY INSIGHTS FOR DATA SCIENCE CO-OP STUDENTS:")
print("="*75)
print(f"🏆 TOP 3 PROVINCES BY MEDIAN DATA SCIENCE SALARY:")
sorted_provinces = sorted(
    zip(province_names, median_annual), key=lambda x: x[1], reverse=True)
for i, (prov, sal) in enumerate(sorted_provinces[:3], 1):
    print(f"   {i}. {prov}: ${sal:.1f}k/year (${sal*1000/2080:.2f}/hour)")

print(f"\n📍 ALBERTA (Your Province):")
ab_idx = provinces.index('AB')
print(f"   • Median: ${median_annual[ab_idx]:.1f}k/year")
print(f"   • Range: ${low_annual[ab_idx]:.1f}k - ${high_annual[ab_idx]:.1f}k")
print(f"   • Strong ML/AI scene in Calgary & Edmonton!")

print(f"\n💰 DATA SCIENCE SALARY INSIGHTS:")
bc_idx = provinces.index('BC')
on_idx = provinces.index('ON')
print(
    f"   • BC offers highest median at ${median_annual[bc_idx]:.1f}k (Vancouver tech hub)")
print(
    f"   • Ontario follows at ${median_annual[on_idx]:.1f}k (Toronto AI corridor)")
print(
    f"   • Alberta competitive at ${median_annual[ab_idx]:.1f}k (energy + tech sectors)")
print(f"   • Even junior roles in AB/BC/ON: ~$80-85k/year")
print(f"   • Senior ML engineers can earn $200k+ in major tech hubs")

print(f"\n🎯 FOR DATA SCIENCE CO-OP PLANNING:")
print(f"   • Target: BC (highest), ON (AI hub), AB (local + competitive)")
print(f"   • Hot skills: Python, SQL, ML frameworks (TensorFlow/PyTorch)")
print(f"   • Industries: Tech, Finance, Energy (AB strength!), Healthcare")
print(f"   • Entry-level co-op: expect $25-40/hour ($52-83k annually)")

print(f"\n📊 VS SOFTWARE ENGINEERING:")
print(f"   • Data Scientists earn 10-20% more in tech hubs (specialized skills)")
print(f"   • Stronger demand in finance, healthcare, energy sectors")
print(f"   • More focus on statistics, ML, and business insights")
print("="*75)
