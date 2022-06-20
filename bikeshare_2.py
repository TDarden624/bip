import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    global input_month
    global input_day
    
    month = ['January', 'Febuary', 'March', 'April', 'May', 'June']
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city =['Chicago', 'New York', 'Washington']
    while True:
        input_city = input('\nWhich city would you like to analyze?:').lower()
        if input_city == 'Chicago':
                print("\nAlright, let's check out chicago.lower()!\n")
                break
                return 'chicago.csv'
        elif input_city == 'New York':
                print("\nAlright, let's check out New York.lower()!\n")
                break
                return 'new_york_city.csv'
        elif input_city == 'Washington':
                print("\nAlright, let's check out Washington.lower()!\n")
                break
                return 'washington.csv'
                continue
        if input_city not in city:
           return("\nPlease enter: Chicago, New York or Washington\n")
           continue
        else:
            break
              
    while True:
        input_month = input('\nPlease select a month to filter by or enter none for no filter').lower()
        print("\nYou've chose {month.title()} as your month.")
        if input_month not in month:
                return("\nPlease enter a valid month\n")
                continue
        else:
                break
    while True:
        input_day = input('\nPlease select a day to filter by or enter all for all options').lower()
        print("\nPulling up {day.title()}")
        if input_day not in day:
                return("\nPlease enter a valid day\n")
                continue
        else:
            break
        
    print('-'*40)
    return input_city, input_month, input_day


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
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()

       
