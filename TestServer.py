import urllib
# Tries to open the url with the params through the method specified
def fetch_url(url, params, method):
  params = urllib.urlencode(params)
  if method=="GET":
    f = urllib.urlopen(url+"?"+params)
  else:
    # Usually a POST
    f = urllib.urlopen(url, params)
  return (f.read(), f.code)

url = "http://google.com"
method = "POST"
params = {"Param1": "Value1"}

# Fetch the content and response code
[content, response_code] = fetch_url(url, params, method)

# Check if the server responded with a success code (200)
if (response_code == 200):
  print(content)
else:
  print(response_code)