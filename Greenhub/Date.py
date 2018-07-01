import time
from datetime import datetime
import calendar
import operator


class Date:
    timestamp = 0

    ONE_DAY = 86400
    ONE_WEEK = ONE_DAY * 7

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

    def __eq__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is equal to the argument
        """

        return self.object_comparison(operator.eq, other)

    def __ne__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is not equal to the argument
        """

        return self.object_comparison(operator.ne, other)

    def __ge__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is greater than or equal to the argument
        """

        return self.object_comparison(operator.ge, other)

    def __gt__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is greater than the argument
        """

        return self.object_comparison(operator.gt, other)

    def __le__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is less than or equal to the argument
        """

        return self.object_comparison(operator.le, other)

    def __lt__(self, other):
        """

        Args:
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is less than the argument
        """

        return self.object_comparison(operator.lt, other)

    def object_comparison(self, op, other):
        """
        compare current object with other object

        Args:
            op    (method)                      : the operator method
            other (Union[Union[Date, str], int]): another date object or date/datetime format string or timestamp int

        Returns:
            bool: if current object is {op} to the argument
        """

        other_type = type(other)

        if other_type is Date:
            return op(self.timestamp, other.timestamp)

        if other_type is str:
            return op(self.timestamp, Date(other_type).timestamp)

        if other_type is int:
            return op(self.timestamp, other)

        return op(self.timestamp, int(other))

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

        self.timestamp = int(time.time())

        return self

    def set_date(self, date=None):
        """
        set current object to a date

        Args:
            date (str): the date/datetime format string
        """

        ts1 = calendar.timegm(Date.date_parser(date))

        self.timestamp = int(datetime.utcfromtimestamp(ts1).timestamp())

        return self

    # day related

    def tomorrow(self):
        """
        set object date to the next day
        """

        self.timestamp += self.ONE_DAY

        return self

    def yesterday(self):
        """
        set object date to the last day
        """

        self.timestamp -= self.ONE_DAY

        self.lowest_timestamp_check()

        return self

    def days_after(self, days):
        """
        set object date to the given days after

        Args:
            days (int): number of days after
        """

        self.timestamp += days * self.ONE_DAY

        return self

    def days_before(self, days):
        """
        set object date to the given days before

        Args:
            days (int): number of days before
        """

        self.timestamp -= days * self.ONE_DAY

        self.lowest_timestamp_check()

        return self

    # week related

    def next_week(self):
        """
        set object date to the next week
        """

        self.timestamp += self.ONE_WEEK

        return self

    def last_week(self):
        """
        set object date to the last week
        """

        self.timestamp -= self.ONE_WEEK

        self.lowest_timestamp_check()

        return self

    def weeks_after(self, weeks):
        """
        set object date to the given weeks after

        Args:
            weeks (int): number of weeks after
        """

        self.timestamp += weeks * self.ONE_WEEK

        return self

    def weeks_before(self, weeks):
        """
        set object date to the given weeks before

        Args:
            weeks (int): number of weeks before
        """

        self.timestamp -= weeks * self.ONE_WEEK

        self.lowest_timestamp_check()

        return self

    def lowest_timestamp_check(self):
        """
        check if timestamp goes below 0
        """

        if self.timestamp < 0:
            self.timestamp = 0
