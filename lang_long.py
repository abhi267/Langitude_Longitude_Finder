import urllib
import json


#using google geocode API
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?address='
#enter your API key after &key="YOUR KEY" in place of **
key='&key=**'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    #Adding and appending url with key
    url = serviceurl + urllib.urlencode({'address': address}) + key
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #printing the entire retrived data
    print 'Retrieved',len(data),'characters'
    
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
