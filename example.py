import fitbit, json
import requests

activityfile = "activity.txt"
tokenfile = "user_settings.txt"

z = fitbit.Fitbit();

# Try to read existing token pair
try:

    #token = json.load(open(tokenfile))
    #activity = json.load(open(activityfile))
    auth_url = z.GetAuthorizationUri()
    r = requests.get(auth_url)
    #print r.text

    #print r.text
    print "Please visit the link below and approve the app:\n %s" % auth_url
    # Set the access code that is part of the arguments of the callback URL FitBit redirects to.
    access_code = raw_input("Please enter code (from the URL you were redirected to): ")
    # Use the temporary access code to obtain a more permanent pair of tokens
    token = z.GetAccessToken(access_code)
    # Save the token to a file
    json.dump(token, open(tokenfile,'w'))

except IOError:
    # If not generate a new file
    # Get the authorization URL for user to complete in browser.
    auth_url = z.GetAuthorizationUri()
    #r = requests.get(auth_url)
    #print r.text
    print "Please visit the link below and approve the app:\n %s" % auth_url
    # Set the access code that is part of the arguments of the callback URL FitBit redirects to.
    access_code = raw_input("Please enter code (from the URL you were redirected to): ")
    # Use the temporary access code to obtain a more permanent pair of tokens
    token = z.GetAccessToken(access_code)
    # Save the token to a file
    json.dump(token, open(tokenfile,'w'))

# Sample API call
response = z.ApiCall(token, '/1/user/-/profile.json')

# Token is part of the response. Note that the token pair can change when a refresh is necessary.
# So we replace the current token with the response one and save it.
token = response['token']
json.dump(token, open(tokenfile,'w'))

activity = z.ApiCall(token, '/1/user/4QTKYC/activities/date/2016-06-23.json')
json.dump(activity, open(activityfile, 'w'))


# Do something with the response
