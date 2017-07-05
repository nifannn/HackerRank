def count_substring(string, sub_string):
    start_list = [i for i, e in enumerate(string) if e == sub_string[0]]
    result = 0
    for idx in start_list:
        if idx + len(sub_string) <= len(string):
            if string[idx:idx+len(sub_string)] == sub_string:
                result = result + 1
    return result
