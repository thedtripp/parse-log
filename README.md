<!-- parse-log documentation master file, created by
sphinx-quickstart on Sun Jun 27 00:02:14 2021. -->

# Welcome to parse-log’s documentation!

[![Build Status](https://travis-ci.com/thedtripp/parse-log.svg?branch=main)](https://travis-ci.com/github/thedtripp/parse-log)

## How to use it:

### Description:

* A command line program to process a log file and return the most active cookie for a specified day.

### Requirements:

* Python 3.6+

### Installation:

* Clone the repo
* ```$ git clone https://github.com/thedtripp/parse-log.git```
* Change directory into the cloned repo
* ```$ cd parse-log```
### Run:
#### unit tests
* ```$ python3 test_get_cookies.py```
#### main code file
Takes arguments for the ``log file`` to parse and a ``target date`` with a ``-d`` flag.
* ```$ python3 most_active_cookie.py cookie_log.csv -d 2018-12-08```


# Problem Statement

## Most Active Cookie

### Given a cookie log file in the following format:

```
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```

Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.

### Command:

```$ ./most_active_cookie cookie_log.csv -d 2018-12-09```

### Output:

```AtY0laUfhglK3lC7```


* We define the most active cookie as one seen in the log the most times during a given day.

### Assumptions:
* If multiple cookies meet that criteria, please return all of them on separate lines.

``` $ ./most_active_cookie cookie_log.csv -d 2018-12-08```
```
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```
* You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.
* You can assume -d parameter takes date in UTC time zone.
* You have enough memory to store the contents of the whole file.
* Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).

### We're looking for a concise, maintainable, extendable and correct solution. We're hoping you'll deliver your solution as production grade code and demonstrate:
* good testing practices,
* knowledge of build systems, testing frameworks, etc.
* clean coding practices (meaningful names, clean abstractions, etc.)

### Please use a programming language you’re very comfortable with. The next stage of the interview will involve extending your code.


# Modules

# most_active_cookie module

A command line program to process a log file and return the most active cookie for a specified day.

How to use it:

`$ python3 most_active_cookie.py cookie_log.csv -d 2018-12-09`

This program parses command line arguments for log file and date.  
It instantiates the CookieGetter class and calls its methods to
output the most active cookies on a given day.


### most_active_cookie.main()
Driver code to get most active cookie(s) given parameters specifed from command line.

Parse cli arguments for log file name and date. Instantiate CookieGetter class
and call its methods to output most active cookie given command line args.
Events are logged to ‘cookies.log’.


* **Return type**

    `None`


### most_active_cookie.parse_arguments()
Parse the log file name and date from the command line.

# get_cookies module

This module is able to output a list of the most active cookie given a timestamped list of cookies and a target date.

This module contains the CookieGetter class with all the methods needed to return 
the most active cookies for a given date. Though some default variables are provided
so the file can be run, this module is intended to be imported by the 
‘most_active_cookie.py’ file where the CookieGetter class is instantiated.


### class get_cookies.CookieGetter()
Bases: `object`

Output a list of the most active cookies given a timestamped cookie log file and a target date.


#### filter_list_on_dates(cookie_list, dates)
Return a List of all cookies that appear on the specified date(s).

Inputs:
A List of cookies and datetime formatted as: ‘cookie,YYYY-MM-DDThh:mm:ss:TZD’.  
A List of dates. Note: This may be a singleton List.

For each cookie in the List, the cookie is included if the corresponding date is 
contained in the List of dates.  Else, the cookie is excluded from the output.  
Split the strings on ‘,’ to separate cookie from datetime. Then split the datetime
on ‘T’ to separate date from time. Use strptime() function to convert the parsed date
to a datetime.date object for comparison with input dates. 
Function is resilient to malformed input data, skipping any such lines.


* **Return type**

    `List`[`str`]


#### get_cookie_frequencies(log)
Return a dict with each cookie and the number of times it occurs.

As input, take list of filtered cookie log entries.
Split each string on the comma in accordance with formatting.


* **Return type**

    `Dict`


#### get_max_value_in_dict(hashmap)
Return the maximum frequency given a dictionary of frequencies.

Input is a frequency hashmap as generated by get_cookie_frequencies().  
This function requires that all values in Dict be numerical.


* **Return type**

    `int`


#### get_most_active_cookies(cookie_list)
Return the most frequently occuring cookies given a list of cookies with frequencies.

Call the get_cookie_frequencies().  
Pass the result to get_max_value_in_dict().  
Return a list of cookies with frequencies equal to max_frequency.


* **Return type**

    `List`[`str`]


#### main(log_file, date_strings)
Given a cookie log file and a list of dates, output a list of the most active cookies on a specified date.

Convert date strings to datetime.date objects.  
Read log file and store each entry in a list.  
Reduce the list of cookies to cookies that occur on target date.  
Return the most common cookie(s) which occur on target date(s).  
In the event of FileNotFoundError, log an error message.


* **Return type**

    `List`[`str`]


#### print_list(list_)
Print elements of list on separate lines.


* **Return type**

    `None`


#### read_file_to_list(file_name)
Read log file and return a List containing the entries.

Input string is the name of the log file. The log is read and converted to a
List with each element representing a line of text from the file.  
Trailing whitespaces and the newline character are removed from the strings.


* **Return type**

    `List`[`str`]


#### string_to_date(date_string)
Convert a string to a datetime.date object.  Returns a datetime.date.

Input must be a string and a valid date in YYYY-MM-DD format.  
Includes some error handling in the event that the input is in wrong format
or is of wrong data type.  In either event, return type is None.


* **Return type**

    `datetime`


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
