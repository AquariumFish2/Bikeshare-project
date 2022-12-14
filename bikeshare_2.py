import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['saturday', 'sunday', 'monday',
        'tuesday', 'wednesday', 'thursday', 'friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        city = input(
            "Which city would you like to explore (Chicago, New york city, Washington)").lower()
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            print('wrong city try again chose one on the given cities\n')
    # get user input for month (all, january, february, ... , june)
    while (True):
        month = input(
            "which month would you like to explore (all, january, february, ... , june)").lower()
        got_right_month = False
        for every_month in MONTHS:
            if(month == 'all' or month == every_month):
                got_right_month = True
                break
        if not(got_right_month):
            print('please try again with a valid month name')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        day = input(
            "which day would you like to explore (saturday, sunday ,..,friday)").lower()
        got_right_day = False
        for every_day in DAYS:
            if(day == 'all' or day == every_day):
                got_right_day = True
                break
        if not got_right_day:
            print('Please Type a vaid day\n')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city], parse_dates=True)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Week Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour
    # print(df[['Start Time','Week Day','Month']])
    # print(month)
    # print(day)
    # print(df.columns)
    if month != 'all':
        df = df[df['Month'] == month.title()]
    if day != 'all':
        df = df[df['Week Day'] == day.title()]
    # print(df.head())
    return df


def time_stats(df: pd.DataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Common month is:', df['Month'].value_counts().idxmax())

    # display the most common day of week
    print('Most Common Day is:', df['Week Day'].value_counts().idxmax())

    # display the most common start hour
    print('Most Common Start Hour is:',
          df['Start Hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df: pd.DataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Commonly Used Start Station:',
          df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('Most Commonly Used End Station:',
          df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start Station and End Station:',
          'Start Session: '+df['Start Station'].add('  End Session: '+df['End Station']).value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df:pd.DataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:',df['Trip Duration'].sum())
    # display mean travel time
    print('Average of travel time:',df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df:pd.DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Types:')
    for key,value in df['User Type'].value_counts().items():
        print(key,':',value)
    print()
    # print(dic)
    # Display counts of gender
    try:
        print('Counts of Gender:')
        for key,value in df['Gender'].value_counts().items():
            print(key,':',value)
    except KeyError:
        print('There is no gender value in this city')
    # Display earliest, most recent, and most common year of birth
    try:
        print('Earliest year of birth',df['Birth Year'].min())
        print('Most Recent year of birth',df.sort_values(by=['Start Time'])['Birth Year'][0])
        print('Most Common year of birth',df['Birth Year'].value_counts().idxmax())
    except KeyError:
        print('There is no Year of Birth value in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df:pd.DataFrame):
    display = input("Do you want to display the first 5 rows ?(Yes/No)").lower()
    index = 5
    start = 0

    while(display!='no'):
        if(display == 'yes'):
            print(df[start:index])
            index +=5
            start +=5
            display = input("Do you want to display the next 5 rows ?(Yes/No)").lower()
        elif (display !='yes' or display != 'no'):
                display = input('Please Enter (Yes or No)').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
