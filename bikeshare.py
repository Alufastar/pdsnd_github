import time
import pandas as pd
import numpy as np

pd.__version__

pd.__version__

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
    start_time = time.time()

    print('Hello! Let\'s explore some US bikeshare data!')
    print('-' * 40)

    CITY_DIC = {1: 'chicago',
                2: 'new york city',
                3: 'washington'}

    MONTH_DIC = {1: 'january',
                 2: 'february',
                 3: 'march',
                 4: 'april',
                 5: 'may',
                 6: 'june',
                 7: 'january-june'}

    WEEKDAY_DIC = {1: 'monday',
                   2: 'tuesday',
                   3: 'wednesday',
                   4: 'thursday',
                   5: 'friday',
                   6: 'saturday',
                   7: 'sunday',
                   8: 'all'}

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city_number = input(
                "Which city do you want to check? Please key in numbers: 1 for chicago, 2 for new york city, 3 for washington")

            city = CITY_DIC[int(city_number)]
            print('Thanks, you selected ' + city)
            break
        except:
            print("Humm this is not a valid option, let us try again:")

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month_number = input(
                "Which month do you want to check? Please key in numbers: 1 for January,..., 6 for june,7 for January-June")

            month = MONTH_DIC[int(month_number)]
            print('Thanks, you selected ' + month)
            break
        except:
            print("Humm this is not a valid option, let us try again:")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            weekday_number = input(
                "Which weekday do you want to check? Please key in numbers: 1 for Monday,..., 7 for Sunday,8 for all")

            day = WEEKDAY_DIC[int(weekday_number)]
            print('Thanks, you selected ' + day)
            break
        except:
            print("Humm this is not a valid option, let us try again:")


    print("All set! The following analysis will focus on "+ city+", "+month+", "+day)
    print('-' * 40)

    return city, month, day

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



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
    start_time = time.time()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['start_hour'] = pd.DatetimeIndex(df["Start Time"]).hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october',
                  'november','december']

        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def display_data(df):
    """
    Display data per request, and only display the next 5 rows at every prompt.
    As long as the user does not enter no, we are inside in the loop.
    """
    start_time = time.time()

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data != "no":
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df.month.value_counts().idxmax()
    print('Most Frequent Start month:', popular_month)

    # display the most common day of week
    popular_day = df.day_of_week.value_counts().idxmax()
    print('Most Frequent Start day of week:', popular_day)

    # display the most common start hour
    popular_start_hour = df.start_hour.value_counts().idxmax()
    print('Most common start hour: ', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['S_E_Station'] = df['Start Station'] + " , " + df['End Station']

    popular_start_end_station = df['S_E_Station'].value_counts().idxmax()
    print('Most commonly used start-end station combination: ', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].sum()," seconds")


    # display mean travel time
    print( "Average travel time per trip: ", df['Trip Duration'].mean()," seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby("User Type").size()
    print('Count of user types:')
    print(user_types)

    # Display counts of gender
    try:
        gender_counts = df.groupby("Gender").size()
        print('Count of genders:')
        print(gender_counts)
    except:
        print('The selected dataset does not have gender information.')

    # Display earliest, most recent, and most common year of birth
    try:
        oldest = df['Birth Year'].min().astype(int)
        youngest = df['Birth Year'].max().astype(int)
        popular_birth = df['Birth Year'].value_counts().idxmax().astype(int)

        print('For the given scope, the users are born between',oldest,'and',youngest,'.'
          ,'\nThe most common birth year is', popular_birth,'.')
    except:
        print('The selected dataset does not have birth year information.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
