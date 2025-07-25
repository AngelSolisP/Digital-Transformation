def string_reverse(my_string):
    """
    This function takes a string and returns it reversed.
    
    :param my_string: The string to be reversed
    :return: The reversed string
    """
    reversed_string = ""
    for character in my_string:
        reversed_string = character + reversed_string
    
    return reversed_string

if __name__ == "__main__":
    print(string_reverse("Hello, World!"))  # Output: !dlroW ,olleH
