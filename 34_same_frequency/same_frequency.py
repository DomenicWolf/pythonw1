def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    count1 = {}
    count2 = {}
    str1 = str(num1)
    str2 = str(num2)

    for num in str1:
        int(num)
        count1[num] = count1.get(num,0) +1

    for num in str2:
        int(num)
        count2[num] = count2.get(num,0) +1

    if count1 == count2:
        return True
    return False