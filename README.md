# pytona

pytona is a really simple way to profile Python functions.

You use the 'chronograph' decorator on a function and a profile file will be created
with the name of the function, or you can set the filename yourself.


## Installing from github

```console
pip install git+https://github.com/data-driven-detroit/pytona
```

## Example use

```python
from pytona import chronograph

@chronograph
def some_function_to_measure(important_argument):
    ... # code to measure


# This will save a 'some_function_to_measure.prof' file in the folder the script was ran from


@chronograph(filename='example.prof')
def function_to_measure(important_argument):
    ... # more code


# This will save a 'example.prof' file in the folder the script was ran from
```
