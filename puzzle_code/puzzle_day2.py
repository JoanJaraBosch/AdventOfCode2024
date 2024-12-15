def check_report(report):
    cont = 1
    found = 0
    first_dif = 0
    val_anterior = int(report[0])
    safe = 0
    while cont < len(report) and found == 0:
        level = int(report[cont])
        if cont == 1:
            first_dif = val_anterior - level

        if cont != 0:
            if (val_anterior - level) > 3 or (val_anterior - level) < -3 or (val_anterior - level) == 0:
                found = 1
            else:
                if first_dif < 0 < (val_anterior - level):
                    found = 1
                elif first_dif > 0 > (val_anterior - level):
                    found = 1
        val_anterior = level
        cont = cont + 1
    if found == 0:
        safe = safe + 1
    return safe


def count_reports_safe():
    reports = open("../input/day2.txt", "r")
    safe = 0
    for report in reports:
        report = report.replace("\n", "").split(" ")
        safe = safe + check_report(report)

    print("There are ", safe, "reports safe")


def count_reports_safe_part2():
    reports = open("../input/day2.txt", "r")
    result = 0
    for report in reports:
        cont = 0
        safe = 0
        found = 0
        report = report.replace("\n", "").split(" ")
        while cont < len(report) and found == 0:
            if cont == 0:
                safe = check_report(report)
                if safe == 0:
                    report_level_removed = report[cont+1:]
                    safe = check_report(report_level_removed)
            elif cont == len(report)-1:
                report_level_removed = report[:-1]
                safe = check_report(report_level_removed)
            else:
                report_level_removed = report[:cont]+report[cont+1:]
                safe = check_report(report_level_removed)

            if safe == 1:
                found = 1
            cont = cont + 1
        result = result + safe
    print("There are ", result, "reports safe")
