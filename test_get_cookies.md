# test_get_cookies module

This file runs a suite of unit tests on the get_cookies module logging timestamped output in ‘tests.log’ file.


### class test_get_cookies.TestCookieGetter(methodName='runTest')
Bases: `unittest.case.TestCase`

This class has methods that run unit tests on the CookieGetter() class from the get_cookies module.


#### setUp()
Instantiate the CookieGetter() class.


#### classmethod setUpClass()
Set up logging for unit test.

During testing, events are logged in the ‘tests.log’ file in the following format:
YYYY-MM-DD hh:mm:ss,ms LOG-LEVEL MESSAGE 
Example:
2021-06-26 21:38:36,973 WARNING  Skipped 80 malformed line(s).  
In addition, the name of this testing file is logged.


#### classmethod tearDownClass()
Log exit message with a line break to separate successive runs of the program.


#### test_filter_list_on_dates()
Test test_filter_list_on_dates() function.

Function is tested in the following cases:
Test with no cookies and no dates
Expected output: an empty list.
Test with no cookies
Expected output: an empty list.
Test with no dates
Expected output: an empty list.
Regular test case with cookies and a date
Expected output: a list consisting of all cookies from the input list that occur on the specified date.


#### test_get_cookie_frequencies()
Test get_cookie_frequencies() function.

Function is tested in the following cases:
Nicely formatted cookies:
Expected output: a dict with cookies as keys and frequencies as values.
Malformed data:
Expected output: similar to well formatted file. Since the cookies are split
on commas, malformed data (specifically string with leading comma) won’t break 
the function but it can cause unwanted results such as empty strings in the dict.


#### test_get_max_value_in_dict()
Test test_get_max_value_in_dict() function.

Function is tested in the following cases:
Max value occurs one time in dict
Max value occurs multiple times in dict
All values are 0
Empty dict
In case of non int values, TypeError is raised.


#### test_get_most_active_cookies()
Test test_get_most_active_cookies() function.

Function is tested in the following cases:
Multiple most active cookies
Single most active cookie
Invalid date type raises an AttributeError.


#### test_main()
Test the entire program for correct output in various conditions.

Function is tested in the following cases:
Valid file, valid date
Valid file, valid date with no data
Invalid file raises FileNotFoundError.
Malformed data in file in include:
-Text file containing no valid timestamped cookies
-Empty text file
-File contining some valid data and invalid data processes the valid data.
-(Invalid lines are not processed but they are counted and logged.)
Valid file, no dates
Valid file, invalid date
Valid file, multiple invalid dates
Valid file, some invalid dates


#### test_read_file_to_list()
Test test_read_file_to_list() function.

Function is tested in the following cases:
Text file:
Expected output: list with each line of the file as an element in the list.
Empty file:
Expected output: an empty list.


#### test_string_to_date()
Test string_to_date() function.

The string_to_date() function is tested under the following conditions:
Valid dates:
A few valid dates are tested to verify correctness including edge cases like leap day (Feb 29)
Invalid dates:
Leap day on a non-leap year
The year 0
A string which is not a date
An expression which evaluates to an integer
