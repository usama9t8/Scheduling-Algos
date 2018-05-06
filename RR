process=int(input("how many processes you want to run? "))
quantumtime=int(input('enter quantum time ?'))
name=[]
arrivaltime=[]
bursttime=[]
for i in range(process):
    print('process ',i+1)
    print("enter the name of  process")
    name1=raw_input()
    name.append(name1)
    print("enter the arrival time of  process")
    arrive=int(input())
    arrivaltime.append(arrive)
    print("enter the burst time of  process")
    burst=int(input())
    bursttime.append(burst)


for i in range(process):
    for j in range(0,process-i-1):
        if arrivaltime[j]>arrivaltime[j+1]:
            temp=arrivaltime[j+1]
            arrivaltime[j+1]=arrivaltime[j]
            arrivaltime[j]=temp
            temp1=bursttime[j+1]
            bursttime[j+1]=bursttime[j]
            bursttime[j]=temp1
            temp2=name[j+1]
            name[j+1]=name[j]
            name[j]=temp2
quantum=[]
for i in range(len(bursttime)):
    quantum.append(quantumtime)
time=0
while not(len(bursttime)==0):
    if time>=arrivaltime[0]:
        if bursttime[0]<=quantum[0]:
            time=time+quantum[0]
            print('process ',name[0],'arrival time ',arrivaltime[0],' finish time ',time)
            del name[0]
            del bursttime[0]
            del quantum[0]
            del arrivaltime[0]
        elif bursttime[0]>quantum[0]:
            time+=quantum[0]
            bursttime[0]-=quantum[0]
            name.append(name[0])
            bursttime.append(bursttime[0])
            quantum.append(quantum[0])
            arrivaltime.append(arrivaltime[0])
            del name[0]
            del bursttime[0]
            del quantum[0]
            del arrivaltime[0]
    else:
        time+=1





