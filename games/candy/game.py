from random import randint
# temp_step = 24


def get_step_list(param) -> list:
    num_list = list()
    num_list.append(randint(param, param + 10))
    num_list.append(randint(param * 2, param * 2 + 10))
    num_list.append(randint(param * 3, param * 3 + 10))
    return num_list


def get_total_list(param: int) -> list:
    num_list = list()
    num_list.append(randint(param * 4, param * 6))
    num_list.append(randint(param * 8, param * 10))
    num_list.append(randint(param * 12, param * 14))
    return num_list
