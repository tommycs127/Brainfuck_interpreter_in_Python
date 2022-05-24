import brainfuck

bf = brainfuck.Brainfuck(cells_length=10)
# A program that prints "Hello world!\n"
bf.code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
bf.run()
bf.print_cells()

bf = brainfuck.Brainfuck(cells_length=10)
bf.code = '+++++>++<[->+<]]'  # Notice the unmatched parentheses
bf.run()  # Will show a warning about unmatched parentheses before run
bf.print_cells()
