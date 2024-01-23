def reverseStringWordWise(string):
    return " ".join(map(str, string.split()[::-1]))

    # string += ' '
    # revStr = []
    # temp = ''
    # for i in string:
    #     if i.isalpha():
    #         temp += i
    #     else:
    #         revStr.append(temp)
    #         temp = ''
    
    # for i in revStr[::-1]:
    #     temp = temp + ' ' + i
    # return temp[1:]


string = "eye of the tiger"
result = reverseStringWordWise(string)

print(f"String: {string}\nReversed String: {result}")