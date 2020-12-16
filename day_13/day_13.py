import numpy as np
from helpers.utils import get_puzzle_input

test_input = """939
7,13,x,x,59,x,31,19"""

time_stamp, bus_intervals = get_puzzle_input(13).split("\n")
time_stamp = int(time_stamp)
bus_intervals = [int(n) for n in bus_intervals.split(",") if n != "x"]
series = []
for interval in bus_intervals:
	time_series = 0
	time_series_array = []
	while time_series < time_stamp:
		time_series += interval
		time_series_array.append(time_series)
	series.append(time_series_array)


def find_nearest(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	return array[idx]


offset = [find_nearest(np.array(array), time_stamp) % time_stamp for array in series]
mins_to_wait = min(offset)
bus = bus_intervals[np.array(offset).argmin()]
print(bus)
print(bus * mins_to_wait)
