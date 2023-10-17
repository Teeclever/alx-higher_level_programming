# Python - Almost a circle

## Important Notes

I discovered that the `setUp` method in the test class runs in alphabetic order and not in the order that the test cases are defined. Also then running all the test files with `discover`, the test files are run in alphabetic order of their names after the `test_` prefix.

This is important in this particular project beause the `Rectangle` class has a private class attribute which is incremented with each instantiation of the class. That means we need to consider the order in which the objects are created for this class to properly track the `id` attrubite of each instance.
