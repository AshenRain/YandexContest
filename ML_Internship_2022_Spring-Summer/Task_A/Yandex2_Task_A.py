def zaraza(meetings, meet_zaraza, pcr, arhcive, id):
    #print('id', id)
    for worker in meetings[meet_zaraza][1:]:
        pcr[worker] = 1
        for meet in archive[worker][1:]:
            #print('kk ', meet)
            if meetings.get(meet, False):
                meetings[meet][0] = 1
                
            else: 
                meetings[meet] = [pcr[worker], worker]
            #Вычеркнуть митинг, на котором он был
            #print('rez be', archive[worker])
            archive[worker] = archive[worker][0:1] + archive[worker][2:]
            #print('rez af', archive[worker])
            zaraza(meetings, meet, pcr, archive, id + 1)
    #print('reverse end ', meetings)
            


fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()

n = int(text_line[0])
pcr = list(map(int, text_line[1].split()))
meetings = dict()
archive = dict()
index_worker = 0
#print(pcr)
for line in text_line[2:]:
    count_meeteings, *meet = map(int, line.split()) 
    archive[index_worker] = [count_meeteings]
    for i in range(count_meeteings):
        archive[index_worker].append(meet[i])
    index_worker +=1

index_worker = 0
for line in text_line[2:]:
    count_meeteings, *meet = map(int, line.split()) 
    for i in range(count_meeteings):
        if meetings.get(meet[i], False):
            if meetings[meet[i]][0] == 0 and pcr[index_worker] == 1:
                meetings[meet[i]][0] = 1
                meetings[meet[i]].append(index_worker)
                #вызов функции которая начинает ходить по всем посетителям втсречи
                zaraza(meetings, meet[i], pcr, archive, 0)
            if pcr[index_worker] == 0 and meetings[meet[i]][0] != 0:
                pcr[index_worker] = 1
                meetings[meet[i]].append(index_worker)
        else: 
            meetings[meet[i]] = [pcr[index_worker], index_worker]
    #print(count_meeteings, meet)
    index_worker +=1
print(*pcr)