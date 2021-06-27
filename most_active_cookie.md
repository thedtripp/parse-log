# most_active_cookie module

A command line program to process a log file and return the most active cookie for a specified day.

How to use it:

$ python3 most_active_cookie.py cookie_log.csv -d 2018-12-09

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
