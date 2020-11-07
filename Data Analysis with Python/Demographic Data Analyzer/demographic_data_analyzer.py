import pandas as pd
import numpy as np
from collections import Counter

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None
    df=pd.read_csv("adult.data.csv")

    tot=len(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels

    race_count=df["race"].value_counts()

    # What is the average age of men?
    average_age_men=round(df.loc[df['sex']=='Male','age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    
    percentage_bachelors=round((len(df[df['education']=='Bachelors'])/tot)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    

    # percentage with salary >50K
    
    options=['Bachelors', 'Masters', 'Doctorate']

    y=df[df['education'].isin(options)]

    c_high=len(y)


    ## higer education + sal> 50K
    y=y[y['salary']=='>50K']
    c_high_sal=len(y)

    higher_education_rich=round((c_high_sal/c_high)*100,1)

    ## lower education rich

    c_low_edu=tot-c_high

    criterion = lambda row: row['education'] not in options
    y=df[df.apply(criterion,axis=1)]
    y=y[y['salary']=='>50K']

    c_low_edu_rich=len(y)

    lower_education_rich=round((c_low_edu_rich/c_low_edu)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours=df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None
    y=df[df['hours-per-week']==min_work_hours]
    c_min_hr=len(y)
    y=y[y['salary']=='>50K']
    c_min_hr_rich=len(y)

    rich_percentage=round((c_min_hr_rich/c_min_hr)*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None
    y=df['native-country'].tolist()
    yy=set(y)
    z=df[df['salary']=='>50K']

    st=[]
    ls=[]

    for i in yy:
        ls.append(i)
        xx=z[z['native-country']==i]
        c_pop_i=y.count(i)
        c_pop_i_rich=len(xx)
    
        st.append(round((c_pop_i_rich/c_pop_i)*100,1))

    highest_earning_country_percentage=max(st)
    
    highest_earning_country=ls[st.index(max(st))]


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    z=df[df['salary']=='>50K']


    xx=z[z['native-country']=='India']

    zz=xx['occupation'].tolist()
    xx=list(Counter(zz).keys())
    top_IN_occupation=xx[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
