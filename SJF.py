burst = []
name = []

print ("Enter number of processes")

total = int(input())

for i in range(total):
    print ("Enter process number")
    name.append(int(input()))
    print("Burst time ")
    burst.append(int(input()))

for i in range(total):
    for j in range(total - i - 1):
        if burst[j] > burst[j + 1]:
            temp = burst[j]
            burst[j] = burst[j + 1]
            burst[j + 1] = temp
            temp = name[j]
            name[j] = name[j + 1]
            name[j + 1] = temp

print ("Process\t\tArrival\t\tBurst\t\t")


for i in range(total):
    print "p", name[i], "\t\t", "0", "\t\t\t", burst[i], "\t\t"
