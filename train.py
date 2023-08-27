to_int = lambda strings: [int(string) for string in strings]
with open("train.txt","r") as file:
    datas=[]
    for line in file:
        datas.append(to_int(line.split()))
    for data in datas:
        try:
            if int(data[0])>m:
                m=data[0]
            if int(data[1])>m:
                m=data[1]
        except:
            pass
    file.close()
#print(datas)

def check_corecting(exemplary_list,defective_list):
    pass
def creat_train_conter(colors,exemplary_list):
    train_conter=[[] for i in range(colors)]
    for number,i in enumerate(exemplary_list):
        train_conter[i-1].append(number)
    return train_conter

def maxmin(exemplary_list,defective_list,datas):
    ones=set()
    #train_conter=creat_train_conter(datas[0][3],exemplary_list)
    
    for number in range(len(exemplary_list)):
        continue_=False
        for i in ones:
            if i==number and exemplary_list[number]!=defective_list[0]:
                continue_=True
        if continue_:
            continue
        
        add_to_ones=[]
        copy_defective_list=defective_list.copy()
        copy_defective_list.pop(0)
        if exemplary_list[number]==defective_list[0]:
            for j_number in range(number+1,len(exemplary_list)):
                #print(copy_defective_list,j_number,exemplary_list[j_number],exemplary_list)
                if exemplary_list[j_number]==copy_defective_list[0]:
                    add_to_ones.append(j_number)
                    copy_defective_list.pop(0)
                if copy_defective_list==[]:
                    ones.add(number)
                    for i in add_to_ones:
                        ones.add(i)
                    break
                    
                    
        
    return ones

def aut_put(maxmin):
    aut_put_=[]
    last_number=-1
    for i in maxmin:
        if last_number+1==i:
            aut_put_.append(1)
        else:
            for j in range(1,i-last_number):
                aut_put_.append(0)
                last_number+=1
            if last_number+1==i:
                aut_put_.append(1)
        last_number=i
    return aut_put_
        
#print(creat_train_conter(3,datas[1]))
print(aut_put(maxmin(datas[1],datas[2],datas)))#,"odp do zadania!")
#print(maxmin(datas[1],datas[2],datas))