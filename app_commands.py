import re

import const


def help():
    return const.HELP


def define_term(content):
    expression = ' (.*)'
    match = re.search(expression, content)
    term = match.group(1).lower()
    term = term.title()
    if term in const.DICT.keys():
        return f"**{term}**: {const.DICT[term]}"
    else:
        return f"Word '{term}' not found."


def dict_print():
    ret_dict = "__**All Terms**__:\n"
    for term in const.DICT.keys():
        ret_dict += f"{term}\n"
    return ret_dict


def day(content):
    expression = ' (\d*)'
    match = re.search(expression, content)
    number = match.group(1)
    if number in const.DAY.keys():
        return f"**Day {number}**: {const.DAY[number]}"
    else:
        return f"Day {number} not found."


def last_day(content):
    last = list(const.DAY.keys())[0]
    return f"**Day {last}**: {const.DAY[last]}"


def get_resource(content):
    expression = ' (.*)'
    match = re.search(expression, content)
    resource = match.group(1)
    resource = resource.lower()
    resource = resource.title()
    if resource == "All":
        ret_dict = "__**All Resources Available:**__\n"
        for key, value in const.RESOURCE_DEF.items():
            ret_dict += f"{key}: {value}\n"
        return ret_dict
    elif resource in const.RESOURCES.keys():
        return f"**{resource}**: {const.RESOURCES[resource]}"
    else:
        return f"{resource} is undefined. Refer to `resource all` for a list of all available resources."
