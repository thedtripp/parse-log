import argparse
import datetime
import logging
from typing import List
from get_cookies import CookieGetter

def parse_arguments():
    parser = argparse.ArgumentParser(description="MOST_ACTIVE_COOKIE: Given a timestamped list of cookies, return the most common cookie on a given date. If no date specified, use current date.")
    parser.add_argument("log_file_name", type=str, help="File to read. Comma-separated CSV expected.")
    parser.add_argument("-d", "--date", type=str, help="Date 'YYYY-MM-DD' to filter on.", required=True)
    return parser.parse_args()

def main() -> None:
    logging.basicConfig(filename="cookie.log", 
        format='%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    args = parse_arguments()
    LOG_FILE_NAME = args.log_file_name

    if args.date:
        DATE_STRINGS = [args.date]
    else:
        DATE_STRINGS = None

    cg = CookieGetter()
    if DATE_STRINGS:
        most_active_cookies = cg.main(LOG_FILE_NAME, DATE_STRINGS)
        cg.print_list(most_active_cookies)
    # No date provided, use any date
    else:
        logging.critical("No date provied. Please supply a date in YYYY-MM-DD format.")
    logging.info("Exiting\n" + "-"*70)

if __name__ == "__main__":
    main()