import fitbit, json
import requests
import webbrowser

tokenfile = "user_settings.txt"

z = fitbit.Fitbit();
try:
    token = json.load(open(tokenfile))
    auth_url = z.GetAuthorizationUri()
except:
    auth_url = z.GetAuthorizationUri()
    webbrowser.open(auth_url)
