import sys
from datetime import timedelta

def analyze_cat_shelter(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        return
    except Exception as e:
        print(f'Error reading file: {e}')
        return

    cat_visits = 0
    other_cats = 0
    total_time_in_house = timedelta()
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_type, entry_time, exit_time = parts

        entry_time = int(entry_time)
        exit_time = int(exit_time)

        if cat_type == 'OURS':
            cat_visits += 1
            total_time_in_house += timedelta(minutes=(exit_time - entry_time))
            visit_lengths.append(exit_time - entry_time)
        elif cat_type == 'THEIRS':
            other_cats += 1

    if cat_visits == 0:
        print('No cat visits recorded.')
        return

    average_visit_length = sum(visit_lengths) / cat_visits
    longest_visit = max(visit_lengths)
    shortest_visit = min(visit_lengths)

    print('\nLog File Analysis')
    print('==================\n')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}\n')
    print(f'Total Time in House: {total_time_in_house.total_seconds() // 3600} Hours, {(total_time_in_house.total_seconds() % 3600) // 60} Minutes\n')
    print(f'Average Visit Length: {int(average_visit_length)} Minutes')
    print(f'Longest Visit: {longest_visit} Minutes')
    print(f'Shortest Visit: {shortest_visit} Minutes\n')

if __name__ == "__main__":
    # print(f'abc arg: {sys.argv}')
    if len(sys.argv) < 2:
        print('Missing command line argument!')
        file_paths = ("shelter_2023-08-25.log", "shelter_2023-08-26.log", "shelter_2023-08-27.log")
    else:

        file_paths = sys.argv[1:]

    # print(f'abc paths: {file_paths}')

    for file_path in file_paths:
        analyze_cat_shelter(file_path)
