# ***** ADVENT OF CODE 2022 *****
# ************ DAY 6 ************
# ****************** Part 1 *****

imported_data = ""

with open("06_tuning_input.txt") as input:
    imported_data = input.read().strip("\n")


def find_pos_start_of_packet_marker(datastream):
    start_of_packet_marker = list()
    num_chars_processed = 0
    for char in datastream:
        if char in start_of_packet_marker:
            start_idx = start_of_packet_marker.index(char) + 1
            start_of_packet_marker = start_of_packet_marker[start_idx:]
        start_of_packet_marker.append(char)
        num_chars_processed += 1
        if len(start_of_packet_marker) == 4:
            return num_chars_processed


pos_start_of_packet_marker = find_pos_start_of_packet_marker(imported_data)

print(f"""
      The start-of-packet marker is found after processing
      {pos_start_of_packet_marker} characters in the datastream.
      """)


# ****************** Part 2 *****

def find_pos_start_of_message_marker(datastream):
    start_of_message_marker = list()
    num_chars_processed = 0
    for char in datastream:
        if char in start_of_message_marker:
            start_idx = start_of_message_marker.index(char) + 1
            start_of_message_marker = start_of_message_marker[start_idx:]
        start_of_message_marker.append(char)
        num_chars_processed += 1
        if len(start_of_message_marker) == 14:
            return num_chars_processed


pos_start_of_message_marker = find_pos_start_of_message_marker(imported_data)

print(f"""
      The start-of-message marker is found after processing
      {pos_start_of_message_marker} characters in the datastream.
      """)
