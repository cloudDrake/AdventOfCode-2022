def get_highest_calories(file_name):
    calorie_list_lines = open(file_name, 'r').readlines()
    elf_calories, current_calories_count = [], 0
    for calorie_str in calorie_list_lines:
        calories: str = calorie_str.strip('\n')
        if not calories:
            elf_calories.append(current_calories_count)
            current_calories_count = 0
        else:
            current_calories_count += int(calories)
    return sorted(elf_calories, reverse=True)


def get_top_three_highest_calories(calories_list):
    top_three_elves = calories_list[0:3]
    return sum(top_three_elves)


if __name__ == '__main__':
    highest_calories_list = get_highest_calories("resources/dayOne/day_one_part_one.txt")
    top_three_highest_calories_summed = get_top_three_highest_calories(highest_calories_list)
    print(f'part one highest calorie: {highest_calories_list[0]}')
    print(f'part one highest calorie: {top_three_highest_calories_summed}')
