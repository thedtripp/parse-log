#!/usr/bin/env python3
"""This module is able to output a list of the most active cookie given a timestamped list of cookies and a target date.

This module contains the CookieGetter class with all the methods needed to return 
the most active cookies for a given date. Though some default variables are provided
so the file can be run, this module is intended to be imported by the 
'most_active_cookie.py' file where the CookieGetter class is instantiated.
"""

from datetime import datetime
import logging
import sys
from typing import List, Dict

# Default variables
DATE_STRINGS = ["2018-12-08"]
LOG_FILE_NAME = "cookie_log.csv"

class CookieGetter():
    """Output a list of the most active cookies given a timestamped cookie log file and a target date."""

    def string_to_date(self, date_string: str) -> datetime:
        """Convert a string to a datetime.date object.  Returns a datetime.date.  
        
        Input must be a string and a valid date in YYYY-MM-DD format.  
        Includes some error handling in the event that the input is in wrong format
        or is of wrong data type.  In either event, return type is None.
        """

        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except Exception:
            logging.warning(f"Error: Invalid date '{date_string}'. Please use 'YYYY-MM-DD' format.")

    def read_file_to_list(self, file_name: str) -> List[str]:
        """Read log file and return a List containing the entries.  

        Input string is the name of the log file. The log is read and converted to a
        List with each element representing a line of text from the file.  
        Trailing whitespaces and the newline character are removed from the strings.
        """

        try:
            with open(file_name, "r") as log_file:
                result = [entry.rstrip() for entry in log_file]
                # if log file is empty, stop execution
                if not result:
                    logging.critical("Empty log file supplied. Nothing to do.")
                    sys.exit()
                else:
                    return result
        except FileNotFoundError:
            logging.critical(f"File: '{file_name}' not found. Please check the file name and try again.")
            sys.exit()

    def filter_list_on_dates(self, cookie_list: List[str], dates: List[datetime]) -> List[str]:
        """Return a List of all cookies that appear on the specified date(s).  

        Inputs:
            A List of cookies and datetime formatted as: 'cookie,YYYY-MM-DDThh:mm:ss:TZD'.  
            A List of dates. Note: This may be a singleton List.  
        For each cookie in the List, the cookie is included if the corresponding date is 
        contained in the List of dates.  Else, the cookie is excluded from the output.  
        Split the strings on ',' to separate cookie from datetime. Then split the datetime
        on 'T' to separate date from time. Use strptime() function to convert the parsed date
        to a datetime.date object for comparison with input dates. 
        Function is resilient to malformed input data, skipping any such lines. 
        """
        filtered_cookie_list = []
        malformed_lines = 0

        for cookie_entry in cookie_list:
            try:
                # Isolate the date portion of the log entry string
                cookie = cookie_entry.split(',')[0]
                log_date_string = cookie_entry.split(',')[1].split('T')[0]
                # Convert the date string to datetime.date object
                log_date = datetime.strptime(log_date_string, "%Y-%m-%d").date()
                if log_date in dates:
                    filtered_cookie_list.append(cookie)
            except (ValueError, IndexError, Exception):
                malformed_lines += 1

        if malformed_lines > 0:
            logging.warning(f"Log file contains invalid data. Skipped {malformed_lines} malformed line(s).")

        # If resulting list is empty, there are no cookies on the specified date. Nothing to do.
        if not filtered_cookie_list:
            logging.critical(f"No cookies found on date: {dates}. Exiting")
            sys.exit()
        else:
            return filtered_cookie_list

    def get_most_active_cookies(self, cookie_list: List[str]) -> List[str]:
        """Return the most frequently occuring cookies given a list of cookies with frequencies.  

        Call the get_cookie_frequencies().  
        Pass the result to get_max_value_in_dict().  
        Return a list of cookies with frequencies equal to max_frequency.  
        """

        cookie_frequency = self.get_cookie_frequencies(cookie_list)
        max_frequency = self.get_max_value_in_dict(cookie_frequency)
        most_common_cookie_list = [cookie for cookie in cookie_frequency.keys() if cookie_frequency[cookie] == max_frequency]
        return most_common_cookie_list

    def get_max_value_in_dict(self, hashmap: Dict) -> int:
        """Return the maximum frequency given a dictionary of frequencies.  
        
        Input is a frequency hashmap as generated by get_cookie_frequencies().  
        This function requires that all values in Dict be numerical.
        """

        try:
            max_value = 0
            for key in hashmap.keys():
                if hashmap[key] > max_value:
                    max_value = hashmap[key]
            return max_value
        except Exception:
            logging.critical(f"There is a problem with the dictionary '{hashmap}'. Keys are strings, values are integers.")
            sys.exit()

    def get_cookie_frequencies(self, log: List[str]) -> Dict:
        """Return a dict with each cookie and the number of times it occurs.  
        
        As input, take list of filtered cookie log entries.
        Split each string on the comma in accordance with formatting.
        """

        cookie_frequency = {}
        for line in log:
            #parse cookie from entries in log
            log_entry = line.split(',')
            cookie = log_entry[0]

            if cookie in cookie_frequency.keys():
                cookie_frequency[cookie] += 1
            else:
                cookie_frequency[cookie] = 1
        return cookie_frequency

    def print_list(self, list_: List) -> None:
        """Print elements of list on separate lines.  """

        for element in list_:
            print(element)
    
    def main(self, log_file: str, date_strings: List[str]) -> List[str]:
        """Given a cookie log file and a list of dates, output a list of the most active cookies on a specified date.  
        
        Convert date strings to datetime.date objects.  
        Read log file and store each entry in a list.  
        Reduce the list of cookies to cookies that occur on target date.  
        Return the most common cookie(s) which occur on target date(s).  
        In the event of FileNotFoundError, log an error message.  
        """

        logging.basicConfig(
            format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler("cookies.log"),
                logging.StreamHandler()
            ]
        )

        try:
            dates = [self.string_to_date(date_string) for date_string in date_strings]
            # Check if all dates are None. If so, stop execution because there are no valid dates.  
            if all(date is None for date in dates):
                logging.critical("No valid date given. Please enter date in 'YYYY-MM-DD' format. Exit.")
                sys.exit()
            log_file_as_list = self.read_file_to_list(log_file)
            cookies_on_date = self.filter_list_on_dates(log_file_as_list, dates)
            most_active_cookies_on_date = self.get_most_active_cookies(cookies_on_date)
            return most_active_cookies_on_date
        except FileNotFoundError as err:
            logging.critical(f"File: '{log_file}' not found. Please check the file name and try again. Exiting.")
            sys.exit()
            

if __name__ == '__main__':
    """Driver code to run the program with default variables.

    This can me run for demonstration purposes but, this module is intended 
    to be imported by the 'most_active_cookie.py' file where the CookieGetter 
    class is instantiated.  Events are logged to 'cookies.log'.  
    """

    logging.basicConfig(filename="cookies.log", 
        format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S")
        
    logging.info("Start get_cookies.py")

    cg = CookieGetter()
    cookies = cg.main(LOG_FILE_NAME, DATE_STRINGS)
    cg.print_list(cookies)

    logging.info("End get_cookies.py")