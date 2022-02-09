import random
event = 400
unscheduled = []
timeslots = []
roomnumber = []
prompt = []
random_scheduled = []
scheduled = []
students = 500
for i in range(0,10):
    roomnumber.append(i)
for i in range (0,45):
    timeslots.append(i)
for i in range (0,400):
    unscheduled.append(i)

for i in range(len(unscheduled)):
    assigned = [[x,y] for x, y in zip(unscheduled, timeslots)]
print(assigned)
for i in unscheduled:
    if unscheduled[i] not in assigned[:x]:
        print(unscheduled[i])
  #  i = random.choice(timeslots)
   # j = random.choice(roomnumber)
    #for num in [i,j]:
     #   random_scheduled =([[i,j]])
#random.shuffle(unscheduled)
ns = number of students //should be stored somewhere in your own code
e = number of events //should be stored somewhere in your own code

def check_conflict(e1, e2):
    for i in range(0, students):
        if student_event[i][e1] == 1 and student_event[i][e2] == 1:
            # print('Debug: conflict for events', e1, 'and', e2, 'found in student', (i+1))
            return 1
    return 0

for i in range(0, e):
    temp = []
    for j in range(0, e):
        if i == j:
            temp.append(0)
        elif i > j:
            temp.append(conflict_matrix[j][i])
        else:
            temp.append(check_conflict(i, j))
    conflict_matrix.append(temp)



