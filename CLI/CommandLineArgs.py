import sys


class CommandLineArgs:
    flags = {}
    params = {}
    arguments = []

    def __init__(self):
        """
        get and set command line options
        """

        options = self.parse_args(sys.argv[1:])

        self.flags = options['flags']
        self.params = options['params']
        self.arguments = options['arguments']

    def __str__(self):
        return str({
            'flags': self.flags,
            'params': self.params,
            'arguments': self.arguments,
        })

    @staticmethod
    def parse_args(args):
        """
        parse a list of arguments and set them into corresponding category

        Args:
            args (list): argument list

        Returns:
            dict: a dict of options having keys
                - flags     (dict): the flag and its value
                - params    (dict): the parameter and its value
                - arguments (list): ordered arguments
        """

        # init options dict
        options = {
            'flags': {},
            'params': {},
            'arguments': [],
        }

        # loop through arguments
        for arg in args:
            # if is option
            if arg[:2] == '--':
                # get separator position
                separator = arg.find('=')

                # get value of the command
                value = CommandLineArgs.auto_convert(arg[separator + 1:])

                # if is flag usage | e.g. --some_true_val
                if separator == -1:
                    options['flags'][arg[2:]] = True

                elif type(value) is bool:
                    options['flags'][arg[2:separator]] = value

                # if is params usage | e.g. --some_param=20
                else:
                    options['params'][arg[2:separator]] = value

            # if is ordered argument | e.g. some
            else:
                options['arguments'].append(arg)

        return options

    @staticmethod
    def boolify(string):
        """
        convert string to boolean type

        Args:
            string (str): the value needs to be check if is boolean type

        Returns:
            bool: if the input is boolean type string, return the value otherwise raise error
        """

        if string == 'True' or string == 'true':
            return True

        if string == 'False' or string == 'false':
            return False

        raise ValueError("wrong type")

    @staticmethod
    def auto_convert(string):
        """
        convert string to corresponding type (bool, int, float, string)

        Args:
            string (str): the string that needs to be check the type

        Returns:
            bool
            int
            float
            string
        """

        for fn in (CommandLineArgs.boolify, int, float):
            try:
                return fn(string)
            except ValueError:
                pass

        return string
