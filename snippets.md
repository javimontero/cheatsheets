# Code Snippets
[Pushover notifications](#Pushover-notifications)  
[Timestamp](#Timestamp)  
[Runtime](#Calculate-runtime-of-code)  
[Retention files](#retention-files)

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
		--form-string "title=$1"\
  		--form-string "message=$2" \
  		https://api.pushover.net/1/messages.json
}

pushover "Title" "Message"
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
__code to profile__
stop = timeit.default_timer()  
print ("Runtime: ", str(timedelta(seconds=stop-start)))
```

## Retention files
Bash script to mantain only specific number of files and delete the rest. If you have daily backup files, for example, this script allows you to control the maximun number of files you want to mantain.
```bash
#!/bin/bash

# Number of files to maintain
RETENTION=10

# Wildcard with absolute path
folder="/Users/grip/Downloads/*.pk"

# Number of files
nfiles=`ls ${folder} | wc -l`

# Number of files to delete
n=$(($nfiles-$RETENTION))

# Check if there are enough files to delete
if [ $n -lt 1 ]; then
	exit 3
fi

# Identify files to delete.
# ATTENTION: check and sort files accordingly
delete_files=`ls ${folder} | head -n ${n}`

# Delete files
for f in ${delete_files};do rm $f;done
```
