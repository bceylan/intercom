import math
import logging
import os
import json
from time import time

import click


_DUBLIN_OFFICE_LONGITUDE = math.radians(-6.257664)
_DUBLIN_OFFICE_LATITUDE = math.radians(53.339428)
_EARTH_RADIUS = 6371  # km
_INVITATION_THRESHOLD = 100  # km


# Logger
_logger = logging.getLogger('intercom')
_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('intercom.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - ' +
                              '%(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
_logger.addHandler(file_handler)


class Intercom(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.customers = dict()

    def start(self):
        self.customers = self.read_customers_file(self.file_path)

        if not self.customers:
            _logger.error('Customer file is empty. Quitting...')
            exit(3)

        self.is_it_close_enough()

        if not self.print_output(self.customers):
            self.error('Could not print to output.')
            exit(4)

    def is_it_close_enough(self):
        for key in self.customers.keys():
            self.customers[key]['close_enough'] = True if \
                (Intercom.calculate_distance(self.customers[key]) <= 100) else False

    @staticmethod
    def read_customers_file(file_path):
        customer_dict = dict()
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    customer = json.loads(line)
                    customer_id = customer.get('user_id')
                    del customer['user_id']
                    customer_dict[customer_id] = customer
            return customer_dict
        except Exception:
            _logger.exception(f'Error reading file {file_path}')
            return

    @staticmethod
    def calculate_distance(customer):
        if not isinstance(customer, dict):
            return

        try:
            customer_longitude = float(customer.get('longitude'))
            customer_latitude = float(customer.get('latitude'))
            customer_longitude = math.radians(customer_longitude)
            customer_latitude = math.radians(customer_latitude)

            # looks bad
            return _EARTH_RADIUS * math.acos(math.sin(customer_latitude) * math.sin(_DUBLIN_OFFICE_LATITUDE) + math.cos(customer_latitude) * math.cos(_DUBLIN_OFFICE_LATITUDE) * math.cos(customer_longitude-_DUBLIN_OFFICE_LONGITUDE))
        except Exception:
            _logger.exception('Error while calculating distance.')
            return

    @staticmethod
    def print_output(customers):
        if not isinstance(customers, dict):
            _logger.error('Customers must be dictionary.')
            return

        customers = {key: val for key, val in sorted(customers.items(), key=lambda ele: ele[0])}

        try:
            with open('output.csv', 'w') as f:
                f.write('user_id,name\n')
                for key in customers.keys():
                    if customers[key]['close_enough']:
                        user_id = key
                        user_name = customers[key]['name']
                        f.write(f'{user_id},{user_name}\n')
            return True
        except Exception:
            _logger.exception('Error writing output file.')
            return


@click.command()
@click.argument('fpath')
def intercom(fpath):
    if not fpath:
        print('Argument file must be given.')
        exit(1)

    if not os.path.isfile(fpath):
        print('{file} is not file.')
        exit(2)

    intercom = Intercom(file_path=fpath)

    start = time()
    intercom.start()
    end = time()

    print(f'\nIntercom took {int(end-start)} seconds.')
    _logger.info(f'\nIntercom took {int(end-start)} seconds.')

    return


if __name__ == '__main__':
    intercom()
    exit(0)
