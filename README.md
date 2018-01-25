# Reverse Sentence in Python
In this assignment, you'll design and implement one of the string manipulation functions that is commonly asked during interviews.

## Exercise
* Design and implement a function to reverse the order of words in a sentence. For example, if the function is called with input of "Yoda&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;&nbsp;&nbsp;awesome", the function should return a string object with the value "awesome&nbsp;&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;&nbsp;Yoda". Note that the whitespace between words is preserved.
* Share and explain the time and space complexities for your solution.
* At minimum, your implementation should pass the basic tests.

## Python Considerations
The Ruby version of this assignment involved reversing the order of words in a sentence in place. Unlike Ruby strings, Python strings are immutable, which means they can't be changed after they are initialized. Because strings cannot be modified in place, a new string must be created whenever a change must be made to a string.

**Note**: Do not use Python provided functionality for `reversed()`, `reverse()`, or string slicing (`"string"[::-1]`). You may use `len()`.

## Running the Tests
Install `pytest`
```terminal
pip install pytest
```
To run all tests, navigate to the same directory as the test file and run:
```terminal
pytest test_reverse_sentence.py
```
Alternatively, to exit instantly on first error or failed test, run:
```terminal
pytest -x test_reverse_sentence.py
```

See [pytest documentation](http://pytest.org/latest/) for more information about `pytest`.
