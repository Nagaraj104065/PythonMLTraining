import time;  # This is required to include time module.

ticks = time.time()

print(ticks)

localtime = time.localtime(time.time())
print "Local current time :", localtime.tm_mday