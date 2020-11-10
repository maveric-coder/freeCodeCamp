import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np




def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')



    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])



    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #print(slope,intercept)
    
    
    x_extended = np.arange(1880, 2050)

    plt.plot(x_extended, intercept + slope*x_extended, "b")
    


    # Create second line of best fit
    df_new=df[df['Year']>=2000]
    x_extended = np.arange(2000, 2050)

    
    
    slope, intercept, r_value, p_value, std_err = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    plt.plot(x_extended, intercept + slope*x_extended, "--r")
    
    


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend(['Since 1880','After 2000'])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()