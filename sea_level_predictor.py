import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file

    df = pd.read_csv(r"epa-sea-level.csv")

    
    # Create scatter plot
    fg, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c = "#D50032")

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years = np.arange(1880, 2051)
    line_values = slope * years + intercept

    plt.plot(years, line_values, '#000000')

    # Create second line of best fit
    later_years = df [df['Year'] >= 2000]
    slope, intercept, r_value, p_value, stderr = linregress(later_years["Year"], later_years['CSIRO Adjusted Sea Level'])

    recent_years = np.arange(2000, 2051)
    second_line_values = slope * recent_years + intercept

    plt.plot(recent_years, second_line_values, '#009A68')

    # Add labels and title

    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == "__main__":
    draw_plot()