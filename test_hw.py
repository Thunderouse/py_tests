import unittest
from hw import *


class TestHw(unittest.TestCase):

    def test_task_1(self):
        FIXTURE = [(geo_logs, [i for i in geo_logs if 'Россия' not in list(i.values())[0]]),
                   ([{'visit1': ['Москва', 'Россия']}],[])]
        for arg, etalon in FIXTURE:
            self.assertEqual(geo(arg), etalon)

    @unittest.expectedFailure
    def test2_task_1(self):
        etalon = [{'visit2': ['Дели', 'Индия']},
                  {'visit4': ['Лиссабон', 'Португалия']},
                  {'visit5': ['Париж', 'Франция']},
                  {'visit6': ['Лиссабон', 'Португалия']}]
        FIXTURE = [[geo_logs], 1, []]
        for arg in FIXTURE:
            self.assertEqual(geo(arg), etalon)

    def test_task_2(self):
        result = to_unique(ids)
        self.assertSetEqual(result, {id_ for item in ids.values() for id_ in item})
        self.assertSetEqual(result, {98, 15, 35, 213, 54, 119})

    def test_task_4(self):
        result = dict_max(stats)
        self.assertEqual(result, max(stats, key=stats.get))
        self.assertEqual(result, 'yandex')



