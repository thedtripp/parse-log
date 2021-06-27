import argparse
import datetime
import logging
from typing import List
from get_cookies import CookieGetter
from get_cookies_extended import CookieGetterExtended

def parse_arguments():
    parser = argparse.ArgumentParser(description="MOST_ACTIVE_COOKIE: Given a timestamped list of cookies, return the most common cookie on a given date. If no date specified, use current date.")
    parser.add_argument("log_file_name", type=str, help="File to read. Comma-separated CSV expected.")
    parser.add_argument("-f", "--frequencies", action='store_true', help="Display cookie frequencies.")
    date_args = parser.add_mutually_exclusive_group()
    date_args.add_argument("-d", "--date", type=str, help="Date 'YYYY-MM-DD' to filter on.")
    date_args.add_argument("-r", "--date-range", type=str, help="Comma-separated date range 'YYYY-MM-DD,YYYY-MM-DD' to filter on.")
    date_args.add_argument("-l", "--date-list", type=str, help="Comma-separated date list 'YYYY-MM-DD,YYYY-MM-DD,...' to filter on.")
    return parser.parse_args()

def parse_date_range(date_range_string: str) -> List[str]:
    dates = []
    try:
        cg = CookieGetter()
        date_str_1, date_str_2 = date_range_string.split(',')
        date_1 = cg.string_to_date(date_str_1)
        date_2 = cg.string_to_date(date_str_2)
        start = min(date_1, date_2)
        end = max(date_1, date_2)
        delta = end - start
        for i in range(delta.days + 1):
            dates.append(str(start + datetime.timedelta(i)))
        return dates
    except ValueError:
        logging.error(f"Invalid date range: '{date_range_string}'. -r option takes a comma-separated date range 'YYYY-MM-DD,YYYY-MM-DD'.")
        print(f"Invalid date range: '{date_range_string}'. -r option takes a comma-separated date range 'YYYY-MM-DD,YYYY-MM-DD'.")

def parse_date_list(date_list_string: str) -> List[str]:
    return date_list_string.split(',')

def main() -> None:
    #logging.basicConfig(filename="cookie.log", format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.basicConfig(filename="cookie.log", 
        format='%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    args = parse_arguments()
    LOG_FILE_NAME = args.log_file_name
    SHOW_FREQUENCIES = args.frequencies

    if args.date:
        DATE_STRINGS = [args.date]
    elif args.date_range:
        DATE_STRINGS = parse_date_range(args.date_range)
    elif args.date_list:
        DATE_STRINGS = parse_date_list(args.date_list)
    # No date provided, use today as default date
    # No date provided, use any date
    else:
        DATE_STRINGS = None

    cge = CookieGetterExtended()
    # No date provided, use any date
    if not DATE_STRINGS:
        most_active_cookies = cge.most_active_cookie_all_dates(LOG_FILE_NAME, SHOW_FREQUENCIES)
        least_active_cookies = cge.least_active_cookie_all_dates(LOG_FILE_NAME, SHOW_FREQUENCIES)
    else:
        most_active_cookies = cge.most_active_cookie_from_date_list(LOG_FILE_NAME, DATE_STRINGS, SHOW_FREQUENCIES)
        least_active_cookies = cge.least_active_cookie_from_date_list(LOG_FILE_NAME, DATE_STRINGS, SHOW_FREQUENCIES)

    print("MOST ACTIVE COOKIES:")
    cge.print_list(most_active_cookies)
    print()
    print("LEAST ACTIVE COOKIES:")
    cge.print_list(least_active_cookies)
    logging.info("Exiting\n" + "-"*70)


if __name__ == "__main__":
    main()