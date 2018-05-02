burst = []

print ("Enter number of processes")

total = int(input())

for i in range(total):
    print("Burst time ")
    burst.append(int(input()))

print ("Process\t\tBurst\t\tArrival\t\t")


for i in range(total):
    print "p", i+1, "\t\t", burst[i], "\t\t\t0\t\t"
