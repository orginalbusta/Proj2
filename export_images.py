import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
print("Loading data...")
df = pd.read_csv('climate-change.csv')

# Focus on CO2 emissions per capita
df_co2 = df[['Country Name', 'Country Code', 'Year', 
             'average_value_CO2 emissions (metric tons per capita)']].copy()
df_co2.columns = ['Country', 'Code', 'Year', 'CO2_per_capita']
df_co2 = df_co2.dropna()

# Define developed vs developing countries
developed = ['USA', 'DEU', 'GBR', 'FRA', 'JPN', 'CAN', 'AUS', 'ITA', 'ESP', 'NLD']
developing = ['CHN', 'IND', 'BRA', 'IDN', 'PAK', 'BGD', 'NGA', 'ETH', 'VNM', 'TUR']

# ===== SUPPORTING VISUALIZATIONS =====

# Viz 1a: Declining trend for developed countries
fig, ax = plt.subplots(figsize=(12, 7))
developed_recent = df_co2[(df_co2['Code'].isin(developed)) & (df_co2['Year'] >= 2000)]
developed_avg = developed_recent.groupby('Year')['CO2_per_capita'].mean().reset_index()

ax.plot(developed_avg['Year'], developed_avg['CO2_per_capita'], 
        linewidth=4, color='green', marker='o', markersize=8)
ax.set_title('Developed Countries CO2 Emissions Per Capita Show Significant Decline', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=14)
ax.fill_between(developed_avg['Year'], developed_avg['CO2_per_capita'], 
                alpha=0.3, color='green')
ax.set_ylim(9, 13)
ax.set_xticks(range(2000, 2021, 2))
ax.grid(True, alpha=0.3)

peak_val = developed_avg['CO2_per_capita'].max()
recent_val = developed_avg['CO2_per_capita'].iloc[-1]
reduction = ((peak_val - recent_val) / peak_val) * 100
ax.text(0.5, 0.05, f'{reduction:.1f}% Reduction in Emissions', 
        transform=ax.transAxes, fontsize=14, 
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
        ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('viz1_supporting.png', dpi=150, bbox_inches='tight')
print("Saved: viz1_supporting.png")
plt.close()

# Viz 2a: Individual countries progress
fig, ax = plt.subplots(figsize=(12, 7))
countries_sample = ['USA', 'DEU', 'GBR', 'FRA', 'JPN']
for country_code in countries_sample:
    country_data = df_co2[(df_co2['Code'] == country_code) & (df_co2['Year'] >= 2000)]
    if len(country_data) > 0:
        country_data = country_data.sort_values('Year')
        country_name = country_data['Country'].iloc[0]
        ax.plot(country_data['Year'], country_data['CO2_per_capita'], 
               linewidth=2.5, marker='o', label=country_name, alpha=0.8, markersize=4)

ax.set_title('Leading Nations Demonstrate Consistent Environmental Progress', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=14)
ax.legend(loc='upper right', fontsize=12)
ax.set_xticks(range(2000, 2021, 2))
ax.grid(True, alpha=0.3)
ax.set_ylim(5, 22)

plt.tight_layout()
plt.savefig('viz2_supporting.png', dpi=150, bbox_inches='tight')
print("Saved: viz2_supporting.png")
plt.close()

# ===== OPPOSING VISUALIZATIONS =====

# Viz 1b: Bar chart comparison
fig, ax = plt.subplots(figsize=(12, 7))
recent_year = 2018
developed_recent = df_co2[(df_co2['Code'].isin(developed)) & 
                          (df_co2['Year'] == recent_year)]['CO2_per_capita'].mean()
developing_recent = df_co2[(df_co2['Code'].isin(developing)) & 
                           (df_co2['Year'] == recent_year)]['CO2_per_capita'].mean()

bars = ax.bar(['Developed Countries', 'Developing Countries'], 
              [developed_recent, developing_recent],
              color=['darkred', 'lightblue'], width=0.6)

ax.set_title('Developed Countries STILL Emit 3X More CO2 Per Person Than Developing Nations', 
             fontsize=16, fontweight='bold', pad=20, color='darkred')
ax.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=14)
ax.set_ylim(0, 13)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.1f}',
           ha='center', va='bottom', fontsize=18, fontweight='bold')

ax.text(0.5, 0.85, 'Despite decades of "progress", the inequality remains stark', 
        transform=ax.transAxes, fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('viz1_opposing.png', dpi=150, bbox_inches='tight')
print("Saved: viz1_opposing.png")
plt.close()

# Viz 2b: Historical comparison
fig, ax = plt.subplots(figsize=(12, 7))
developed_all = df_co2[df_co2['Code'].isin(developed)].groupby('Year')['CO2_per_capita'].mean()
developing_all = df_co2[df_co2['Code'].isin(developing)].groupby('Year')['CO2_per_capita'].mean()

ax.fill_between(developed_all.index, 0, developed_all.values, 
                alpha=0.6, color='red', label='Developed Countries')
ax.fill_between(developing_all.index, 0, developing_all.values, 
                alpha=0.6, color='blue', label='Developing Countries')

ax.set_title('Historical Perspective: Developed Countries Have Been Major Polluters for Decades', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=14)
ax.legend(loc='upper left', fontsize=12)
ax.set_ylim(0, 14)
ax.set_xticks(range(1960, 2021, 10))
ax.grid(True, alpha=0.3)

ax.axvspan(2000, 2020, alpha=0.1, color='gray')
ax.text(2010, 12, 'Even in "recent progress" era,\ngap remains huge', 
        fontsize=11, ha='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('viz2_opposing.png', dpi=150, bbox_inches='tight')
print("Saved: viz2_opposing.png")
plt.close()

print("\nAll images exported successfully!")

