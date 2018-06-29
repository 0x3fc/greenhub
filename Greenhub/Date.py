import time


# date range constants
ONE_DAY = 86400
ONE_WEEK = ONE_DAY * 7


class Date:
    timestamp = 0

    def __init__(self):
        self.now()

    def __str__(self, with_time=False):
        time_str = '%Y-%m-%d'

        if with_time:
            time_str += '%H:%M:%S'

        return time.strftime(time_str, self.timestamp)

    def now(self):
        self.timestamp = time.time()

    # day related

    def tomorrow(self):
        self.timestamp += ONE_DAY

    def yesterday(self):
        self.timestamp -= ONE_DAY

        self.lowest_timestamp_check()

    def days_after(self, days):
        self.timestamp += days * ONE_DAY

    def days_before(self, days):
        self.timestamp -= days * ONE_DAY

        self.lowest_timestamp_check()

    # week related

    def next_week(self):
        self.timestamp += ONE_WEEK

    def last_week(self):
        self.timestamp -= ONE_WEEK

        self.lowest_timestamp_check()

    def weeks_after(self, weeks):
        self.timestamp += weeks * ONE_WEEK

    def weeks_before(self, weeks):
        self.timestamp -= weeks * ONE_WEEK

        self.lowest_timestamp_check()

    def lowest_timestamp_check(self):
        if self.timestamp < 0:
            self.timestamp = 0
