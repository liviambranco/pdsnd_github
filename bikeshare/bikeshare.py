import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhat city would you like to analyze? \nChicago, New York City or Washington? ').lower()
        if city not in ['chicago', 'new york city', 'washington']:
                        print('\nSorry, the city you entered is not in our database.')
        else:
                        print('\nYou chose:', city.upper())
                        break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease specify the month to analyze (all, January until June): ').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('\nSorry, you entered an invalid month.')
        else:
                print('\nYou chose:', month.upper())
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nPlease specify the day of the week to analyze (all, monday...): ').lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('\nSorry, you entered an invalid day.')
        else:
                print('\nYou chose:', day.upper())
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most popular month is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('\nThe most popular day is:', popular_day)

    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nThe most popular start station is:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nThe most popular end station is:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Stations'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    popular_route = df ['Start and End Stations'].mode()[0]

    print('\nThe most popular route station is:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time was:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time was:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThis is the user type breakdown\n',user_types)

    # TO DO: Display counts of gender

    try:
        user_gender = df['Gender'].value_counts()
        print('\nThis is the gender breakdown\n',user_gender)
    except:
        print('\nSorry, no gender information available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min().astype(int)
        print('\nThe oldest client was born in:', earliest_year_of_birth)
        most_recent_year_of_birth = df['Birth Year'].max().astype(int)
        print('\nThe youngest client was born in:', most_recent_year_of_birth)
        most_common_year_of_birth = df['Birth Year'].mode()[0].astype(int)
        print('\nMost clients were born in:', most_common_year_of_birth)

    except:
        print('\nSorry, no birth year information available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    """
    Asks user to whether they would like to see the raw data.
    If the user answers 'yes,' print 5 rows of the data at a time.

    Returns:
        df - Pandas DataFrame containing city data
    """

    x = 0
    while True:
        prompt_1 = input('\nWould you like to see 5 rows of the statistics raw data? Enter yes or no.\n').lower()
        if prompt_1 in ['n', 'no', 'np']:
            break
        elif prompt_1 not in ['yes', 'y', 'ye', 'ys', 'n', 'no', 'np']:
            print('\nNot sure what you mean. Would you like to see the statistics raw data? Enter yes or no.\n').lower()
        elif prompt_1 in ['yes', 'y', 'ye', 'ys']:
            print(df.iloc[x:x + 5])
            x = x + 5

    """
    Continue prompting and printing the next 5 rows at a time until the user chooses 'no.'

    Returns:
        df - Pandas DataFrame containing city data
    """


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
