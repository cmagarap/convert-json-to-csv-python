from constants import DataMapping
import csv
import json
import logging
import utils

logging.basicConfig(level=logging.INFO)


def main():
    logging.info('Extracting data from JSON file...')
    with open('catch-sales/catch_sales.json', 'r') as file:
        data_from_json = json.load(file)
        file.close()

    # Iterate over the JSON data and flatten the data
    lst = []
    for obj in data_from_json:
        lst.append(list(utils.flatten_expand(obj)))

    # Flatten the list of list
    flat_data = utils.flatten_list(lst)

    # Rename the keys in flat_data and only get specific values
    final = []
    for obj in flat_data:
        data_mapping = DataMapping()
        final.append(data_mapping.get_data_mapping(obj))

    logging.info('Writing data to CSV...')
    file_path = 'catch-sales/catch_sales.csv'
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, final[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(final)
    logging.info(f' Data successfully written to {file_path}')


if __name__ == '__main__':
    main()
