import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('../projeto02_boilerplate-demographic-data-analyzer/adult.data.csv') ## Check


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() ## Check


    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1) ## Check


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df['education'])) * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    total_advanced_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_more50k = total_advanced_edu[total_advanced_edu['salary'] == '>50K']

    higher_education = round((len(higher_edu_more50k) / len(total_advanced_edu)) * 100, 1)


    total_non_advanced_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_more50k = total_non_advanced_edu[total_non_advanced_edu['salary'] == '>50K']

    lower_education = round((len(lower_edu_more50k) / len(total_non_advanced_edu)) * 100, 1)


    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == 1])

    rich_percentage = (len(df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')]) / num_min_workers) * 100
    rich_percentage


    # What country has the highest percentage of people that earn >50K?
    series_country_salary = df[df['salary'] == '>50K']['native-country']
    series_country_salary = series_country_salary.value_counts()

    series_country_total = df['native-country']
    series_country_total = series_country_total.value_counts()

    country_percentage_50K = []

    for country_salary, values_salary in series_country_salary.items():
        for country_total, values_total in series_country_total.items():
            if country_total == country_salary:
                percentage = round((values_salary / values_total) * 100, 1)
                country_percentage_50K.append(percentage)

    highest_earning_country_value = country_percentage_50K[13]
    highest_earning_country_percentage_index = series_country_salary.index[13]

    highest_earning_country_percentage_value = 0
    for i in country_percentage_50K:
        if i >  highest_earning_country_percentage_value:
            x = i
        highest_earning_country_percentage_value = x

    highest_earning_country = highest_earning_country_percentage_index

    highest_earning_country_percentage = highest_earning_country_percentage_value

 
    # Identify the most popular occupation for those who earn >50K in India.
    df_India_high_salary = df[(df['native-country'] == "India") & (df['salary'] == '>50K')]
    top_IN_occupation = df_India_high_salary['occupation'].mode()
    top_IN_occupation = df_India_high_salary['occupation'].iloc[0]

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
