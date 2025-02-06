def group_by_type(lst):
    my_dict = {}

    def flatten(our_lst):
        result = []

        for item in our_lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    for item in flatten(lst):
        if type(item).__name__ not in my_dict:
            my_dict[type(item).__name__] = []

        my_dict[type(item).__name__].append(item)

    return my_dict


# input_data = [1, "hello", [2, "world", 3.14], 42]
# print(group_by_type(input_data))




