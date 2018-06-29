from os import path
from subprocess import call
from random import random


class Greenhub:
    file_name = 'green.hub'

    def __init__(self):
        """
        create commit file if not exists
        """

        if not path.isfile(self.file_name):
            open(self.file_name, 'w')

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
        call(['git', 'commit', '-m', date, '--date="%s"' % date])

    @staticmethod
    def write(date):
        """
        write green hub file a date and a random number

        Args:
            date (str): the date that will appear in the file
        """

        # set file content to a date time with a random number
        content = 'date: %d' % random()

        # update file with the content
        with open(Greenhub.file_name, 'w') as file:
            file.write(content)
