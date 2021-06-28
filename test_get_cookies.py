#!/usr/bin/env python3
"""This file runs a suite of unit tests on the get_cookies module logging timestamped output in 'tests.log' file.  """

import datetime
import logging
import unittest

from get_cookies import CookieGetter


class TestCookieGetter(unittest.TestCase):
    """This class has methods that run unit tests on the CookieGetter() class from the get_cookies module.  """

    @classmethod
    def setUpClass(cls):
        """Set up logging for unit test. 
        
        During testing, events are logged in the 'tests.log' file in the following format:
        YYYY-MM-DD hh:mm:ss,ms LOG-LEVEL MESSAGE 
        Example:
        2021-06-26 21:38:36,973 WARNING  Skipped 80 malformed line(s).  
        In addition, the name of this testing file is logged.  
        """

        logging.basicConfig(filename="tests.log", 
            format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S")
        logging.info("test_get_cookies.py")

    @classmethod
    def tearDownClass(cls):
        """Log exit message with a line break to separate successive runs of the program.  """

        logging.info("Tests complete. Exiting\n" + "-"*70)

    def setUp(self):
        """Instantiate the CookieGetter() class.  """
        
        self.cookie_getter = CookieGetter()

    def test_string_to_date(self):
        """Test string_to_date() function.  
        
        The string_to_date() function is tested under the following conditions:
        Valid dates:
            A few valid dates are tested to verify correctness including edge cases like leap day (Feb 29)
        Invalid dates:
            Leap day on a non-leap year
            The year 0
            A string which is not a date
            An expression which evaluates to an integer
        """
        # Valid Dates
        self.assertEqual(self.cookie_getter.string_to_date("2018-12-08"), datetime.date(2018, 12, 8))
        self.assertEqual(self.cookie_getter.string_to_date("2020-02-29"), datetime.date(2020, 2, 29))
        self.assertEqual(self.cookie_getter.string_to_date("0001-01-01"), datetime.date(1, 1, 1))
        # Invalid Dates
        self.assertEqual(self.cookie_getter.string_to_date("2019-02-29"), None)
        self.assertEqual(self.cookie_getter.string_to_date("0000-01-01"), None)
        self.assertEqual(self.cookie_getter.string_to_date("garbage string"), None)
        self.assertEqual(self.cookie_getter.string_to_date(20200-229), None)

    def test_read_file_to_list(self):
        """Test test_read_file_to_list() function.  
        
        Function is tested in the following cases:
        Text file:
            Expected output: list with each line of the file as an element in the list.
        Empty file:
            Expected output: an empty list.
        """

        self.assertEqual(
            self.cookie_getter.read_file_to_list("cookie_log.csv"),         
            [
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"
            ]
        )
        with self.assertRaises(SystemExit):
            self.cookie_getter.read_file_to_list("./test_files/empty_file.txt")

    def test_filter_list_on_dates(self):
        """Test test_filter_list_on_dates() function.  
        
        Function is tested in the following cases:
        Test with no cookies and no dates
            Expected output: an empty list.
        Test with no cookies
            Expected output: an empty list.
        Test with no dates
            Expected output: an empty list.
        Regular test case with cookies and a date
            Expected output: a list consisting of all cookies from the input list that occur on the specified date.
        """

        # Test with no cookies and no dates.
        with self.assertRaises(SystemExit):
            self.cookie_getter.filter_list_on_dates([], [])
        # Test with no cookies.
        with self.assertRaises(SystemExit):
            self.cookie_getter.filter_list_on_dates([], [datetime.date(2018, 12, 8)])
        # Test with no dates.
        with self.assertRaises(SystemExit):
            self.cookie_getter.filter_list_on_dates(self.cookie_getter.read_file_to_list("cookie_log.csv"), [])
        # Regular test case with cookies and a date.
        self.assertEqual(self.cookie_getter.filter_list_on_dates(self.cookie_getter.read_file_to_list("cookie_log.csv"), [datetime.date(2018, 12, 8)]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])

    def test_get_cookie_frequencies(self):
        """Test get_cookie_frequencies() function.  
        
        Function is tested in the following cases:
        Nicely formatted cookies:
            Expected output: a dict with cookies as keys and frequencies as values.
        Malformed data:
            Expected output: similar to well formatted file. Since the cookies are split
            on commas, malformed data (specifically string with leading comma) won't break 
            the function but it can cause unwanted results such as empty strings in the dict.
        """

        list_a = [
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"
        ]
        self.assertEqual(self.cookie_getter.get_cookie_frequencies(list_a), {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 2, "5UAVanZf6UtGyKVS": 1, "4sMM2LxV07bPJzwf": 2, "fbcn5UAVanZf6UtG": 1})
        list_b = ["abc,fd237y,", ",sdf", "def", "abc", "ghi,-----", "ghi", "jkl", "def", "abc", ""]
        self.assertEqual(self.cookie_getter.get_cookie_frequencies(list_b), {"abc": 3, "def": 2, "ghi": 2, "jkl": 1, "":2})

    def test_get_max_value_in_dict(self):
        """Test test_get_max_value_in_dict() function.  
        
        Function is tested in the following cases:
            Max value occurs one time in dict
            Max value occurs multiple times in dict
            All values are 0
            Empty dict
            In case of non int values, TypeError is raised.
        """

        dict_a = {"abc": 3, "def": 2, "ghi": 2, "jkl": 1, "":1}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_a), 3)
        dict_b = {"abc": 4, "def": 4, "ghi": 2, "jkl": 1, "":1}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_b), 4)
        dict_c = {"abc": 0, "def": 0, "ghi": 0, "jkl": 0, "":0}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_c), 0)
        # Test with empty dictionary
        dict_d = {}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_d), 0)
        dict_e = {"abc": "cat", "def": False, "ghi": 0, "jkl": 0, "":0}
        with self.assertRaises(SystemExit):
            self.cookie_getter.get_max_value_in_dict(dict_e)

    def test_get_most_active_cookies(self):
        """Test test_get_most_active_cookies() function.  
        
        Function is tested in the following cases:
            Multiple most active cookies
            Single most active cookie
            Invalid date type raises an AttributeError.
        """

        list_a = [
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"
        ]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_a), ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf"])
        
        list_b = [
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00"
        ]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_b), ["AtY0laUfhglK3lC7"])
        
        list_c = [
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00"
        ]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_c), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])
        
        list_d = ["4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_d), ["4sMM2LxV07bPJzwf"])

        list_e = ["abc,fd237y,", ",sdf", "def", "abc", "ghi,-----", "ghi", "jkl", "def", "abc"]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_e), ["abc"])

        list_f = ["4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00", 4]
        with self.assertRaises(AttributeError):
            self.self.cookie_getter.get_most_active_cookies(list_d, 0)

    def test_main(self):
        """Test the entire program for correct output in various conditions.  
        
        Function is tested in the following cases:
            Valid file, valid date
            Valid file, valid date with no data
            Invalid file raises FileNotFoundError.
            Malformed data in file in include:
                Text file containing no valid timestamped cookies
                Empty text file
                File contining some valid data and invalid data processes the valid data.
                (Invalid lines are not processed but they are counted and logged.)
            Valid file, no dates
            Valid file, invalid date
            Valid file, multiple invalid dates
            Valid file, some invalid dates
        """

        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-08"]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-09"]), ["AtY0laUfhglK3lC7"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-07"]), ["4sMM2LxV07bPJzwf"])
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("cookie_log.csv", ["2018-12-06"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-09", "2018-12-08", "2018-12-07"]), ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf"])
        # Test program in condition: File not found.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("This_is_not_a_file.csv", ["2018-12-08"])    
        # Test program in condition: Malformed data in log.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("./test_files/malformed_cookie_log.csv", ["2018-12-08"])
        # Test program in condition: Empty log file.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("./test_files/empty_file.txt", ["2018-12-08"])
        self.assertEqual(self.cookie_getter.main("./test_files/problem_statement.txt", ["2018-12-08"]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])
        # Test program in condition: Empty date List.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("cookie_log.csv", [])
        # Test program in condition: Invalid date.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("cookie_log.csv", [None])
        # Test program in condition: All invalid dates.  
        with self.assertRaises(SystemExit):
            self.cookie_getter.main("cookie_log.csv", [None, None])
        # Test program in condition: Some invalid dates.  
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", [None, "2018-12-08", None]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])


if __name__ == "__main__":
    unittest.main()
