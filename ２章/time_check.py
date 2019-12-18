sched = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0),
        (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
        (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0),]

def BestTimeToParty(schedule, ystart, yend):
    time = []
    for i in schedule:
        time.append((i[0], 'start'))
        time.append((i[1], 'end'))
    
    sort(time)
    max, best_time = choosetime(time, ystart, yend)

    print('Best time to attend the party is as', best_time,'o\'clock',
        ':', max,'celebrities will be attending!')

def sort(time):
    for ind in range(len(time) - 1):
        ism = ind
        for i in range(ind, len(time)):
            if time[ism] > time[i]:
                ism = i
        time[ind], time[ism] = time[ism], time[ind]

def choosetime(time, ystart, yend):
    max_cou = 0
    count = 0
    for i in time:
        # change
        if i[1] == 'start' and i[0] >= ystart and i[0] < yend:
            count += 1
            print(count, i)
        # change
        elif i[1] == 'end' and i[0] > ystart and i[0] < yend:
            count -= 1
            print(count, i)
        if count > max_cou:
            max_cou = count
            best_time = i[0]
    
    return max_cou, best_time

ystart, yend = map(float, input('Please enter ystart and yend: ').split())
# print(type(ystart))
BestTimeToParty(sched, ystart, yend)

