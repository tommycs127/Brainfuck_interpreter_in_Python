class Brainfuck:
    def __init__(self):
        self.__clean()
        
    '''
    The parameter
        "clean" indicates whether cleaning the cell before running the code;
        "printCell" indicates whether printing all cells after running the code.
    '''
    def run(self, s, clean=True, printCell=True):
        if (type(s) is not str): raise TypeError("{0} is {1}, not str".format(s, type(s)))
        if (type(clean) is not bool): raise TypeError("{0} is {1}, not bool".format(clean, type(clean)))
        if (type(printCell) is not bool): raise TypeError("{0} is {1}, not bool".format(printCell, type(printCell)))
        
        if (clean): self.__clean()
        
        s_loc = 0
        
        while (s_loc < len(s)):
            if (s[s_loc] == '['): self.__loopLoc.append([s_loc])
            elif (s[s_loc] == ']'): self.__insertLoopEnd(s_loc)
            s_loc += 1
        
        s_loc = 0
        
        while (s_loc < len(s)):
            if (s[s_loc] == '>'):
                if self.__ptr == len(self.__cell)-1: self.__cell.append(0)
                self.__ptr += 1
            elif (s[s_loc] == '<'):
                if self.__ptr-1 < 0: raise IndexError("Error @ {0} : index out of range".format(s_loc+1))
                self.__ptr -= 1
            elif (s[s_loc] == '+'):
                self.__cell[self.__ptr] += 1
            elif (s[s_loc] == '-'):
                self.__cell[self.__ptr] -= 1
            elif (s[s_loc] == '.'):
                print(chr(self.__cell[self.__ptr]), end='')
            elif (s[s_loc] == ','):
                self.__cell[self.__ptr] = ord((input() or '\0')[0])
            elif (s[s_loc] == '['):
                if self.__cell[self.__ptr] == 0: s_loc = self.__findLocation(s_loc)
            elif (s[s_loc] == ']'):
                if self.__cell[self.__ptr]: s_loc = self.__findLocation(s_loc)
            
            s_loc += 1
            
        if (printCell):
            print("{{ {0} }}".format(
                    ", ".join(
                        [
                            "[{0}]".format(self.__cell[i]) 
                            if i == self.__ptr else
                            "{0}".format(self.__cell[i])
                            for i in range(len(self.__cell))
                        ]
                    )
                )
            )
        
    def __insertLoopEnd(self, loc):
        if (type(loc) is not int): raise TypeError("{0} is {1}, not int".format(loc, type(loc)))
        for i in reversed(self.__loopLoc):
            if (len(i) == 1):
                i.append(loc)
                return None
        raise self.AsymmetryError("Error @ {0}: loop asymmetry".format(loc+1))
        
    def __findLocation(self, loc):
        for i in self.__loopLoc:
            if (loc in i):
                other = [item for item in i if item not in [loc]]
                if (len(other) == 1): return other.pop(0)
        raise self.AsymmetryError("Error @ {0}: loop asymmetry".format(loc+1))
        
    def __clean(self):
        self.__cell = [0]
        self.__ptr = 0
        
        '''
        Loop character location.
        Each element in the list is a list with two integers,
        indicating the location of '[' and ']'.
        '''
        self.__loopLoc = []
        
    class AsymmetryError(Exception):
        pass
