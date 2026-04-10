# Prog8 "command line" arguments

NOTE: This experimental version of my Prog8 [args](https://github.com/gillham/prog8libs/tree/main/args) 
library is designed for use with the Prog8 IR virtual machine.
It works the same when used from Prog8 but the arguments are passed differently.

This module will parse text passed in via the `args.buffer` array.  This array is inserted
into the program (`demo.p8ir` for example) via the `tools/p8ir.py` Python script.

The Python script reads the p8ir file looking for `args.buffer` and replaces the line *and*
overwrites the original p8ir.  If you won't want to do that for some reason then add a Makefile
step to copy your original p8ir and use `tools/p8ir.py` on the copy instead.

The script is looking for the `ubyte[81] args.buffer=...` line and rewrites it with the passed
in arguments.  If there are no arguments it doesn't rewrite the line.  And you probably don't
need this anyway. Once the p8ir is modified the Python scripts calls `prog8c -quiet -vm` to run
the program in the VM.

There is ongoing work to improve error handling and make sure newer features (like graphics) work
on the VM.

Passing arguments to the VM:
```
tools/p8ir.py build/demo.p8ir arg1 arg2 arg3 arg4 "arg5 is a string with spaces"
```

# Usage

You need to `%import args` and then call `args.parse()` before using `args.argc` or `args.argv`.
The call to `args.parse()` will return true if any arguments are found, otherwise false.

Example:
```Prog8
%import args
%import textio

main {
    sub start() {
        ubyte i = 0

        if args.parse() {
            txt.print("argc: ")
            txt.print_ub(args.argc)
            txt.nl()
            repeat args.argc {
                txt.print("argv: ")
                txt.print(args.argv[i])
                txt.nl()
                i++
            }
        }
    }
}
```
