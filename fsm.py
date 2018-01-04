import easygui
path=easygui.fileopenbox("select input file")
f=open(path,"r")
f.readline()
inp=int(f.readline().split()[1])
out=int(f.readline().split()[1])
states=int(f.readline().split()[1])
productions=int(f.readline().split()[1])
start=f.readline().split()[1]
print inp,out,states,productions,start

