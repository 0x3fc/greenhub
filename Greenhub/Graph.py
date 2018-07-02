from Greenhub import Date
from os import path


class Graph:
    file_name = 'graph.txt'

    EMPTY_GRAPH = """.....................................................
.....................................................
.....................................................
.....................................................
.....................................................
.....................................................
....................................................."""

    def __init__(self):
        """
        initialize graph object
        """

        self.make_graph()

    @staticmethod
    def process(start_date, name=None):
        """
        process the graph

        Args:
            start_date (Union[Date, str]): the first date (top left corner) of the graph
            name       (str)             : the file name of the new graph, default Graph.file_name

        Returns:
            dict: processed graph info
                - keys   (Date): graph corresponding dates
                - values (int) : the commit times
        """

        # set the default file name to graph file name
        if name is None:
            name = Graph.file_name

        # check if graph exists
        if not path.isfile(name):
            return

        # set the start date object
        if type(start_date) is not Date:
            start_date = Date(start_date)

        # read graph
        file = open(name, 'r')

        # init graph dict
        graph = {}

        # read 7 lines
        for line_number in range(7):
            Graph.parse_line(str(start_date), file.readline().rstrip('\n'), graph)
            start_date.tomorrow()

        # close file
        file.close()

        return graph

    @staticmethod
    def parse_line(start_date, content, graph):
        """
        parse one line of the graph

        Args:
            start_date (str) : the first date of the content
            content    (str) : the graph representation line
            graph      (dict): the graph dict; result will be added to this argument
        """

        # set a start date object
        start_date = Date(start_date)

        # loop through each day in the content line
        for commit in content:
            # get commit date
            commit_date = str(start_date)

            # get commit times
            commit_times = Graph.convert_graph_number(commit)

            # write to graph
            if commit_times > 0:
                graph[commit_date] = commit_times

            # move date to next week
            start_date.next_week()

    @staticmethod
    def convert_graph_number(num):
        """
        translate graph number representation to integer

        Args:
            num (str): the graph number representation

        Returns:
            int: the translated graph number
        """

        # . represents 0
        if num == '.':
            num = 0

        # 1-9 + 0 represent 1-10
        elif num.isnumeric():
            num = int(num)

        # A-Z represent 11-36
        elif num.isupper():
            num = ord(num) - 54

        # a-z represent 37-62
        elif num.islower():
            num = ord(num) - 60

        return num

    @staticmethod
    def make_graph(name=None, force=False):
        """
        create a graph file for filling graph

        Args:
            name  (str) : the file name of the new graph, default Graph.file_name
            force (bool): force mode will write an empty graph if the graph already exists
        """

        # set default file name to graph file name
        if name is None:
            name = Graph.file_name

        # check if file exists or in force mode
        if not path.isfile(name) or force:
            # write file with an empty graph
            with open(name, 'w') as file:
                file.write(Graph.EMPTY_GRAPH)
