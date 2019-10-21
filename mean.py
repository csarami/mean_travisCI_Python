def mean(x):
    if len(x) == 0:
        return 0
    else:
        sum = 0
        for i in range(len(x)):
            sum += x[i]
        return sum/len(x)
