import puzzle_day1
import puzzle_day2
import puzzle_day3
import puzzle_day4
import puzzle_day5
import puzzle_day6
import puzzle_day7
import puzzle_day8
import puzzle_day9

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
    elif int(x) == 4:
        print("DAY 4 FIRST PART")
        print(puzzle_day4.count_xmas())
        print("DAY 4 SECOND PART")
        print(puzzle_day4.count_mas())
    elif int(x) == 5:
        print("DAY 5 FIRST PART")
        print(puzzle_day5.print_order())
        print("DAY 5 SECOND PART")
        print(puzzle_day5.print_order_and_fix())
    elif int(x) == 6:
        print("DAY 6 FIRST PART")
        print(puzzle_day6.guard_movement())
        print("DAY 6 SECOND PART")
        print(puzzle_day6.guard_movement_loop())
    elif int(x) == 7:
        print("DAY 7 FIRST PART")
        puzzle_day7.add_mul()
        print("DAY 7 SECOND PART")
        puzzle_day7.add_mul_concat()
    elif int(x) == 8:
        puzzle_day8.main()
    elif int(x) == 9:
        print("DAY 9 FIRST PART")
        print(puzzle_day9.order_map(1))
        print("DAY 9 SECOND PART")
        print(puzzle_day9.order_map(2))
    elif int(x) == 10:
        print("DAY 10 FIRST PART")
        print(puzzle_day9.order_map(1))
        print("DAY 10 SECOND PART")
        print(puzzle_day9.order_map(2))
