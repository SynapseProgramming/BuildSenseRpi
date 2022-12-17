import requests 

url = 'http://192.168.50.50:5000/api/v1/sensors/create'
testobj = {'Nodid' : 34,'Battery' : 69, 'X' : 1, 'Y' :2, 'Z' : 3, 'Time' : 12.3334, 'Sent' : False }
x = requests.post(url, json = testobj)
if bool(x.text) == True:
  print("this is true")
else:
  print("this is false")



