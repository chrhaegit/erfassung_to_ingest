# Python snippets

## modules

- A module is a file containing Python definitions and statements.
- The file name is the module name with the suffix .py appended
- Within a module, the module’s name (as a string) is available as the value of the global variable ```__name__```
- To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name *module.version.pyc*, where the version encodes the format of the compiled file; it generally contains the Python version number.

## use file as script and importable module

- if you run `python fibo.py <arguments>` the code in the module will be executed, just as if you imported it, but with the `__name__` set to "`__main__`".
- That means that by adding the following code at the end of your module, the file is usable as a script as well as an importable module:
  
```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

## packages

- Packages are a way of structuring Python’s module namespace by using “dotted module names”.
- When importing the package, Python searches through the directories on `sys.path` looking for the package subdirectory.
- The `__init__.py` files are required to make Python treat directories containing the file as packages (unless using a namespace package, a relatively advanced feature). This prevents directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable, described later.

## import

- The `__init__.py` file is executed as soon as the package is imported somewhere

## python setup tools

run in project directory:

- What is a wheel? Packages binary version of te code. `pip install wheel` need first!

## unittests

- `python -m unittest discover -s ".\test" -p "test*.py"`

## create virtual env

```> python -m venv .env```

### Activate virtual environment

- in VSCode: Ctrl/Shift/P
- click on select interpreter
- choose your newly created virtual environment (will be remembered, for all code in projec)
- or: `.venv/bin/activate`
  
### pip

```shell
# intall packages, e.g.:nopenpyxl
> pip install openpyxl

# creating requirements.txt
> pip freeze requirements.txt

#installing from a requirements.txt
> pip install -r requirements.txt 

# show installed packages
> pip list
```

## Object Orientation in python

### do validation with 'assert'

```python
class Lesson(self, price:int):
    # if price <= 0 an AssertionError will be raised with the given message
    assert price > 0, f"price should be > 0!" 
    self.price = price
```

### class variables & methods

if you access a class variable by an instance of the class its working, because it looks up the class if the variable is not found as a member variable.

for class methods, use the @classmethod decorator. --> an Class type object is first paramter f(cls)
for static methods, use the #staticmethod decorator. No additional object is given as first parameter.

### magic attributes

```python
le = Lesson(25)
le.__dict__
Lesson.__dict__
```
