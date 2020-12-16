from collections import OrderedDict
test_input = """13,16,0,12,15,1"""

tracker = OrderedDict()
turn = 1
# list of count, turn number
for starter in test_input.split(","):
	# starter number : count, turn_index
	tracker[starter] = [1, turn]
	turn += 1

while turn < 30000001:
	# print("hello")
	prev_number, (count, last_turn_spoken_on) = tracker.popitem()
	tracker[prev_number] = [count, turn - 1]
	# turn previous num was spoken on
	turn_spoken_on = turn - 1
	# consider 6
	if count == 1:
		num_to_speak = 0
	# we have 2 turns that this was spoken on and we need difference
	else:
		num_to_speak = turn_spoken_on - last_turn_spoken_on
	num_to_speak = str(num_to_speak)
	if num_to_speak in tracker:
		tracker.move_to_end(num_to_speak)
		tracker[num_to_speak][0] += 1
	else:
		tracker[num_to_speak] = [1, turn]
	turn += 1
print(tracker.popitem())