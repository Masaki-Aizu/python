sched = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2),
        (7.5, 10.0, 3), (8.0, 9.0, 2), (8.0, 10.0, 1), (9.0, 12.0, 2),
        (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7),]

def BestTimeToParty(schedule):
    time = []
    for i in schedule:
        time.append((i[0], 'start', i[2]))
        time.append((i[1], 'end', i[2]))
    
    sort(time)
    max, best_time = choosetime(time)

    print('Best time to attend the party is as', best_time,'o\'clock',
        ':', max)

def sort(time):
    for ind in range(len(time) - 1):
        ism = ind
        for i in range(ind, len(time)):
            if time[ism] > time[i]:
                ism = i
        time[ind], time[ism] = time[ism], time[ind]

def choosetime(time):
    max_wei = 0

    count = 0
    weight = 0
    for i in time:
        #change
        if i[1] == 'start':
            count += 1
            weight += i[2]
        #change
        elif i[1] == 'end':
            count -= 1
            weight -= i[2]
        #change
        if weight > max_wei:
            max_wei = weight
            best_time = i[0]
    
    return max_wei, best_time

BestTimeToParty(sched)