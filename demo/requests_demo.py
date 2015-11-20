import requests

def query_page(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return response
    except:
        print '404!!'
        return

print 'request 1:'
response = query_page('jiachengzhuo.com')
# Notice that this will return 404
# The reason is that, requests is quit stupid ... it will not add http:// itself

print 'request 2:'
response = query_page('http://jiachengzhuo.com')
print response
