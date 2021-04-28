# Not solved yet
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    
    records = []
    
    for _ in range(int(input())):
        inner_list = []
        name = input()
        score = float(input())
        inner_list.append(name)
        inner_list.append(score)
        
        records.append(inner_list)
        
    print(records)
    #print(records[i][2])
    
    scores = []
    for i in range(len(records)):
        scores.append(records[i][1])
        
    print(scores) 
    scores.sort()
    print(scores)
    
    second_lowest = scores[2]
    print(second_lowest)
    
    # x = records.find([_, scores[2]])
    
    # x = [(el.index(second_lowest)) for i, el in enumerate(records) if second_lowest in el]
    
    # print(x)