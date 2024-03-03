def buble_sort(input):

    for i in range(len(input)):
        for j in range(len(input)):
            if (len(input) -j - 2) < 0:
                break
            if input[len(input) - j - 1] < input[len(input) - j -2]:
                input[len(input) - j - 1] , input[len(input) - j -2] = input[len(input) - j -2] , input[len(input) - j - 1] 

    return input
