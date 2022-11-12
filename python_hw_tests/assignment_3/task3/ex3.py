def count_characters(my_string,dictionary):
    my_string = my_string.lower()

    for i in range(len(my_string)):
        if my_string[i] not in dictionary:
            dictionary[my_string[i]] = 1
        else:
            dictionary[my_string[i]] += 1
