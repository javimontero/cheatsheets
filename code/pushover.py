def send_pushover(title="No title", msg="No message"):
    import http.client, urllib

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": "aajp5jkbq4yhmf5nk15cayvcipk8zt",
                "user": "uwug4i6nxuyfia4k58zqbug54f6z1f",
                "title": title,
                "message": msg,
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()