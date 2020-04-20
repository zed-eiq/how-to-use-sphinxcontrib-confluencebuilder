class ExampleEcho:
    """ExampleEcho is a
    sample class that
    allows you to initialize an
    Echo object that can take ``input``
    and immediately return it.
    """

    def __init__(self):
        pass

    def __call__(self, input):
        """

        @param input string: Input should be a string
        @return: string
        """

        if isinstance(input, str):
            return input
        else:
            return ""
