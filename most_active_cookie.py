#!/usr/bin/env python3
"""A command line program to process a log file and return the most active cookie for a specified day.

How to use it:

$ python3 most_active_cookie.py cookie_log.csv -d 2018-12-09

This program parses command line arguments for log file and date.  
It instantiates the CookieGetter class and calls its methods to
output the most active cookies on a given day.  
"""

import argparse
import logging

from get_cookies import CookieGetter
from csv_file_reader import CSVFileReader


def parse_arguments():
    """Parse the log file name and date from the command line."""

    parser = argparse.ArgumentParser(
        description="MOST_ACTIVE_COOKIE: Given a timestamped list of cookies, return the most common cookie on a given date."
    )
    parser.add_argument("log_file_name", type=str, help="File to read. Comma-separated CSV expected.")
    parser.add_argument("-d", "--date", type=str, help="Date 'YYYY-MM-DD' to filter on.", required=True)
    return parser.parse_args()


def main() -> None:
    """Driver code to get most active cookie(s) given parameters specifed from command line.

    Parse cli arguments for log file name and date. Instantiate CookieGetter class
    and call its methods to output most active cookie given command line args.
    Events are logged to 'cookies.log'.
    """

    logging.basicConfig(
        format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler("cookies.log"), logging.StreamHandler()],
    )

    args = parse_arguments()
    LOG_FILE_NAME = args.log_file_name

    if args.date:
        DATE_STRINGS = [args.date]
        cg = CookieGetter()
        cfr = CSVFileReader()
        cookies_from_file = cfr.read_file_to_list(LOG_FILE_NAME)
        most_active_cookies = cg.main(cookies_from_file, DATE_STRINGS)
        cg.print_list(most_active_cookies)
    else:
        logging.critical("No date provied. Please supply a date in 'YYYY-MM-DD' format.")


if __name__ == "__main__":

    main()
