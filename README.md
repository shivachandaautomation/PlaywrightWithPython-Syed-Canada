# PlaywrightWithPython-Syed-Canada

Beginner-friendly Python practice examples organized by learning day. The current
examples introduce basic Python values and data types, then explore strings,
dictionaries, sets, and tuples.

## Project structure

```text
.
├── Day2/
│   └── intro.py              # Basic Python statements and output
├── Day3/
│   └── datatypes.py          # Examples of Python data types
└── Day5/
    ├── dictionary.py         # Creating and using dictionaries
    ├── python_strings.py     # String indexing, slicing, and methods
    └── set_tuple_etc.py      # Set operations and tuple examples
```

## Requirements

- Python 3
- No third-party packages are required

## Run an example

Open a terminal in the project folder and run a script with Python:

```powershell
python Day2/intro.py
python Day3/datatypes.py
python Day5/dictionary.py
python Day5/python_strings.py
python Day5/set_tuple_etc.py
```

Each script is standalone and prints its examples to the terminal. Run one at a
time to focus on that topic.

## Topics covered

- **Basics and data types:** integers, floats, complex numbers, strings,
  booleans, lists, sets, and dictionaries
- **Strings:** indexing, slicing, case conversion, searching, splitting,
  joining, replacement, formatting, and checks such as `isalpha()`
- **Dictionaries:** reading, adding, updating, and removing key-value pairs;
  dictionary views; nested dictionaries; membership checks
- **Sets:** adding and removing items, set comparisons and operations, copying,
  and removing duplicates from a list
- **Tuples:** `count()` and `index()`, indexing, slicing, concatenation,
  repetition, and conversion from a list

## Looping through a dictionary

Use `.items()` to access each key and value together:

```python
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
}

for key, value in student.items():
    print(key, "is", value)
```

Output:

```text
name is Alice
age is 21
course is Computer Science
```

You can also loop over just the keys with `student.keys()` or just the values
with `student.values()`. Dictionary keys are unique, so assigning a value to
the same key again replaces its earlier value.
