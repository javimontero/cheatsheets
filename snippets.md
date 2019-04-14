# Code Snippets

## Pushover notifications
Send real time notification to the phone via pushover ([pushover.net](https://pushover.net))

### Bash 
```
if [ $# -ne 1 ];then
	echo "Usage: $0 msg"
	exit 3
fi

function pushover {
	curl -s \
  		--form-string "token=<TOKEN>" \
  		--form-string "user=<USER>" \
  		--form-string "message=$1" \
  		https://api.pushover.net/1/messages.json
}

pushover "Message"
```
### Python
```
import http.client, urllib
def send_pushover (msg):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "_insert_your_token_here_",
        "user": "_insert_your_user_here",
        "message": msg,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
```
