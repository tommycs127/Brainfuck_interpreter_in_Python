class Brainfuck:

    def run(self, s):
        if type(s) is not str: raise TypeError("not str")
        
        cell = [0]
        ptr = 0
        s_loc = 0 # Location of the string 's'
        depth = [] # List of while loop command's location
        
        while(s_loc < len(s)):
            if s[s_loc] == ">":
                if ptr == len(cell)-1: cell.append(0)
                ptr += 1
            elif s[s_loc] == "<":
                if ptr-1 < 0: raise IndexError("Error @ {0} : index out of range".format(s_loc+1))
                ptr -= 1
            elif s[s_loc] == "+":
                cell[ptr] += 1
            elif s[s_loc] == "-":
                cell[ptr] -= 1
            elif s[s_loc] == ".":
                print(chr(cell[ptr]), end="")
            elif s[s_loc] == ",":
                cell[ptr] = ord((input() or "\0")[0])
            elif s[s_loc] == "[":
                temp = depth.copy()
                depth.append(s_loc)
                try:
                    if cell[ptr] == 0:
                        s_loc += 1
                        while(temp != depth):
                            if s[s_loc] == "[":
                                depth.append(s_loc)
                            elif s[s_loc] == "]":
                                if len(depth)-1 == len(temp): s_loc -= 1
                                del depth[-1]
                            s_loc += 1
                except:
                    raise IndexError("Error @ {0} : loop asymmetry".format(s_loc+1))
            elif s[s_loc] == "]":
                try:
                    if cell[ptr]:
                        s_loc = depth[-1] - 1
                    del depth[-1]
                except:
                    raise IndexError("Error @ {0} : loop asymmetry".format(s_loc+1))
            s_loc += 1
        
        print(", ".join(["[{0}]".format(cell[i]) if i == ptr else "{0}".format(cell[i]) for i in range(len(cell))]))
        
try:
    bf = Brainfuck()
    bf.run("Your Brainfuck code here")
except Exception as e: print(e)
