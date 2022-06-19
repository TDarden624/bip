import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv', 'New york city': 'new_york_city.csv',
              'washington': 'washington.csv', 'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    while True:
        print('\nWhich city would you like to analyze?:')
        if city.lower() == 'chicago':
                print("\nAlright, let's check out Chicago!\n")
                return 'chicago.csv'
        elif city.lower() == 'new york':
                print("\nAlright, let's check out New York!\n")
                return 'new_york_city.csv'
        elif city.lower() == 'washington':
                print("\nAlright, let's check out Washington!\n")
                return 'washington.csv'
                continue
    while city not in('chicago.csv', 'new_york_city.csv', 'washington.csv'):
        print("\nPlease enter: Chicago, New York or Washington\n")
        break

                
    while True:
        print("\nPlease choose a month to filter by: January, Febuary, March, April, May, June or all\n")
        if month not in('January','Febuary','March','April','May','June','none'):
                return("\nPlease enter a valid month\n")
                continue
        else:
                print("\nYou've chose {month.title()} as your month.")
        month = input().lower()
        break

    
    while True:
        print("\nPlease choose a day to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n")
        if day not in('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
                return("\nPlease enter a valid day\n")
        else:
                print("\nPulling up {day.title()}")
        day = input().lower()
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
    df = pd.read_csv(CITY_DATA[city])

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    pop_month = df['month'].mode()[0]
    print('Most common month:', pop_month)


    pop_day = df['day'].mode()[0]
    print('Most common day:', pop_day)

       
    pop_hour = df['hour'].mode()[0]
    print('Most common start time:', pop_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print("\nThe most common start station: {pop_start_station}")

    # display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print("\nThe most common end station: {pop_end_station}")

    # display most frequent combination of start station and end station trip
    pop_combo_station = df['Start Station', 'End Station'].mode()[0]
    print('\nThe most common combination station: {}, {}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("\nTotal trip duration is {} hours, {} minutes and {} seconds.")
    # display mean travel time
    mean_trip = df['Trip Duration'].mean()
    minute, second = divmod(mean_time, 60)
    if min > 60:
          hour, minute = divmod(minute, 60)
          print("\nThe average trip is {} hours, {} minutes and {} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertype = df['User Type'].value_counts()
    print("The user types are:\n", user_counts)

    # Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
          User_gender = df['Gender'].value_counts()
          print("The types of user by 'Gender' are:\n", user_gender)

    # 
def birth_year(df):
    """Display earliest, most recent, and most common year of birth."""
          
    earliest_year = df['birth_year'.min()]
    latest_year = df['birth_year'.max()]
    common_year = df['birth_year'.mode()]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    print(df)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
    


        if __name__ == "__main__":
            
            main()
