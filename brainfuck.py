# Python 3.3+

class Brainfuck(object):
    def __init__(self, cells_length=100):
        self.__data_pointer = 0
        self.__instruc_pointer = 0
        self.code = ''
        
        self.cells_length = cells_length
        self.__cells = [0] * cells_length
        
        self.__bracket_lookup = dict()
        self.__bracket_ignore = list()
        
        self.__commands = dict()
        self.__register_commands()
        
    def __register_commands(self):
        self.__commands['>'] = self.__increment_data_pointer
        self.__commands['<'] = self.__decrement_data_pointer
        self.__commands['+'] = self.__increment_byte
        self.__commands['-'] = self.__decrement_byte
        self.__commands[','] = self.__input
        self.__commands['.'] = self.__output
        self.__commands['['] = self.__while
        self.__commands[']'] = self.__while_end
        self.__commands['@'] = self.__print_data_pointer  # Register your own command here
        
    # Command >
    def __increment_data_pointer(self):
        if (self.__data_pointer + 1) < self.cells_length:
            self.__data_pointer += 1
        else:
            raise MemoryError('Out of bounds')
        self.__instruc_pointer += 1
    
    # Command <
    def __decrement_data_pointer(self):
        if (self.__data_pointer - 1) >= 0:
            self.__data_pointer -= 1
        else:
            raise MemoryError('Out of bounds')
        self.__instruc_pointer += 1
    
    # Command +
    def __increment_byte(self):
        self.__cells[self.__data_pointer] += 1
        self.__instruc_pointer += 1
    
    # Command -
    def __decrement_byte(self):
        self.__cells[self.__data_pointer] -= 1
        self.__instruc_pointer += 1
    
    # Command ,
    def __input(self):
        self.__cells[self.__data_pointer] = ord(input()[:1] or '\0')
        self.__instruc_pointer += 1
    
    # Command .
    def __output(self):
        print(chr(self.__cells[self.__data_pointer]), end='')
        self.__instruc_pointer += 1
    
    # Command [
    def __while(self):
        if self.__should_ignore(self.__instruc_pointer):
            self.__instruc_pointer += 1
            return
        if self.__cells[self.__data_pointer] == 0:
            self.__instruc_pointer = self.__bracket_lookup[self.__instruc_pointer]
        else:
            self.__instruc_pointer += 1
    
    # Command ]
    def __while_end(self):
        if self.__should_ignore(self.__instruc_pointer):
            self.__instruc_pointer += 1
            return
        if self.__cells[self.__data_pointer] != 0:
            self.__instruc_pointer = self.__bracket_lookup[self.__instruc_pointer]
        else:
            self.__instruc_pointer += 1
            
    # Command @ - Just an example to show that you can create your own command
    def __print_data_pointer(self):
        print(f'The data pointer is at {self.__data_pointer}.')
        self.__instruc_pointer += 1
            
    # Skip if not command
    def __skip(self):
        self.__instruc_pointer += 1
        
    def __execute(self, symbol):
        self.__commands.get(symbol, self.__skip)()
        
    def __should_ignore(self, pos):
        return pos in self.__bracket_ignore
    
    def __get_parentheses(self, code):
        parentheses_start = []
        
        for instruc_pointer in range(len(code)):
            if code[instruc_pointer] == '[':
                parentheses_start.append(instruc_pointer)
            elif code[instruc_pointer] == ']':
                if len(parentheses_start) > 0:
                    parentheses = parentheses_start.pop()
                    self.__bracket_lookup[parentheses] = instruc_pointer
                    self.__bracket_lookup[instruc_pointer] = parentheses
                else:
                    self.__bracket_ignore.append(instruc_pointer)
        
        self.__bracket_ignore += parentheses_start.copy()
        self.__bracket_ignore.sort()
        
    def print_cells(self):
        print('[', end='')
        for i in range(len(self.__cells)):
            if i != self.__data_pointer:
                print(self.__cells[i], end='' if i + 1 == len(self.__cells) else ', ')
            else:
                print(f'({self.__cells[i]})', end='' if i + 1 == len(self.__cells) else ', ')
        print(']')
        
    def check_code(self, code=None):
        if code is None:
            code = self.code
    
        self.__bracket_lookup.clear()
        self.__bracket_ignore.clear()
        
        self.__get_parentheses(code)
        for pos in self.__bracket_ignore:
            print(f'Warning: unmatched parentheses at position {pos}.')
    
    def run(self, code=None):
        if code is None:
            code = self.code
            
        self.check_code(code)
            
        self.__instruc_pointer = 0
        while self.__instruc_pointer < len(code):
            self.__execute(code[self.__instruc_pointer])
        
        if '.' in code:
            print()
