# Code Snippets
[Pushover notifications](#Pushover-notifications)  
[Timestamp](#Timestamp)  
[Runtime](#Calculate-runtime-of-code)  
[Retention files](#retention-files)  
[Python argparse](#python-argparse)

## Pushover notifications
Send real time notification to the phone via pushover ([pushover.net](https://pushover.net)). Useful to inform of long process termination like machine learning training.  

### Bash 
```shell
#!/bin/bash
function pushover {
	curl -s \
  		--form-string "token=_INSERT_YOUR_TOKEN_HERE_" \
  		--form-string "user=_INSERT_YOUR_USER_HERE" \
		--form-string "title=$1"\
  		--form-string "message=$2" \
  		https://api.pushover.net/1/messages.json
}

# Check to see if a pipe exists on stdin.
if [ -p /dev/stdin ]; then
    # If we want to read the input line by line
    while IFS= read line; do
            msg=${line}
    done
    pushover $(hostname) ${msg}
fi

if [ $# -ne 1 ];then
	echo "Usage: $0 msg"
	exit 3
fi

pushover $(hostname) $1
```
Usage:  
`$ zip -T file.zip | pushover`   
or:  
`$ pushover msg`  

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

## Python argparse
'''python
import argparse

# General info
# https://pymotw.com/3/argparse/

# How to work with subparsers
# https://stackoverflow.com/questions/8250010/argparse-identify-which-subparser-was-used/9286586#9286586


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help="commands", dest="command")

# A list command
list_parser = subparsers.add_parser("list", help="List contents")
list_parser.add_argument("dirname", action="store", help="Directory to list")
# list_parser.set_defaults(command="list")
# A create command
create_parser = subparsers.add_parser("create", help="Create a directory")
create_parser.add_argument("dirname", action="store", help="New directory to create")
create_parser.add_argument(
    "--read-only",
    default=False,
    action="store_true",
    help="Set permissions to prevent writing to the directory",
)
# create_parser.set_defaults(command="create")

# A delete command
delete_parser = subparsers.add_parser("delete", help="Remove a directory")
delete_parser.add_argument("dirname", action="store", help="The directory to remove")
delete_parser.add_argument(
    "--recursive",
    "-r",
    default=False,
    action="store_true",
    help="Remove the contents of the directory, too",
)
# delete_parser.set_defaults(command="delete")

print(parser.parse_args())
'''