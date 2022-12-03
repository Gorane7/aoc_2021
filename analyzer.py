import sys
import json


def main():
    file = open("data.json", "r")
    data = json.loads(file.read())
    file.close()

    data = data["members"]
    days = {}
    for user, scores in data.items():
        for day, times in scores["completion_day_level"].items():
            for part, part_times in times.items():
                if (day, part) not in days.keys():
                    days[(day, part)] = []
                days[(day, part)].append((part_times["get_star_ts"], scores["name"]))
    for key in days.keys():
        days[key].sort()
    for key, value in days.items():
        print(f"Ordering for day {key}:")
        [print(x[1]) for x in value[:int(sys.argv[1])]]
        print()


if __name__ == '__main__':
    main()
