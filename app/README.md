flask-test-kata
===============

CREDIT: https://github.com/plain-vanilla-games/flask-test-kata

This is a python testing kata for a simple Flask web "service".

This project has the following skeleton:

```
app
├── calculator
│   ├── __init__.py
│   ├── app.py
│   ├── logic.py
│   └── templates
│       └── index.html
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── base.py
    ├── integration
    |   ├── __init__.py
    |   └── test_views.py
    └── unit
        ├── __init__.py
        └── test_logic.py
```
The tasks at hand:

Unit Tests
----------

1. Implement `test_mul` unit test for the multiply method in `logic.Calculator`,
   then flesh out `logic.Calculator.mul` until test passes.

2. `test_mul` as a test is rather coarse. A better test would be in the form
   `test_function_satisfies_condition_after_pre-condition`. Implement the tests
   `test_mul_with_two_positive_numbers`, `test_mul_with_two_negative_numbers`,
   `test_mul_with_one_negative_one_positive_number`.

3. The constructor of `logic.Calculator` takes two arguments `min_value` and
   `max_value`. Change the class so that it's methods throw the exceptions
   in `logic.py` when confronted with numbers that are too high or too low.

4. Make sure to add tests to check the boundary of `min_value` and `max_value`.

5. `logic.Calculator` contains another method stub: `div`. This method should
   divide `a` by `b`, but it is just a stub now. Write corresponding tests for
   the method, as you've written for `logic.Calculator.mul`, then implement
   the method to pass your tests.

6. Division has more caveats than multiplication. Python will raise an exception
   of type ZeroDivisionError when you attempt to divide by zero, write a test
   asserts that your Calculator class does not suppress them.


The preferred way of testing whether exceptions are raised is to use
```
with pytest.raises(MyException):
    code...
```



Integration Tests
-----------------

1. If by now the multiplication logic has been correctly implemented,
   the `test_multiply` integration test should be passing.
   Implement integration tests which verify the responses for valid
   and invalid inputs (think about the boundaries of max and min values).

2. Write corresponding integration tests for the `/div` view

3. Make sure that for requests that attempt to divide by zero that the
   calculator app returns an appropriate 403 response.

