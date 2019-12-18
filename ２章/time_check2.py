sched = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0),
        (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
        (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0),]

def checktime(schedule):
    best_time = 0
    maxcou = 0
    for i in schedule:
        count = 0
        for j in schedule:
            if j[0] <= i[0] and i[0] < j[1]:
                count += 1

            if count > maxcou:
                maxcou = count
                best_time = j[0]

    print(maxcou, best_time)

checktime(sched)