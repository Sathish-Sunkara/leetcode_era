start = 0
petrol = 0
total_petrol = 0
total_distance = 0
def fun():
    for i in range(len(petropumps)):
        petrol += petrolpumps[i][0] - petrolpumps[i][1]
        if petrol < 0:
            start = i+1
            petrol = 0
        total_petrol += petrolpumps[i][0]
        total_distance += petrolpumps[i][1]
    if total_petrol >= total_distance :
        return start
    return -1
