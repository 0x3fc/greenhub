from os import path
from subprocess import call
import random
from .Date import Date


class Greenhub:
    file_name = 'green.hub'

    def __init__(self):
        """
        create commit file if not exists
        """

        if not path.isfile(self.file_name):
            open(self.file_name, 'w')

    @staticmethod
    def commit_everyday(start_date=None, commit_count_range=None):
        """
        commit everyday from a start date so the time line in github shows green

        Args:
            start_date         (str) : the start date
            commit_count_range (list): the range of the commit times (e.g. [1, 5]: will commit randomly once to five
                                       times)
        """

        # set start date to last year so it covers the whole time line if start date is not specified
        if start_date is None:
            start_date = Date().days_before(380)

        else:
            start_date = Date(start_date)

        # commit everyday until now
        Greenhub.commit_in_range(start_date, Date().tomorrow(), commit_count_range)

    @staticmethod
    def commit_in_range(start_date, end_date, commit_count_range=None):
        """
        commit from start date til end date (include start date, exclude end date)

        Args:
            start_date         (Date): the start date (inclusive: will have commit on this date)
            end_date           (Date): the end date (exclusive: will not have commit on this date)
            commit_count_range (list): the range of the commit times (e.g. [1, 5]: will commit randomly once to five
                                       times)
        """

        # check if start date is larger than end date
        if start_date > end_date:
            return

        if commit_count_range is None:
            commit_count_range = [1, 1]

        # commit start date and move to next date until reaches end date
        while start_date != end_date:
            for commit_times in range(0, random.randint(commit_count_range[0], commit_count_range[1])):
                Greenhub.commit(str(start_date))

            start_date.tomorrow()

    @staticmethod
    def commit(date):
        """
        commit a file and change the date to the given date

        Args:
            date (str): the commit date with date format
        """

        # update file
        Greenhub.write(date)

        # git add {file_name}
        call(['git', 'add', Greenhub.file_name])

        # git commit -m "{date}" --date="{date}"
        call(['git', 'commit', '-m', "%s" % date, '--date="%s"' % date])

    @staticmethod
    def write(date):
        """
        write green hub file a date and a random number

        Args:
            date (str): the date that will appear in the file
        """

        # set file content to a date time with a random number
        content = '%s: %f' % (date, random.random())

        # update file with the content
        with open(Greenhub.file_name, 'w') as file:
            file.write(content)
