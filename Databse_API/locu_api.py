import urllib2
import json

locu_api_key = 'a82545d8c7a73021c0a1052c3e7346429fe7af69'

#url = 'https://api.locu.com/v1_0/venue/search/?country=india&region=Gujarat&category=Restaurant&api_key=a82545d8c7a73021c0a1052c3e7346429fe7af69'


def locu_search(query):
    print query
    api_key = locu_api_key
    url = 'https://api.locu.com/v1_0/venue/search/'
    search = query
    final_url = url + "?country=" + search + "&category=Restaurant" + "&api_key=" + api_key
    print final_url
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    print data
    return data

x = locu_search('india')
print "pratik"
print x
for item in x['objects']:
    print item['name']
    print item['phone']
