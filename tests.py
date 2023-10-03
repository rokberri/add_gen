def T(array):
    if len(array)<65:
        print("Too small to find T")
        exit()
    return len(set(array[65::]))