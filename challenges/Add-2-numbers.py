def add_two_number(l1, l2):
    """
    :param l1: List
    :param l2: List
    :return: List, a sum of l1 and l2
    """
    carry = 0
    result = []

    while l1 or l2 or carry:
        if l1:
            carry += l1.pop()
        if l2:
            carry += l2.pop()
        result.append(carry % 10)
        carry //= 10
    return result[::-1] #reverse the list