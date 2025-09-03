from analytics.io.reader import read_data
from analytics.io.writer import write_data
from analytics.core.processor import process_data
from analytics.tools.formatter import format_data


data = read_data()
processed_data_1 = process_data(data)
processed_data_2 = format_data(processed_data_1)
print(write_data(processed_data_2))
