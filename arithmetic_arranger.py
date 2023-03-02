def arithmetic_arranger(lst, ans=False):

    valid_operators = ["-", "+"]
    max_number_length = 4
    concatinated_first_row = ""
    concatinated_second_row = ""
    concatinated_third_row = ""
    concatinated_fourth_row = ""

    # Perform error tests
    if len(lst) > 5:
        return "Error: Too many problems."

    for item in lst:
        split_lst = item.split(" ")

        if split_lst[0].isdigit() == False or split_lst[2].isdigit() == False:
            return "Error: Numbers must only contain digits."
        if len(split_lst[0]) > 4 or len(split_lst[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if split_lst[1] not in ["-", "+"]:
            return "Error: Operator must be '+' or '-'."

        # Find correct operator
        if split_lst[1] == "+":
            solution = int(split_lst[0]) + int(split_lst[2])
        else:
            solution = int(split_lst[0]) - int(split_lst[2])

        # Find longest operand in each problem and add placeholders for the operator and space (+2)
        max_length = max(len(split_lst[0]), len(split_lst[2])) + 2
        # Compute length for each row in each problem
        first_row = str(split_lst[0]).rjust(max_length)
        second_row = str(split_lst[1]) + str(split_lst[2]).rjust(max_length - 1)
        # Created dashed line based on max_length
        third_row = ""
        for dash in range(max_length):
            third_row += "-"
        fourth_row = str(solution).rjust(max_length)

        # Build a concatinated string for each row seperately
        concatinated_first_row += first_row + "    "
        concatinated_second_row += second_row + "    "
        concatinated_third_row += third_row + "    "
        concatinated_fourth_row += fourth_row + "    "

    # Strip out spaces at end of each string
    concatinated_first_row = concatinated_first_row.rstrip()
    concatinated_second_row = concatinated_second_row.rstrip()
    concatinated_third_row = concatinated_third_row.rstrip()
    concatinated_fourth_row = concatinated_fourth_row.rstrip()

    # Build final output string by concatinating the concatinated rows
    if ans:
        concatinate_all_rows = (
            concatinated_first_row
            + "\n"
            + concatinated_second_row
            + "\n"
            + concatinated_third_row
            + "\n"
            + concatinated_fourth_row
        )
    else:
        concatinate_all_rows = (
            concatinated_first_row
            + "\n"
            + concatinated_second_row
            + "\n"
            + concatinated_third_row
        )

    arranged_problems = concatinate_all_rows

    return arranged_problems


# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
