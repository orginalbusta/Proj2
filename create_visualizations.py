import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

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

# Define developed vs developing countries (simplified)
developed = ['USA', 'DEU', 'GBR', 'FRA', 'JPN', 'CAN', 'AUS', 'ITA', 'ESP', 'NLD']
developing = ['CHN', 'IND', 'BRA', 'IDN', 'PAK', 'BGD', 'NGA', 'ETH', 'VNM', 'TUR']

# Create PDF
pdf_filename = 'checkpoint_visualizations.pdf'
with PdfPages(pdf_filename) as pdf:
    
    # PAGE 1: PROPOSITION - "Developed countries are leading the fight against climate change"
    fig = plt.figure(figsize=(11, 14))
    fig.suptitle('PROPOSITION: Developed Countries Are Leading the Fight Against Climate Change', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Visualization 1: Show declining trend for developed countries (2000-2020)
    ax1 = plt.subplot(2, 1, 1)
    developed_recent = df_co2[(df_co2['Code'].isin(developed)) & (df_co2['Year'] >= 2000)]
    developed_avg = developed_recent.groupby('Year')['CO2_per_capita'].mean().reset_index()
    
    ax1.plot(developed_avg['Year'], developed_avg['CO2_per_capita'], 
             linewidth=4, color='green', marker='o', markersize=8)
    ax1.set_title('Developed Countries CO2 Emissions Per Capita Show Significant Decline', 
                  fontsize=14, fontweight='bold', pad=20)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=12)
    ax1.fill_between(developed_avg['Year'], developed_avg['CO2_per_capita'], 
                     alpha=0.3, color='green')
    ax1.set_ylim(9, 13)  # Truncated y-axis to emphasize decline
    ax1.set_xticks(range(2000, 2021, 2))  # Whole numbers only, every 2 years
    ax1.grid(True, alpha=0.3)
    
    # Add annotation
    peak_val = developed_avg['CO2_per_capita'].max()
    recent_val = developed_avg['CO2_per_capita'].iloc[-1]
    reduction = ((peak_val - recent_val) / peak_val) * 100
    ax1.text(0.5, 0.05, f'{reduction:.1f}% Reduction in Emissions', 
             transform=ax1.transAxes, fontsize=14, 
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
             ha='center', fontweight='bold')
    
    # Visualization 2: Show individual developed countries' progress
    ax2 = plt.subplot(2, 1, 2)
    countries_sample = ['USA', 'DEU', 'GBR', 'FRA', 'JPN']
    for country_code in countries_sample:
        country_data = df_co2[(df_co2['Code'] == country_code) & (df_co2['Year'] >= 2000)]
        if len(country_data) > 0:
            country_data = country_data.sort_values('Year')  # Sort by year
            country_name = country_data['Country'].iloc[0]
            ax2.plot(country_data['Year'], country_data['CO2_per_capita'], 
                    linewidth=2.5, marker='o', label=country_name, alpha=0.8, markersize=4)
    
    ax2.set_title('Leading Nations Demonstrate Consistent Environmental Progress', 
                  fontsize=14, fontweight='bold', pad=20)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=12)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.set_xticks(range(2000, 2021, 2))  # Whole numbers only, every 2 years
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(5, 22)  # Focus on the decline
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()
    
    # PAGE 2: OPPOSING VIEW - "Developed countries are not doing enough"
    fig = plt.figure(figsize=(11, 14))
    fig.suptitle('OPPOSING VIEW: Developed Countries Are NOT Leading the Fight Against Climate Change', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Visualization 1: Compare absolute levels - developed vs developing
    ax1 = plt.subplot(2, 1, 1)
    
    # Get recent data (2015-2020)
    recent_year = 2018
    developed_recent = df_co2[(df_co2['Code'].isin(developed)) & 
                              (df_co2['Year'] == recent_year)]['CO2_per_capita'].mean()
    developing_recent = df_co2[(df_co2['Code'].isin(developing)) & 
                               (df_co2['Year'] == recent_year)]['CO2_per_capita'].mean()
    
    bars = ax1.bar(['Developed Countries', 'Developing Countries'], 
                   [developed_recent, developing_recent],
                   color=['darkred', 'lightblue'], width=0.6)
    
    ax1.set_title('Developed Countries STILL Emit 3X More CO2 Per Person Than Developing Nations', 
                  fontsize=14, fontweight='bold', pad=20, color='darkred')
    ax1.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=12)
    ax1.set_ylim(0, 13)  # Start from 0 to show true scale
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=16, fontweight='bold')
    
    ax1.text(0.5, 0.85, 'Despite decades of "progress", the inequality remains stark', 
             transform=ax1.transAxes, fontsize=12, ha='center',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # Visualization 2: Show historical emissions (full timeline)
    ax2 = plt.subplot(2, 1, 2)
    
    # Get full historical data
    developed_all = df_co2[df_co2['Code'].isin(developed)].groupby('Year')['CO2_per_capita'].mean()
    developing_all = df_co2[df_co2['Code'].isin(developing)].groupby('Year')['CO2_per_capita'].mean()
    
    ax2.fill_between(developed_all.index, 0, developed_all.values, 
                     alpha=0.6, color='red', label='Developed Countries')
    ax2.fill_between(developing_all.index, 0, developing_all.values, 
                     alpha=0.6, color='blue', label='Developing Countries')
    
    ax2.set_title('Historical Perspective: Developed Countries Have Been Major Polluters for Decades', 
                  fontsize=14, fontweight='bold', pad=20)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('CO2 Emissions (metric tons per capita)', fontsize=12)
    ax2.legend(loc='upper left', fontsize=11)
    ax2.set_ylim(0, 14)
    ax2.set_xticks(range(1960, 2021, 10))  # Whole numbers only, every 10 years
    ax2.grid(True, alpha=0.3)
    
    # Shade recent years
    ax2.axvspan(2000, 2020, alpha=0.1, color='gray')
    ax2.text(2010, 12, 'Even in "recent progress" era,\ngap remains huge', 
             fontsize=10, ha='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()
    
    # PAGE 3: WRITEUP
    fig = plt.figure(figsize=(11, 14))
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    # Title
    fig.text(0.5, 0.98, 'CHECKPOINT WRITEUP', fontsize=20, fontweight='bold', ha='center')
    
    # Proposition section
    fig.text(0.1, 0.94, 'Proposition:', fontsize=13, fontweight='bold')
    fig.text(0.1, 0.915, '"Developed countries are leading the fight against climate change through\n' +
             'significant reductions in CO2 emissions."', 
             fontsize=11, style='italic')
    
    # Focus section
    fig.text(0.1, 0.87, 'Visualization Focus:', fontsize=13, fontweight='bold')
    fig.text(0.1, 0.85, 'I am leaning towards creating the OPPOSING VIEW (Page 2) for the final project,\n' +
             'as it demonstrates more compelling use of persuasive/deceptive techniques.',
             fontsize=10)
    
    # Techniques section
    fig.text(0.1, 0.81, 'Design Decisions and Scores (-2=deceptive, +2=earnest):', fontsize=13, fontweight='bold')
    
    # Page 1 techniques
    fig.text(0.1, 0.775, 'Page 1 - Supporting the Proposition (Pro-Developed Countries):', 
             fontsize=11, fontweight='bold')
    
    techniques_p1 = [
        ('1.  Truncated Y-axis (Score: -1.5)', 
         '     Starting at 9 instead of 0 makes the decline appear more dramatic. This is moderately',
         '     deceptive as it exaggerates visual change, though the data itself remains accurate.'),
        ('2.  Selective time window (Score: -1.0)',
         '     Showing only 2000-2020 hides historical context. Somewhat deceptive but justified',
         '     as focusing on recent trends for "current progress" narrative.'),
        ('3.  Green color and positive language (Score: -0.5)',
         '     Creates positive emotional association. Mildly persuasive through color psychology',
         '     but commonly used in environmental "good news" contexts.'),
        ('4.  Percentage-based framing (Score: -1.0)',
         '     "20% reduction" sounds impressive without absolute context. Deceptive framing that',
         '     obscures that emissions remain high in absolute terms.')
    ]
    
    y_pos = 0.75
    for lines in techniques_p1:
        for line in lines:
            fig.text(0.12, y_pos, line, fontsize=8.5)
            y_pos -= 0.017
        y_pos -= 0.008
    
    # Page 2 techniques
    y_pos -= 0.01
    fig.text(0.1, y_pos, 'Page 2 - Opposing the Proposition (Critical of Developed Countries):', 
             fontsize=11, fontweight='bold')
    y_pos -= 0.025
    
    techniques_p2 = [
        ('1.  Full scale bar chart starting at 0 (Score: 1.5)',
         '     Shows true magnitude of difference between groups. Earnest approach that provides',
         '     accurate visual representation, though choice to highlight this metric is strategic.'),
        ('2.  Red/dark colors for developed countries (Score: -1.0)',
         '     Creates negative emotional response through color psychology. Moderately deceptive',
         '     manipulation of reader emotions, violating neutral color conventions.'),
        ('3.  Emphatic language: "STILL" and "3X MORE" (Score: -1.5)',
         '     Emphasizes ongoing inequality with charged language. Deceptive through emotional',
         '     framing, though the factual claims are accurate.'),
        ('4.  Historical timeline included (Score: 1.5)',
         '     Shows long-term pattern providing full context. Earnest decision that gives reader',
         '     complete picture rather than cherry-picked timeframe.')
    ]
    
    for lines in techniques_p2:
        for line in lines:
            fig.text(0.12, y_pos, line, fontsize=8.5)
            y_pos -= 0.017
        y_pos -= 0.008
    
    # Conclusion section
    y_pos -= 0.01
    fig.text(0.1, y_pos, 'Conclusion:', fontsize=13, fontweight='bold')
    y_pos -= 0.022
    
    fig.text(0.1, y_pos, 'Leaning towards: Page 2 (Opposing View)', 
             fontsize=10, fontweight='bold')
    y_pos -= 0.025
    
    conclusion_text = (
        'This set more effectively demonstrates the spectrum of persuasive techniques, from earnest\n'
        '(using full scale, showing historical data) to deceptive (selective color choices, emotionally\n'
        'charged language). The mix of positive and negative scores shows the nuanced boundary\n'
        'between acceptable persuasion and misleading visualization.'
    )
    
    fig.text(0.1, y_pos, conclusion_text, fontsize=9, verticalalignment='top')
    
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

print(f"\nPDF created successfully: {pdf_filename}")
print("\nSummary:")
print("- Page 1: Two visualizations supporting the proposition")
print("- Page 2: Two visualizations opposing the proposition")  
print("- Page 3: Writeup with proposition and design decision scores")

