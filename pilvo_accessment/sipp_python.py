import datetime
import subprocess

process = subprocess.Popen('sipp phone.plivo.com -sf uac_send.xml -inf uac.csv -i 192.168.30.2 -p 7012 -m 1 -trace_screen -trace_msg -trace_err -trace_logs'.split(" "),stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
print("Process_id:",process.pid) 
process.wait()
file_name="uac_send_"+str(process.pid)+"_messages.log"


def call_summary(file_name):
  print("Call Summary of File name:",file_name)
  f=open(file_name,mode='r')
  lines=f.readlines()
  data=[]
  message = {}
  for line in lines:
     if line.startswith("----------------------------------------------- "):
       if len(message.keys()) == 3:
          data.append(message)
          message = {}
       time= line.split("- ")[1]
       message['time']= time[:-1]
     else:
       if line.startswith("UDP message received"):
         type = "received"
         message['type'] = type
       elif line.startswith("UDP message sent"):
         type = "sent" 
         message['type'] = type
       elif line.startswith("UDP message sent"):
         print(line)
     if line.startswith("INVITE"):
        message_type = "INVITE"
        message["message_type"]=message_type
     elif line.startswith("ACK"):
        message_type = "ACK"
        message["message_type"]=message_type
     elif line.startswith("BYE"):
        message_type = "BYE"
        message["message_type"]=message_type
     elif line.startswith("SIP/2.0 200 OK"):
        message_type = "200 OK"
        message["message_type"]=message_type
     elif line.startswith("SIP/2.0 183"):
        message_type = "183"
        message["message_type"]=message_type
  data.append(message)

  if data[0]['message_type']=="INVITE":
    print("Start Time is:",data[0]['time'])
    start_time=datetime.datetime.strptime(data[0]['time'],'%Y-%m-%d %H:%M:%S.%f')

  if data[4]['message_type']=="200 OK":
    print("Time Caller received 200 OK:",data[4]['time'])


  if data[7]['message_type']=="200 OK":
    print("Time Caller received 200 OK:",data[7]['time'])
    end_time=datetime.datetime.strptime(data[7]['time'],'%Y-%m-%d %H:%M:%S.%f')
  print("Total Duration",(end_time-start_time).seconds)



call_summary(file_name)

