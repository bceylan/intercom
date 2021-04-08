import unittest
import json

from intercom import Intercom

file_path = 'tests/test_customers.txt'


class IntercomTest(unittest.TestCase):

    def setUp(self):
        self.intercom = Intercom(file_path=file_path)
        self.intercom.customers = {
            '1': {"latitude": "53.339428", "name": "Christina McArdle", "longitude": "-6.257664"},
            '2': {"latitude": "54.339428", "name": "Christina McArdle", "longitude": "-6.257664"}
        }

    def test_0_km(self):
        customer = json.loads('{"latitude": "53.339428", "user_id": 1, "name": "Christina McArdle", "longitude": "-6.257664"}')
        distance = self.intercom.calculate_distance(customer)

        self.assertEqual(distance, 0)

    def test_1_degree_south(self):
        customer = json.loads('{"latitude": "52.339428", "user_id": 1, "name": "Christina McArdle", "longitude": "-6.257664"}')
        distance = self.intercom.calculate_distance(customer)

        self.assertEqual(distance, 111.19492664454764)

    def test_close_enough(self):
        self.intercom.is_it_close_enough()
        customers = self.intercom.customers.copy()
        customers['1']['close_enough'] = True
        customers['2']['close_enough'] = False

        self.assertDictEqual(self.intercom.customers, customers)


if __name__ == '__main__':
    unittest.main()
