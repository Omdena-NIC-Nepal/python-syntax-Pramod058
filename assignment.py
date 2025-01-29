
def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if(number>10):
        return "Greater"
    if(number<10):
        return "Lesser"
    if(number==10):
        return "Equal"


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for nums in range(n+1):
        sum = sum + nums
    return sum


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    tuple_var = (sum(numbers), max(numbers), min(numbers))
    return tuple_var

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    students_list = []
    for name, score in students_dict.items(): 
        if score>80:
            students_list.append(name)
    return students_list


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    result_set =  (set(list1) & set(list2))
    return result_set


def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """

    result_dict = {"sum": a+b, "difference": a-b , "product": a*b , "quotient": a/b if b!=0 else "Undefined"}
    return result_dict

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    result_dict = {"and": x and y, "or": x or y , "not_x": not x}

    return result_dict

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    result_dict = {"and": a & b, "or": a | b , "xor": a^b}

    return result_dict