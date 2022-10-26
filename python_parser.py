

class FileReader:

    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        self.code = [x for x in "".join(lines)][::-1]

    def peek(self, n=1):
        if n > len(self.code):
            print(f"Error, file reader has input {self.code[::-1]} remaining, that has length {len(self.code)}, but {n} characters were requested.")
            return self.code
        if n == 1:
            return self.code[-1]
        return self.code[-n:][::-1]

    def consume(self, n=1):
        if n > len(self.code):
            print(f"Error, file reader has input {self.code[::-1]} remaining, that has length {len(self.code)}, but {n} characters were requested.")
            return self.code
        end = self.code[-n:]
        self.code = self.code[:-n]
        if n == 1:
            return end[0]
        return end[::-1]

    def isEOF(self):
        return len(self.code) == 0

    def chars_left(self):
        return len(self.code)

class Lexer:
    """
    Possible output things are:
      - variable: ["variable", {variable string}]
      - symbol: ["symbol", {symbol}] -> Values are: "=-+[]{}(),"
      - string literal: ["string", {string value}]
      - numerical literal: ["number", {string of numbers}]
      - tabs: ["tab", {number saying how many indents (0 is allowed)}]
    """

    LETTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    NUMBERS = "0123456789"
    OTHER_VARIABLE_CHARS = "_"
    SYMBOLS = "=-+[]{}()"

    def __init__(self, reader):
        self.reader = reader
        self.tokens = []
        self.current_token = None
        self.in_string_literal = False
        self.string_literal_start = None
        self.in_numerical_literal = False
        self.at_start_tabulation = True
        self.error = False
        self.in_variable_creation = False
        while not self.reader.isEOF():
            ch = self.reader.peek()
            if self.in_string_literal:
                if ch == "\\":
                    self.reader.consume()
                    self.current_token.append(self.reader.consume())
                    continue
                if ch == self.string_literal_start:
                    self.reader.consume()
                    self.tokens.append(["string", "".join(self.current_token)])
                    self.current_token = None
                    self.in_string_literal = False
                    self.string_literal_start = None
                    continue
                self.current_token.append(self.reader.consume())
                continue
            if self.in_numerical_literal:
                if ch in Lexer.NUMBERS:
                    self.current_token.append(self.reader.consume())
                    continue
                self.in_numerical_literal = False
                self.tokens.append(["number", "".join(self.current_token)])
                self.current_token = None
                continue
            if self.at_start_tabulation:
                if ch == " ":
                    if self.current_token is None:
                        self.current_token = [self.reader.consume()]
                        continue
                    self.current_token.append(ch)
                    continue
                self.at_start_tabulation = False
                if self.current_token is None:
                    self.tokens.append(["tab", 0])
                    continue
                if len(self.current_token) % 4 != 0:
                    print(f"Error, unexpected indentation: {len(self.current_token)}")
                    self.error = True
                    break
                self.tokens.append(["tab", len(self.current_token) // 4])
                self.current_token = None
                continue
            if self.in_variable_creation:
                if ch in Lexer.LETTERS + Lexer.NUMBERS + Lexer.OTHER_VARIABLE_CHARS:
                    self.current_token.append(self.reader.consume())
                    continue
                self.in_variable_creation = False
                self.tokens.append(["variable", "".join(self.current_token)])
                self.current_token = None
                continue
            if ch in Lexer.SYMBOLS:
                self.tokens.append(["symbol", self.reader.consume()])
                continue
            if ch == "\n":
                self.at_start_tabulation = True
                self.current_token = None
                self.reader.consume()
                continue
            if ch in "\"'":
                self.in_string_literal = True
                self.current_token = []
                self.string_literal_start = self.reader.consume()
            if ch in Lexer.NUMBERS:
                self.in_numerical_literal = True
                self.current_token = [self.reader.consume()]
                continue
            if ch in Lexer.LETTERS + Lexer.OTHER_VARIABLE_CHARS:
                self.in_variable_creation = True
                self.current_token = [self.reader.consume()]
                continue
            print(f"Token '{self.reader.consume()}' has no meaning, skipping")
        print(self.tokens)


if __name__ == '__main__':
    reader = FileReader("test.py")
    lexer = Lexer(reader)
