import unittest
from main import *


class TestGr(unittest.TestCase):
    def test_from_str_to_dict(self):
        lst = ['DATE, RESOURCE, AMOUNT, STAFFID\n', '2020-01, 2, 10, 4\n', '2020-01, 1, 10, 2\n', '2020-02, 4, 20, 4\n', '2020-09, 1, 44, 1\n', '2020-10, 3, 34, 3\n']
        result = from_str_to_dict(lst)
        expect = [{'DATE': '2020-01', 'RESOURCE': '2', 'AMOUNT': '10', 'STAFFID': '4'}, {'DATE': '2020-01', 'RESOURCE': '1', 'AMOUNT': '10', 'STAFFID': '2'}, {'DATE': '2020-02', 'RESOURCE': '4', 'AMOUNT': '20', 'STAFFID': '4'}, {'DATE': '2020-09', 'RESOUCE': '1', 'AMOUNT': '44', 'STAFFID': '1'}, {'DATE': '2020-10', 'RESOURCE': '3', 'AMOUNT': '34', 'STAFFID': '3'}]
        self.assertEqual(expect, result)

    def test_filtrate(self):
        lst = [{'DATE': '2020-03', 'RESOURCE': '1', 'AMOUNT': '48', 'STAFFID': '4'}, {'DATE': '2020-05', 'RESOURCE': '3', 'AMOUNT': '25', 'STAFFID': '4'}, {'DATE': '2020-01', 'RESOURCE': '2', 'AMOUNT': '10', 'STAFFID': '3'}, {'DATE': '2020-02', 'RESOURCE': '2', 'AMOUNT': '20', 'STAFFID': '1'}, {'DATE': '2020-03', 'RESOURCE': '2', 'AMOUNT': '40', 'STAFFID': '1'}, {'DATE': '2020-04', 'RESOURCE': '1', 'AMOUNT': '48', 'STAFFID': '4'}, {'DATE': '2020-02', 'RESOURCE': '1', 'AMOUNT': '33', 'STAFFID': '4'}, {'DATE': '2020-01', 'RESOURCE': '3', 'AMOUNT': '10', 'STAFFID': '2'}, {'DATE': '2020-04', 'RESOURCE': '3', 'AMOUNT': '23', 'STAFFID': '1'}, {'DATE': '2020-02', 'RESOURCE': '3', 'AMOUNT': '15', 'STAFFID': '3'}, {'DATE': '2020-03', 'RESOURCE': '3', 'AMOUNT': '20', 'STAFFID': '2'}, {'DATE': '2020-05', 'RESOURCE': '2', 'AMOUNT': '16', 'STAFFID': '3'}, {'DATE': '2020-01', 'RESOURCE': '1', 'AMOUNT': '10', 'STAFFID': '4'}, {'DATE': '2020-05', 'RESOURCE': '1', 'AMOUNT': '33', 'STAFFID': '2'}, {'DATE': '2020-04', 'RESOURCE': '2', 'AMOUNT': '80', 'STAFFID': '2'}]
        result = filtrate('STAFFID', 1, lst)
        expect = [{'DATE': '2020-02', 'RESOURCE': '2', 'AMOUNT': '20', 'STAFFID': '1'}, {'DATE': '2020-03', 'RESOURCE': '2', 'AMOUNT': '40', 'STAFFID': '1'}, {'DATE': '2020-04', 'RESOURCE': '3', 'AMOUNT': '23', 'STAFFID': '1'}]
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
