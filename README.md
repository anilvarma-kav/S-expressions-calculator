S-expression calculator
=======================
For full details on this problem refer to https://gist.github.com/rraval/2ef5e2ff228e022653db2055fc12ea9d


Requirements
=======================
1. Python3

How to run(MacOS or Linux)
=======================

**Step 1:** Make calc.py execultable

```
chmod +x calc.py
```

*NOTE : the above command assumes that the python3 is installed in the system and assuming you are in the directory where calc.py is located.*

**Step 2:** Add/change the shebang line(path to python3 interpretter) - Add it at the top of the script

```
#!/usr/bin/python3
```
*default shebang line for Python 3. modify it if your python 3 path is different* 

**Step 3:** run the command, remember program takes single argument which must be an S-expression

```
$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24
```

