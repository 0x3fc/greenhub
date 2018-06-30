import time
from datetime import datetime
import calendar


# date range constants
ONE_DAY = 86400
ONE_WEEK = ONE_DAY * 7


class Date:
    timestamp = 0

    def __init__(self, date=None):
        """
        initialize current object with given date or now

        Args:
            date (str): the date/datetime format string
        """

        # set object timestamp to now
        if date is None:
            self.now()

        # set object timestamp to the date given
        else:
            self.set_date(date)

    def __str__(self):
        """
        transform object to datetime format string

        Returns:
            str: datetime format string
        """

        return str(datetime.fromtimestamp(self.timestamp))

    @staticmethod
    def date_parser(date):
        """
        parse a date/datetime format string to date time tuple

        Args:
            date (str): the date/datetime format string

        Returns:
            tuple: transformed datetime tuple having
                - (int): year
                - (int): month
                - (int): day
                - (int): hour
                - (int): minute
                - (int): second
        """

        parsed_datetime = date.strip().split(maxsplit=2)

        # get date part data
        try:
            date_part = parsed_datetime[0].split('-', maxsplit=3)
        except IndexError:
            date_part = [1970, 1, 1]

        # set year
        try:
            year = int(date_part[0])
        except IndexError:
            year = 1970

        # set month
        try:
            month = int(date_part[1])
        except IndexError:
            month = 1

        # set day
        try:
            day = int(date_part[2])
        except IndexError:
            day = 1

        # get time part data
        try:
            time_part = parsed_datetime[1].split(':', maxsplit=3)
        except IndexError:
            time_part = [0, 0, 0]

        # set hour
        try:
            hour = int(time_part[0])
        except IndexError:
            hour = 0

        # set minute
        try:
            minute = int(time_part[1])
        except IndexError:
            minute = 0

        # set second
        try:
            second = int(time_part[2])
        except IndexError:
            second = 0

        return year, month, day, hour, minute, second

    def now(self):
        """
        set date object to current time
        """

        self.timestamp = time.time()

    def set_date(self, date=None):
        """
        set current object to a date

        Args:
            date (str): the date/datetime format string
        """

        ts1 = calendar.timegm(Date.date_parser(date))

        self.timestamp = datetime.utcfromtimestamp(ts1).timestamp()

    # day related

    def tomorrow(self):
        """
        set object date to the next day
        """

        self.timestamp += ONE_DAY

    def yesterday(self):
        """
        set object date to the last day
        """

        self.timestamp -= ONE_DAY

        self.lowest_timestamp_check()

    def days_after(self, days):
        """
        set object date to the given days after

        Args:
            days (int): number of days after
        """

        self.timestamp += days * ONE_DAY

    def days_before(self, days):
        """
        set object date to the given days before

        Args:
            days (int): number of days before
        """

        self.timestamp -= days * ONE_DAY

        self.lowest_timestamp_check()

    # week related

    def next_week(self):
        """
        set object date to the next week
        """

        self.timestamp += ONE_WEEK

    def last_week(self):
        """
        set object date to the last week
        """

        self.timestamp -= ONE_WEEK

        self.lowest_timestamp_check()

    def weeks_after(self, weeks):
        """
        set object date to the given weeks after

        Args:
            weeks (int): number of weeks after
        """

        self.timestamp += weeks * ONE_WEEK

    def weeks_before(self, weeks):
        """
        set object date to the given weeks before

        Args:
            weeks (int): number of weeks before
        """

        self.timestamp -= weeks * ONE_WEEK

        self.lowest_timestamp_check()

    def lowest_timestamp_check(self):
        """
        check if timestamp goes below 0
        """

        if self.timestamp < 0:
            self.timestamp = 0
