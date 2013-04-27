def groupby(func, seq):
    result_dictionary = {}
    for i in seq:
        key = func(i)
        if key in result_dictionary:
            result_dictionary[key].append(i)
        else:
            result_dictionary[key] = [i]
    return result_dictionary
