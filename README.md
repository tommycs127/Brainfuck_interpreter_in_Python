# Brainfuck interpreter in Python
An attempt to write a Brainfuck Interpreter in Python.

To use it, import it and create a Brainfuck() object. Then use the function .run() to interpret the Brainfuck code.
```
.run(code[, clean, printCell]) -> None

Interpret a Brainfuck code.

Parameters:
  "code" indicates the Brainfuck code. Must be a string;
  "clean" indicates whether cleaning the cell before running the code. Must be a boolean;
  "printCell" indicates whether printing all cells after running the code. Must be a boolean.
```

An example code using this interpreter is shown at [example.py](example.py).
