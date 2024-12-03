import puzzle_day1
import puzzle_day2
import puzzle_day3

if __name__ == '__main__':

    x = input("Which puzzle do you want to solve?: ")
    if int(x) == 1:
        print("DAY 1 FIRST PART")
        print(puzzle_day1.distances())
        print("DAY 1 SECOND PART")
        print(puzzle_day1.similarity())
    elif int(x) == 2:
        print("DAY 2 FIRST PART")
        puzzle_day2.count_reports_safe()
        print("DAY 2 SECOND PART")
        puzzle_day2.count_reports_safe_part2()
    elif int(x) == 3:
        print("DAY 3 FIRST PART")
        print(puzzle_day3.extract_numbers_from_file())
        print("DAY 3 SECOND PART")
        print(puzzle_day3.calculate_enabled_multiplications())
