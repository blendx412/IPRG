def output(ip):
    of = open("ip.txt","a")
    of.write(ip+"\n")
    of.close()

def header(start,end):
    of = open("ip.txt","w")
    of.write("output file for ip list From:"+start+" To:"+end+"\n")
    of.write("===============================\n")
    of.close()

print """IP Address Range Generator
Usage: python ip.py
Enter Start range ip ( Ex: 192.168.12.0)
Enter End range ip ( Ex:192.168.12.255)
---------------------------------------
AliYazdani - SecurityTube.ir
=======================================
"""
start = raw_input("Enter Start ip:")
end = raw_input("Enter End ip:")
header(start,end)
s = start.split('.')
e = end.split('.')

r0 = int(e[0])-int(s[0])+1
r1 = int(e[1])-int(s[1])+1
r2 = int(e[2])-int(s[2])+1
r3 = int(e[3])-int(s[3])+1
c=0
print "ip.txt making...     please wait"
for i0 in range(int(s[0]),int(s[0])+r0):
    for i1 in range(int(s[1]),int(s[1])+r1):
        for i2 in range(int(s[2]),int(s[2])+r2):
            for i3 in range(int(s[3]),int(s[3])+r3):
                c = c+1
                res = str(i0)+"."+str(i1)+"."+str(i2)+"."+str(i3)
                output(res)
print "count ip = "+str(c)
print "The End"
