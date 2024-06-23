def unique(input_list= []):
    # """
    # Returns a list containing only unique elements from the input_list.
    
    # Args:
    # - input_list (list): A list of elements where duplicates are to be removed.
    
    # Returns:
    # - list: A new list containing unique elements from input_list in the order they first appeared.
    # """
    to_return: list = []
    
    for value in input_list:
        if value not in to_return:
            to_return.append(value)
    
    return to_return
