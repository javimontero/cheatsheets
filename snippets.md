# Code Snippets
[Pushover notifications](#Pushover-notifications)  
[Timestamp](#Timestamp)  
[Runtime](#Calculate-runtime-of-code)

## Pushover notifications
Send real time notification to the phone via pushover ([pushover.net](https://pushover.net)). Usefull to inform of long process termination like machine learning training.  

### Bash 
```shell
if [ $# -ne 1 ];then
	echo "Usage: $0 msg"
	exit 3
fi

function pushover {
	curl -s \
  		--form-string "token=_INSERT_YOUR_TOKEN_HERE_" \
  		--form-string "user=_INSERT_YOUR_USER_HERE" \
  		--form-string "message=$1" \
  		https://api.pushover.net/1/messages.json
}

pushover "Message"
```
### Python
```python
import http.client, urllib
def send_pushover (msg):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "_INSERT_YOUR_TOKEN_HERE_",
        "user": "_INSERT_YOUR_USER_HERE",
        "message": msg,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
```
## Timestamp
Generate a timestamp including microseconds for a file name, for example.
```python
import datetime
fname = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S%f") + ".pk"
```
## Calculate runtime of code
```python
from datetime import datetime, timedelta
import timeit
start = timeit.default_timer()
``` 
Some code  
```python
stop = timeit.default_timer()  
print ("Runtime: ", str(timedelta(seconds=stop-start)))
```

