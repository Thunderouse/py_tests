import unittest
import requests
import time
from yandex import create_folder


folders_name = 'new_folder'
token = 'TOKEN'


class TestYandex(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder(token, folders_name), 201)
        params_get_meta = {'path': '/',
                           'fields': '_embedded.items.name',
                           'limit': 999999999999}
        disk_headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth {token}'}
        disk_create_folder_method = '/v1/disk/resources'
        url_disk = 'https://cloud-api.yandex.net'
        time.sleep(0.34)
        get_meta = requests.get(url_disk + disk_create_folder_method,
                                params=params_get_meta,
                                headers=disk_headers).json()
        files_names = [item['name'] for item in get_meta['_embedded']['items']]
        self.assertIn(folders_name, files_names)

    @unittest.expectedFailure
    def test_wrong_folder_name(self):
        FIXTURE = [folders_name, '', '   ', '/newfolder']
        etalon = 201
        for arg in FIXTURE:
            result = create_folder(token, arg)
            self.assertEqual(result, etalon)

