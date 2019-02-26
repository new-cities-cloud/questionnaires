import csv
import itertools
import yaml

filepath = './data-questionnaire.yaml'

my_list = yaml.load(open(filepath))
keys = list(my_list[0].keys())

with open('people.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(my_list)
