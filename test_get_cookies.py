import unittest
import logging
import datetime
from get_cookies import CookieGetter



class TestCookieGetter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename="tests.log", 
            format="%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S")
        logging.info("test_get_cookies.py")

    @classmethod
    def tearDownClass(cls):
        logging.info("Exiting\n" + "-"*70)


    def setUp(self):
        self.cookie_getter = CookieGetter()


    def test_string_to_date(self):
        """Test string_to_date() function.  """
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
        self.assertEqual(self.cookie_getter.read_file_to_list("empty_file.txt"),[])

    def test_filter_list_on_dates(self):
        # Test with no cookies and no dates.
        self.assertEqual(self.cookie_getter.filter_list_on_dates([], []),[])
        # Test with no cookies.
        self.assertEqual(self.cookie_getter.filter_list_on_dates([], [datetime.date(2018, 12, 8)]),[])
        # Test with no dates.
        self.assertEqual(self.cookie_getter.filter_list_on_dates(self.cookie_getter.read_file_to_list("cookie_log.csv"), []),[])
        # Regular test case with cookies and a date.
        self.assertEqual(self.cookie_getter.filter_list_on_dates(self.cookie_getter.read_file_to_list("cookie_log.csv"), [datetime.date(2018, 12, 8)]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])


    def test_get_cookie_frequencies(self):
        """Test get_cookie_frequencies() function.  """
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
        list_b = ["abc,fd237y,", ",sdf", "def", "abc", "ghi,-----", "ghi", "jkl", "def", "abc"]
        self.assertEqual(self.cookie_getter.get_cookie_frequencies(list_b), {"abc": 3, "def": 2, "ghi": 2, "jkl": 1, "":1})

    def test_get_max_value_in_dict(self):
        dict_a = {"abc": 3, "def": 2, "ghi": 2, "jkl": 1, "":1}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_a), 3)
        dict_b = {"abc": 4, "def": 4, "ghi": 2, "jkl": 1, "":1}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_b), 4)
        dict_c = {"abc": 0, "def": 0, "ghi": 0, "jkl": 0, "":0}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_c), 0)
        # Test with empty dictionary
        dict_d = {}
        self.assertEqual(self.cookie_getter.get_max_value_in_dict(dict_d), 0)

    def test_get_most_active_cookies(self):
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
        list_d = [
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"
        ]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_d), ["4sMM2LxV07bPJzwf"])
        list_e = ["abc,fd237y,", ",sdf", "def", "abc", "ghi,-----", "ghi", "jkl", "def", "abc"]
        self.assertEqual(self.cookie_getter.get_most_active_cookies(list_e), ["abc"])


    def test_main(self):
        """Test the entire program for correct output in various conditions.  """
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-08"]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-09"]), ["AtY0laUfhglK3lC7"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-07"]), ["4sMM2LxV07bPJzwf"])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-06"]), [])
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", ["2018-12-09", "2018-12-08", "2018-12-07"]), ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf"])
        # Test program in condition: File not found.  
        with self.assertRaises(FileNotFoundError):
            self.cookie_getter.main("This_is_not_a_file.csv", ["2018-12-08"])      
        # Test program in condition: Malformed data in log.  
        self.assertEqual(self.cookie_getter.main("malformed_cookie_log.csv", ["2018-12-08"]), [])
        self.assertEqual(self.cookie_getter.main("empty_file.txt", ["2018-12-08"]), [])
        self.assertEqual(self.cookie_getter.main("problem_statement.txt", ["2018-12-08"]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])
        # Test program in condition: Empty date List.  
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", []), [])
        # Test program in condition: Invalid date.  
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", [None]), [])
        # Test program in condition: All invalid dates.  
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", [None, None]), [])
        # Test program in condition: Some invalid dates.  
        self.assertEqual(self.cookie_getter.main("cookie_log.csv", [None, "2018-12-08", None]), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])


    

if __name__ == "__main__":
    unittest.main()
