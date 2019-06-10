An example of using [`Gooey`](https://github.com/chriskiehl/Gooey) to generate a simple GUI frontend for a command line application using only two additional lines of code.  This is possible for scripts using the `argparse` module and only requires decorating `main` with `@Gooey` (and importing gooey).  Another example script uses the `GooeyParser` to take advantage of widgets for file/directory/date selection.  You can find more examples here:

https://github.com/chriskiehl/GooeyExamples

These examples provide a mock interface to an application that sends scheduled emails to coworkers.

# Installing
Follow instructions on the Gooey GitHub page.

```
pip install Gooey
``` 

NOTE: you will need X11 to run the GUI, which means that using Cygwin or WSL will not work.


## Version
```
>>> gooey.__version__
'1.0.2'
```

# Running

## Command Line Version

You can see how the command line version would be run if you comment out the `@Gooey` decorator on `main`.

```
python3 ./example_simple.py --name Matt --message "Your code is awesome!" --num-emails 5 --delay 2.0 --spacing 2.0
```

## Simple Example
`python3 example_simple.py`

![](screenshot-simple.png)

![](screenshot-simple-running.png)

![](screenshot-simple-complete.png)

## GooeyParser Example
`python3 example_gooey_parser.py`

![](screenshot-widget_example.png)
