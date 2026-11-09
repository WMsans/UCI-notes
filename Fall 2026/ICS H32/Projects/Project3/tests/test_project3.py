import json
import os
import tempfile
import unittest

from project3 import process

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')

SAMPLE_INPUT = [
    'TARGET FILE nominatim_target.json',
    'WEATHER FILE nws_hourly.json',
    'TEMPERATURE AIR C 24 MAX',
    'NO MORE QUERIES',
    'REVERSE FILE nominatim_reverse.json',
]


class TestProcess(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.saved = os.getcwd()
        os.chdir(self.directory.name)
        self.addCleanup(os.chdir, self.saved)
        for name in ('nominatim_target.json', 'nominatim_reverse.json', 'nws_hourly.json'):
            with open(os.path.join(DATA, name), encoding='utf-8') as source:
                with open(name, 'w', encoding='utf-8') as destination:
                    destination.write(source.read())

    def test_sample_from_the_project_write_up(self):
        self.assertEqual(
            process(SAMPLE_INPUT),
            [
                'TARGET 33.6480612/N 117.8469736/W',
                'FORECAST 33.654532225/N 117.83296842499999/W',
                'Auburn Aisle, Oxford Court, University Town Center, Irvine, '
                'Orange County, California, 92612, United States',
                '2024-09-17T19:00:00Z 22.7778',
            ],
        )

    def test_local_files_are_not_attributed(self):
        self.assertFalse(any(line.startswith('**') for line in process(SAMPLE_INPUT)))

    def test_missing_file(self):
        self.assertEqual(
            process(['TARGET FILE nowhere.json'] + SAMPLE_INPUT[1:]), 
            ['FAILED', 'nowhere.json', 'MISSING'],
        )

    def test_misformatted_file(self):
        with open('nws_hourly.json', 'w', encoding='utf-8') as file:
            file.write('{not json')
        self.assertEqual(process(SAMPLE_INPUT), ['FAILED', 'nws_hourly.json', 'FORMAT'])

    def test_file_with_missing_content(self):
        with open('nws_hourly.json', 'w', encoding='utf-8') as file:
            json.dump({'geometry': {}}, file)
        self.assertEqual(process(SAMPLE_INPUT), ['FAILED', 'nws_hourly.json', 'FORMAT'])

    def test_empty_geocoding_results(self):
        with open('nominatim_target.json', 'w', encoding='utf-8') as file:
            file.write('[]')
        self.assertEqual(
            process(SAMPLE_INPUT), ['FAILED', 'nominatim_target.json', 'FORMAT']
        )

    def test_many_queries_in_order(self):
        output = process(SAMPLE_INPUT[:2] + [
            'TEMPERATURE AIR F 1 MAX',
            'WIND 2 MAX',
            'PRECIPITATION 3 MAX',
            'NO MORE QUERIES',
            'REVERSE FILE nominatim_reverse.json',
        ])
        self.assertEqual(len(output), 6)
        self.assertEqual(output[3:6], [
            '2024-09-16T20:00:00Z 70.0000',
            '2024-09-16T21:00:00Z 15.0000',
            # All three hours tie, so the earliest one is reported.
            '2024-09-16T20:00:00Z 5.0000%',
        ])


if __name__ == '__main__':
    unittest.main()
