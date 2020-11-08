import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from matplotlib import dates as mpl_dates

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)


# Clean data
f25 = df['value'] <= df['value'].quantile(0.025)
f75 = df['value'] >= df['value'].quantile(0.975)
cond = (f25 | f75)
df = df.drop(index=df[cond].index)

months=['January','February','March','April','May','June','July','August','September','October','November','December']

def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots(figsize=(20, 6))
    
    ax.plot_date(df.index, df['value'], linestyle='solid', marker=None, color="red")
    ax.set_xlabel('Date',fontsize=10)
    ax.set_ylabel('Page Views',fontsize=10)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(180))
    
    date_format = mpl_dates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_formatter(date_format)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year']=df_bar.index.year
    df_bar['Month']=df_bar.index.strftime('%B')
    df_bar_grp=df_bar.groupby(['year','Month'])
    
    df_bar_grp['value'].apply(lambda x: x.mean())

    # Draw bar plot
    # There are five preset seaborn themes: darkgrid, whitegrid, dark, white, and ticks
    sns.set_style("ticks")
    sns.set_context("paper")
    sns.despine(ax=None)
    xx=sns.catplot(x='year',y='value', hue='Month', data=df_bar, hue_order=months,ci=None,legend=False,palette='bright',kind='bar',height=9,legend_out=False)
    fig=xx.fig
    ax=xx.ax
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title='Months')
    plt.setp(ax.get_legend().get_texts(), fontsize=8)
    plt.setp(ax.get_legend().get_title(), fontsize=8)
    #plt.tight_layout()
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    df_box.sort_values(by=['year','date'], ascending=[False, True], inplace=True)



    def fixed_boxplot(*args, label=None, **kwargs):
        sns.boxplot(*args, **kwargs, labels=[label])
    # Draw box plots (using Seaborn)
    df_box["Page Views"] = df_box["value"]
    df_box["Month"] = df_box["month"]
    df_box["Year"] = df_box["year"]
    sns.color_palette('dark')
    g = sns.PairGrid(df_box, y_vars=["Page Views"], x_vars=["Year", "Month"],despine=False)
    g.map(fixed_boxplot)
    fig = g.fig
    fig.set_figheight(8)
    fig.set_figwidth(15)
    fig.axes[0].set_ylabel('Page Views')
    fig.axes[1].set_ylabel('Page Views')
    fig.axes[0].set_title('Year-wise Box Plot (Trend)')
    fig.axes[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()
    





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
