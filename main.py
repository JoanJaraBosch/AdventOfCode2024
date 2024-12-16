from puzzle_code import puzzle_day10, puzzle_day12, puzzle_day15, puzzle_day3, puzzle_day2, puzzle_day7, puzzle_day5, \
    puzzle_day14, puzzle_day1, puzzle_day13, puzzle_day6, puzzle_day4, puzzle_day11, puzzle_day8, puzzle_day9, puzzle_day16

if __name__ == '__main__':

    x = input("Which puzzle do you want to solve?: ")
    boucle = True
    while boucle:
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
            print(puzzle_day10.solve_part1())
            print("DAY 10 SECOND PART")
            print(puzzle_day10.solve_part2())
        elif int(x) == 11:
            print("DAY 11 FIRST PART")
            print(puzzle_day11.iterative_count_end_nodes(25))
            print("DAY 11 SECOND PART")
            print(puzzle_day11.iterative_count_end_nodes(75))
        elif int(x) == 12:
            print("DAY 12 FIRST PART AND SECOND PART")
            print(puzzle_day12.solution())
        elif int(x) == 13:
            print("DAY 13 FIRST PART")
            print(puzzle_day13.solver(False))
            print("DAY 13 SECOND PART")
            print(puzzle_day13.solver(True))
        elif int(x) == 14:
            print("DAY 14 FIRST PART AND SECOND PART")
            print(puzzle_day14.main())
        elif int(x) == 15:
            print("DAY 15 FIRST PART")
            print(puzzle_day15.robot_movement(1))
            print("DAY 15 SECOND PART")
            print(puzzle_day15.robot_movement(2))
        elif int(x) == 16:
            print("DAY 16 FIRST PART")
            print(puzzle_day16.traverse())
            print("DAY 16 SECOND PART")
            print(puzzle_day16.find_all_paths())
        else:
            print("Not a valid puzzle")

        answer = input("Do you want to keep solving puzzles? (Y/n)")
        if str(answer).upper() != "Y":
            boucle = False
