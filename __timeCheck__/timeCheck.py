import time

def currentTime():
    timeStamp = (time.ctime().split(' ')[3]).split(':')[:-1]
    return timeStamp

def endTimer(timeStamp): 
    endTime = []
    if int(timeStamp[1]) != 0:
        num = 60 - int(timeStamp[1])
        endTime.append(int(timeStamp[0])+1)
        endTime.append(60-num)
    return endTime

timeStamp =currentTime()
endTime = endTimer(timeStamp)

while ((int(((time.ctime().split(' ')[3]).split(':')[:-1])[1])) < endTime[1]):
  time.sleep(10)
  print(time.ctime())

#take a snapshot of attendies and check for any comments after 30 mins of session 


#if the no of attendies halves after 45 min of lec then it will exit too 