class Page(object):
    def __init(self):
        self.__title = "Sandwich"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = ""
        self.__error = ' '
        self.__close = """
    </body>
</html>
        """
    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all