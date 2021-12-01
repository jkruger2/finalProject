import http.client
import json

conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': "e8add8818emsh375582548eaa496p11cec5jsnb2f8ec06618b"
    }
conn.request("GET", "/leaderboard/1/psn", headers=headers)
res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")
#print(data)
d = json.loads(data)
#print(d)

i=0
for i in range(0,10):
    toPrint = d['entries'][i]
    print(toPrint)