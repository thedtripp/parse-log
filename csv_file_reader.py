#!/usr/bin/env python3
"""
This module is able to outFor each data format, we need a function and converts the data to a common form. In this case, a list of tuples ('cookie', datetime.date(YYYY, M, D)).
put a list of the most active cookie given a timestamped list of cookies and a target date.

This module contains the CookieGetter class with all the methods needed to return 
the most active cookies for a given date. Though some default variables are provided
so the file can be run, this module is intended to be imported by the 
'most_active_cookie.py' file where the CookieGetter class is instantiated.



"""

from datetime import datetime
import logging
import sys
from typing import List, Tuple

# Default variables
LOG_FILE_NAME = "cookie_log.csv"


class CSVFileReader:
    def read_file_to_list(self, file_name: str) -> List[Tuple[str, datetime.date]]:
        """Read log file and return a List containing the entries as tuples ('cookie', datetime.date(YYYY, M, D)).

        Input string is the name of the log file. The log is read and converted to a
        List with each element representing a line of text from the file.
        Trailing whitespaces and the newline character are removed from the strings.
        For each cookie in the List, the cookie is included if the corresponding date is
        contained in the List of dates.  Else, the cookie is excluded from the output.
        Split the strings on ',' to separate cookie from datetime. Then split the datetime
        on 'T' to separate date from time. Use strptime() function to convert the parsed date
        to a datetime.date object for comparison with input dates.
        Function is resilient to malformed input data, skipping any such lines.
        """

        try:
            with open(file_name, "r") as log_file:
                result = []
                malformed_lines = 0
                for entry in log_file:
                    try:
                        cookie = entry.rstrip().split(",")[0]
                        timestamp_str = entry.rstrip().split(",")[1].split("T")[0]
                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d").date()
                        result.append((cookie, timestamp))
                    except (IndexError, ValueError, Exception):
                        malformed_lines += 1

                if malformed_lines > 0:
                    logging.warning(f"Log file contains invalid data. Skipped {malformed_lines} malformed line(s).")

                # if log file is empty, stop execution
                if not result:
                    logging.critical("Empty log file supplied. Nothing to do.")
                    sys.exit()
                else:
                    return result
        except FileNotFoundError:
            logging.critical(f"File: '{file_name}' not found. Please check the file name and try again.")
            sys.exit()


if __name__ == "__main__":
    """Driver code to run the program with default variables.

    This can be run for demonstration purposes but, this module is intended
    to be imported by the 'most_active_cookie.py' file where the CSVFileReader
    class is instantiated.  Events are logged to 'cookies.log'.
    """

    logging.basicConfig(
        filename="cookies.log",
        format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info("Start csv_file_reader.py")

    cfr = CSVFileReader()
    cookies = cfr.read_file_to_list(LOG_FILE_NAME)
    print(cookies)

    logging.info("End csv_file_reader.py")
