

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

class MockReader:
    def __init__(self, chars):
        print(chars)
        self.code = chars[::-1]

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


class Lexer:
    """
    Possible output things are:
      - variable: ["variable", {variable string}]
      - symbol: ["symbol", {symbol}] -> Values are: "=-+[]{}(),"
      - string literal: ["string", {string value}]
      - numerical literal: ["number", {string of numbers}]
      - tabs: ["tab", {number saying how many indents (0 is allowed)}]
      - keyword: ["keyword", {keyword string}]
    """

    LETTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    NUMBERS = "0123456789"
    OTHER_VARIABLE_CHARS = "_"
    SYMBOLS = "=-+[]{}():.,"
    KEYWORDS = ["for", "in", "def", "import", "from", "class", "return", "continue", "break", "if", "else", "elif"]

    def __init__(self, reader):
        debug = False
        self.reader = reader
        self.tokens = []
        self.current_token = None
        self.in_string_literal = False
        self.string_literal_start = None
        self.in_numerical_literal = False
        self.at_start_tabulation = True
        self.error = False
        self.in_variable_creation = False
        self.in_comment = False
        self.in_f_string = False
        self.f_string_level = 0
        self.sub_parser = None
        while not self.reader.isEOF():
            if debug:
                print(self.tokens)
            ch = self.reader.peek()
            if self.in_comment:
                if ch == "\n":
                    self.in_comment = False
                    continue
                self.reader.consume()
                continue
            if self.in_string_literal:
                if debug:
                    print("Parsing string literal")
                if ch == "\\":
                    slash = self.reader.consume()
                    next = self.reader.peek()
                    if next == self.string_literal_start:
                        self.current_token.append(next)
                        self.reader.consume()
                    self.current_token.append(slash)
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
            if self.in_f_string:
                if debug:
                    print("Parsing string literal")
                if ch == "{":
                    self.f_string_level += 1
                    if self.f_string_level == 1:
                        self.tokens.append(["string", "".join(self.current_token)])
                        self.current_token = None
                        self.sub_parser = []
                        self.tokens.append(["meta", "f-start"])
                        self.reader.consume()
                        continue
                if ch == "}":
                    self.f_string_level -= 1
                    if self.f_string_level == 0:
                        self.sub_parser = Lexer(MockReader(self.sub_parser))
                        self.tokens += self.sub_parser.tokens
                        self.sub_parser = None
                        self.current_token = []
                        self.tokens.append(["meta", "f-end"])
                        self.reader.consume()
                        continue
                if self.f_string_level > 0:
                    self.sub_parser.append(self.reader.consume())
                    continue
                if ch == "\\":
                    slash = self.reader.consume()
                    next = self.reader.peek()
                    if next == self.string_literal_start:
                        self.current_token.append(next)
                        self.reader.consume()
                    self.current_token.append(slash)
                    continue
                if ch == self.string_literal_start:
                    self.reader.consume()
                    self.tokens.append(["string", "".join(self.current_token)])
                    self.current_token = None
                    self.in_f_string = False
                    self.string_literal_start = None
                    continue
                self.current_token.append(self.reader.consume())
                continue
            if self.in_numerical_literal:
                if debug:
                    print("Parsing numerical literal")
                if ch in Lexer.NUMBERS:
                    self.current_token.append(self.reader.consume())
                    continue
                self.in_numerical_literal = False
                self.tokens.append(["number", "".join(self.current_token)])
                self.current_token = None
                continue
            if self.at_start_tabulation:
                if debug:
                    print("Parsing tabulation start")
                    print(ch)
                if ch == " ":
                    if debug:
                        print("was space")
                    if self.current_token is None:
                        self.current_token = [self.reader.consume()]
                        continue
                    self.current_token.append(self.reader.consume())
                    continue
                self.at_start_tabulation = False
                if self.current_token is None:
                    if len(self.tokens) > 0 and self.tokens[-1][0] == "tab":
                        self.tokens.pop()
                    self.tokens.append(["tab", 0])
                    continue
                if len(self.current_token) % 4 != 0:
                    if debug:
                        print(f"Error, unexpected indentation: {len(self.current_token)}")
                    self.error = True
                    break
                if len(self.tokens) > 0 and self.tokens[-1][0] == "tab":
                    self.tokens.pop()
                self.tokens.append(["tab", len(self.current_token) // 4])
                self.current_token = None
                continue
            if ch == "f":
                a = self.reader.peek(2)
                if len(a) == 2 and a[1] in "'\"":
                    self.in_f_string = True
                    self.tokens.append(["symbol", "f"])
                    self.string_literal_start = a[1]
                    self.reader.consume(2)
                    self.current_token = []
                    continue
            if ch == "#":
                self.in_comment = True
                continue
            if self.in_variable_creation:
                if debug:
                    print("Parsing variable creation")
                if ch in Lexer.LETTERS + Lexer.NUMBERS + Lexer.OTHER_VARIABLE_CHARS:
                    self.current_token.append(self.reader.consume())
                    continue
                self.in_variable_creation = False
                if "".join(self.current_token) in Lexer.KEYWORDS:
                    self.tokens.append(["keyword", "".join(self.current_token)])
                else:
                    self.tokens.append(["variable", "".join(self.current_token)])
                self.current_token = None
                continue
            if ch in Lexer.SYMBOLS:
                if debug:
                    print("Parsing special symbol")
                self.tokens.append(["symbol", self.reader.consume()])
                continue
            if ch == "\n":
                if debug:
                    print("Parsing new line")
                self.at_start_tabulation = True
                self.current_token = None
                self.reader.consume()
                continue
            if ch in "\"'":
                if debug:
                    print("Parsing string literal start")
                self.in_string_literal = True
                self.current_token = []
                self.string_literal_start = self.reader.consume()
                continue
            if ch in Lexer.NUMBERS:
                if debug:
                    print("Parsing numerical literal start")
                self.in_numerical_literal = True
                self.current_token = [self.reader.consume()]
                continue
            if ch in Lexer.LETTERS + Lexer.OTHER_VARIABLE_CHARS:
                if debug:
                    print("Parsing variable start")
                self.in_variable_creation = True
                self.current_token = [self.reader.consume()]
                continue
            if debug:
                print(f"Token '{self.reader.consume()}' has no meaning, skipping")
            else:
                self.reader.consume()
        if self.in_comment:
            pass
        elif self.in_string_literal:
            print("ERROR: Invalid syntax")
            # self.tokens.append(["string", "".join(self.current_token)])
        elif self.in_f_string:
            print("ERROR: Invalid syntax")
        elif self.in_numerical_literal:
            self.tokens.append(["number", "".join(self.current_token)])
        elif self.at_start_tabulation:
            pass
        elif self.in_variable_creation:
            if "".join(self.current_token) in Lexer.KEYWORDS:
                self.tokens.append(["keyword", "".join(self.current_token)])
            else:
                self.tokens.append(["variable", "".join(self.current_token)])
        for token in self.tokens:
            print(f"{token[0]} -> {token[1]}")
            # print(token)
        self.tokens = self.tokens[::-1]

    def peek(self, n=1):
        if n > len(self.tokens):
            print(f"Error, lexer has tokens {self.tokens[::-1]} left, that has length {len(self.tokens)}, but {n} characters were requested.")
            return self.tokens
        if n == 1:
            return self.tokens[-1]
        return self.tokens[-n:][::-1]

    def consume(self, n=1):
        if n > len(self.tokens):
            print(f"Error, lexer has tokens {self.tokens[::-1]} left, that has length {len(self.tokens)}, but {n} characters were requested.")
            return self.tokens
        end = self.tokens[-n:]
        self.tokens = self.tokens[:-n]
        if n == 1:
            return end[0]
        return end[::-1]

    def isEOF(self):
        return len(self.tokens) == 0

class Liner:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lines = []
        self.line = None
        while not self.lexer.isEOF():
            symbol = self.lexer.peek()
            if symbol[0] == "tab":
                if self.line is not None:
                    self.lines.append(self.line)
                    self.line = None
                self.line = [self.lexer.consume()]
                continue
            else:
                self.line.append(self.lexer.consume())
        self.lines.append(self.line)
        self.line = None
        [print(line) for line in self.lines]
        self.lines = self.lines[::-1]

    def peek(self, n=1):
        if n > len(self.lines):
            print(f"Error, liner has lines {self.lines[::-1]} left, that has length {len(self.lines)}, but {n} lines were requested.")
            return self.lines
        if n == 1:
            return self.lines[-1]
        return self.lines[-n:][::-1]

    def consume(self, n=1):
        if n > len(self.lines):
            print(f"Error, liner has lines {self.lines[::-1]} left, that has length {len(self.lines)}, but {n} lines were requested.")
            return self.lines
        end = self.lines[-n:]
        self.lines = self.lines[:-n]
        if n == 1:
            return end[0]
        return end[::-1]

    def isEOF(self):
        return len(self.lines) == 0

class LineParser:
    def __init__(self, liner):
        self.liner = liner
        self.lines = []
        self.errors = []
        print("")
        while not self.liner.isEOF():
            try_parse = self.parse_full_line(self.liner.consume())
            if try_parse[0]:
                self.lines.append(try_parse[1])
            else:
                self.errors.append(try_parse)
        [print(x) for x in self.lines]
        [print(x) for x in self.errors]
        # [print(line) for line in self.lines]

    # GRAMMAR RULES
    # basic <variable> {variable}
    # basic <tab>      {tab}

    # computation <variable> {variable}
    # computation <string> {string_literal}
    # computation <number> {number_literal}
    # computation <call> {computation}({comma_computations})
    # computation <dot_access> {computation}.{variable}
    # computation <index_access> {computation}[{computation}]

    # comma_computations <base> {computation}
    # comma_computations <next_computation> {computation}, {comma_computations}

    def separate_by_commas(self, variables):
        result = []
        nest_round = 0
        nest_square = 0
        nest_curly = 0
        current = []
        for variable in variables:
            if variable == ["symbol", "("]:
                nest_round += 1
            elif variable == ["symbol", ")"]:
                nest_round -= 1
            elif variable == ["symbol", "["]:
                nest_square += 1
            elif variable == ["symbol", "]"]:
                nest_square -= 1
            elif variable == ["symbol", "{"]:
                nest_curly += 1
            elif variable == ["symbol", "}"]:
                nest_curly -= 1

            if variable == ["symbol", ","] and nest_round == nest_square == nest_curly == 0:
                result.append(current)
                current = []
            else:
                current.append(variable)
        if current:
            result.append(current)
        return result

    # import_variable <base>     {variable}
    # import_variable <next_dot> {variable}.{import_variable}
    def parse_import_variable(self, import_variable):
        if len(import_variable) % 2 == 0:
            return False, import_variable
        for i, variable in enumerate(import_variable):
            if i % 2:
                if variable != ["symbol", "."]:
                    return False, import_variable
            else:
                if variable[0] != "variable":
                    return False, import_variable
        return True, [x[1] for x in import_variable[::2]]

    # comma_import_variable <base>          {import_variable}
    # comma_import_variable <next_variable> {import_variable}, {comma_import_variable}
    def parse_comma_import_variable(self, comma_import_variable):
        separated = self.separate_by_commas(comma_import_variable)
        result = []
        for var in separated:
            try_parse = self.parse_import_variable(var)
            if not try_parse[0]:
                return False, comma_import_variable
            result.append(try_parse[1])
        return True, result

    # function_variables <null>          _
    # function_variables <base>          {variable}
    # function_variables <next_variable> {variable}, {function_variables}
    def parse_function_variables(self, function_variables):
        return True, function_variables

    # assign_to <base>         {variable}
    # assign_to <dot_access>   {assign_to}.{variable}
    # assign_to <index_access> {assign_to}[{computation}]
    def parse_assign_to(self, assign_to):
        return True, assign_to

    # comma_assign_to <base>           {assign_to}
    # comma_assign_to <next_assign_to> {assign_to}, {comma_assign_to}
    def parse_comma_assign_to(self, comma_assign_to):
        separated = self.separate_by_commas(comma_assign_to)
        result = []
        for var in separated:
            try_parse = self.parse_assign_to(var)
            if not try_parse[0]:
                return False, comma_assign_to
            result.append(try_parse[1])
        return True, result

    def parse_comma_computations(self, comma_computations):
        return True, comma_computations

    # line <import>       import {comma_import_variable}
    # line <base_import>  from {import_variable} import {comma_import_variable}
    # line <function_def> def {variable}({function_variables}):
    # line <assigment>    {comma_assign_to} = {comma_computations} # enforce some additional checks here
    def parse_line(self, line):
        if line[0] == ["keyword", "import"]:
            try_parse = self.parse_comma_import_variable(line[1:])
            if try_parse[0]:
                return True, ["import", try_parse[1]]
        if line[0] == ["keyword", "def"] and line[1][0] == "variable" and line[2] == ["symbol", "("] and line[-1] == ["symbol", ":"] and line[-2] == ["symbol", ")"]:
            try_parse = self.parse_function_variables(line[3:-2])
            if try_parse[0]:
                return True, ["def", line[1][1], try_parse[1]]
        if ["symbol", "="] in line:
            i = line.index(["symbol", "="])
            try_parse_comma_assign_to = self.parse_comma_assign_to(line[:i])
            try_parse_comma_computations = self.parse_comma_computations(line[i + 1:])
            if try_parse_comma_assign_to[0] and try_parse_comma_computations[0]:
                return True, ["assign", try_parse_comma_assign_to[1], try_parse_comma_computations[1]]
        return False, line


    # full_line <base> {tab} {line}
    def parse_full_line(self, full_line):
        if full_line[0][0] == "tab":
            try_parse = self.parse_line(full_line[1:])
            if try_parse[0]:
                return True, [full_line[0][1], try_parse[1]]
        return False, full_line


if __name__ == '__main__':
    reader = FileReader("meta_runner.py")
    lexer = Lexer(reader)
    liner = Liner(lexer)
    lineparser = LineParser(liner)
