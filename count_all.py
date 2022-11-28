def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    a = 0
    q = 0
    for i in txt:
        if i.isdigit():
            a+=1
        if i.isalpha():
            q+=1
    return [a,q]
print(count_all('32kmkmk2'))