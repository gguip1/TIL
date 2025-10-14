import sys

full_station_name = sys.stdin.readline()

if '(' in full_station_name and ')' in full_station_name:
    station_name, sub_station_name = full_station_name.replace(')', '').split(' (')
    print(station_name.strip())
    print(sub_station_name.strip())
else:
    print(full_station_name.strip())
    print('-')