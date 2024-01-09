import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file from the local folder
df = pd.read_csv("terrorist-attacks.csv")

# Drop rows with missing values in the 'Code' column
df = df.dropna(subset=['Code'])

# Filter data for the year 2021
df_2021 = df[df['Year'] == 2021]

# Sorting the DataFrame by total production in descending order
sorted_countries = df_2021.sort_values(by='Terrorist attacks', ascending=False)

# Drop the first rows
sorted_countries = sorted_countries.iloc[1:]
# Select the top five countries
top_countries = sorted_countries.head(5)

# Plotting a bar chart for the top five countries
plt.figure(figsize=(12, 6))
bars = plt.bar(top_countries['Entity'], top_countries['Terrorist attacks'])

# Adding text labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 1),
             ha='center', va='bottom')

# Adding labels and title
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Number of Terrorist Attacks', fontweight='bold')

# Display the plot
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Save the plot as a PNG file
plt.savefig("22082816_1.png", dpi=300)

# Filtering original DataFrame to include only data for the top five countries
df_top_countries = df[df['Entity'].isin(top_countries['Entity'])]

# Creating a line chart for each country using Seaborn
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Terrorist attacks', hue='Entity',
             data=df_top_countries)

# Adding labels and title
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Terrorist attacks', fontweight='bold')

plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Show the legend outside the plot
plt.legend(title='Country', loc='upper left', frameon=False)

# Save the plot as a PNG file
plt.savefig("22082816_2.png", dpi=300)

# Melt the DataFrame to transform it into a format suitable for seaborn
melted_df = pd.melt(top_countries, id_vars=['Entity'], 
                    value_vars=['Death Age 100+',
       'Death Age: 51-99 ', 'Death Age : 21-50 ', 'Death Age : 11-20 ',
       'Death Age : 6-10 ', 'Death Age :  1-5'], var_name='Age Group',
        value_name='Number of Deaths')

# Create a bar plot using seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x='Entity', y='Number of Deaths', hue='Age Group',
            data=melted_df, palette='viridis')

# Adding labels and title
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Number of Deaths', fontweight='bold')

plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
# Save the plot as a PNG file
plt.savefig("22082816_3.png", dpi=300)

# Calculate the total number of deaths in all countries
total_deaths_all_countries = df['Terrorism deaths'].sum()

# Calculate the percentage of deaths for each of the top five countries
top_countries.loc[:, 'Percentage'] = (
    top_countries['Terrorism deaths'] / total_deaths_all_countries) * 100

# Create a pie chart
labels = top_countries['Entity']
sizes = top_countries['Percentage']
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 
          'lightpink']
explode = [0, 0.1, 0, 0.1, 0]
plt.figure(figsize=(14, 14))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
        explode=explode,textprops=dict(fontweight='bold',size=14))

# Save the plot as a PNG file
plt.savefig("22082816_4.png", dpi=300)

