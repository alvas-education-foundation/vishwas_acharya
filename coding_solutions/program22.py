#Write a Python program to convert seconds today, hour ,minutes and seconds
time=float(input("Inputtimeinseconds:"))
day=time//(24*3600)
time=time%(24*3600)
hour=time//3600
time%=3600
minutes=time//60
time%=60
seconds=time
print("day:->%d"%(day))
print("hour:->%d"%(hour))
print("minutes:->%d"%(minutes))
print("seconds:->%d"%(seconds))
