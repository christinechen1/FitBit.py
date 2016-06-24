import fitbit, json
import requests
import webbrowser

tokenfile = "user_settings.txt"

z = fitbit.Fitbit();
try:
    auth_url = z.GetAuthorizationUri()
    webbrowser.open(auth_url)
    token = json.load(open(tokenfile))
    auth_url = z.GetAuthorizationUri()
    print "token already here"
except:
    auth_url = z.GetAuthorizationUri()
    webbrowser.open(auth_url)
