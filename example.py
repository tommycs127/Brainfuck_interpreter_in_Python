import brainfuck

bf = brainfuck.Brainfuck()

'''
If you don't want to use the prefix "brainfuck.",
change "import brainfuck" to "from brainfuck import *".
'''

# Should print "Hello world!" and all cells after running the code
bf.run("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.")
print()

# Should print "All cells should not be printed in the next line after running this code."
bf.run(
    "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-----.>++++++++..<<++.>>---------.++.+++++++..+++++++.<<.>>.-----------.+++++++.++++++.---------.--------.<<.>>++++++++++.+.+++++.<<.>>------------------.+++.<<.>>+++++++++++.++.---------.+++++.++++++.---------------.-.<<.>>+++++.+++++.<<.>>++++++.------------.---.<<.>>+++++++++.---------.+++++++++++++++++++.----.<<.>>--------.---.+++++.---------.<<.>>----.+++++.++++++++++++++.---------------.+++++++++++++.<<.>>.+++.-------..-----.+++++.-------.<<.>>+++++++++++++.------------.+.++++++++++.<<.>>----------------.++++++++++++.-----------.+.<<++++++++++++++.",
    printCell = False
)
print()

# Should print "{ [3] }" and then "{ [6] }" because cells are not cleaned before running the second code.
bf.run("+++")
bf.run("+++", clean = False)
