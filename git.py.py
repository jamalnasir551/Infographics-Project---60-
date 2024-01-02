import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def pie_plot(file):
    # Load the data from the CSV file
    df4 = pd.read_csv(file)

    # Select a specific year for the pie chart (e.g., 2020)
    year_to_visualize = 2020

    # Filter the DataFrame for the selected year
    data_for_pie = df4[df4['Year'] == year_to_visualize]

    # Sum the production values for each energy source
    sums = data_for_pie.iloc[:, 2:].sum()

    # Set font size for labels
    font_size = 16

    # Create a pie plot
    plt.figure(figsize=(12, 12))
    plt.pie(sums, labels=sums.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors, textprops={'fontsize': font_size})
    plt.title(f'Electricity Production Distribution in {year_to_visualize} by Source', fontsize=font_size + 2)
    plt.show()

def line_plot(file):
    df4 = pd.read_csv(file)
    df4['Total Electricity Production'] = df4['Other Renewables'] + df4['Hydroelectric'] + df4['Oil'] + df4['Gas'] + df4['Coal']
    result_df = df4
    result_df['Hydro'] = df4['Hydroelectric']
    result_df['Gas'] = df4['Gas']
    result_df['Other Renewables'] = df4['Other Renewables']
    result_df['Oil'] = df4['Oil']
    result_df['Coal'] = df4['Coal']

    # Set font size for axis labels and title
    font_size = 16

    plt.figure(figsize=(16, 8))
    sns.lineplot(data=result_df, x='Year', y='Total Electricity Production', hue='Entity')
    plt.title('Electricity Production Trend Over Year', fontsize=font_size + 2)
    plt.xlabel('Year', fontsize=font_size)
    plt.ylabel('Total Electricity Production', fontsize=font_size)
    plt.show()
def area_plot(file):
    df4 = pd.read_csv(file)
    columns_to_plot = ['Coal', 'Gas', 'Oil', 'Hydroelectric']

    # Filter the dataset for the years 2000-2020
    df_subset = df4[(df4['Year'] >= 2000) & (df4['Year'] <= 2020)]

    # Calculate cumulative percentage for each source
    cumulative_percentage_df = df_subset[columns_to_plot].cumsum(axis=1) / df_subset[columns_to_plot].sum(axis=1).values[:, None] * 100

    # Set font size for axis labels and title
    font_size = 16

    # Set the figure size
    plt.figure(figsize=(16, 10))

    # Create an area chart
    sns.lineplot(x='Year', y=cumulative_percentage_df[columns_to_plot[0]], data=df_subset, label='Coal', color='blue', linewidth=2)
    sns.lineplot(x='Year', y=cumulative_percentage_df[columns_to_plot[1]], data=df_subset, label='Gas', color='orange', linewidth=2)
    sns.lineplot(x='Year', y=cumulative_percentage_df[columns_to_plot[2]], data=df_subset, label='Oil', color='green', linewidth=2)
    sns.lineplot(x='Year', y=cumulative_percentage_df[columns_to_plot[3]], data=df_subset, label='Hydroelectric', color='yellow', linewidth=2)

    # Set plot title and labels
    plt.title('Cumulative Percentage of Electricity Production from Different Sources (2000-2020)', fontsize=font_size + 2)
    plt.xlabel('Year', fontsize=font_size)
    plt.ylabel('Cumulative Percentage', fontsize=font_size)

    # Add legend and adjust position
    plt.legend(title='Energy Source', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=font_size - 2)

    # Show Plot
    plt.tight_layout()
    plt.show()

def bar_plot(file):
    df4 = pd.read_csv(file)
    countries_to_plot = ['Asia', 'China', 'India', 'Japan', 'United Kingdom']
    df4['Total Electricity Production'] = df4['Other Renewables'] + df4['Hydroelectric'] + df4['Oil'] + df4['Gas'] + df4['Coal']
    # Filter the dataset for the selected countries
    df_subset1 = df4[(df4['Entity'].isin(countries_to_plot)) & (df4['Year'] >= 2015) & (df4['Year'] <= 2020)]

    # Set font size for axis labels and title
    font_size = 16

    # Set the figure size
    plt.figure(figsize=(16, 10))

    # Create a stacked bar plot
    sns.barplot(x='Total Electricity Production', y='Entity', hue='Year', data=df_subset1, palette='viridis')

    # Set plot title and labels
    plt.title('Electricity Produced in TWh Over Years (Selected Countries)', fontsize=font_size + 2)
    plt.xlabel('Electricity Production (TWh)', fontsize=font_size)
    plt.ylabel('Country', fontsize=font_size)

    # Add legend and adjust position
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=font_size - 2)

    # Show Plot
    plt.tight_layout()
    plt.show()


# Call the function with the filename
pie_plot('final.csv')
line_plot('final.csv')
area_plot('final.csv')
bar_plot('final.csv')
