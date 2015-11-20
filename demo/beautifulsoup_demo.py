from bs4 import BeautifulSoup as bs
import urllib2

target_stock = {
    'HSI',
}

'''
Google a specific stock and return a html string
'''
def query_page(stock):
    # TODO(Carlson): No any error handling nor and detection on the input
    target_url = ('https://www.google.com.hk/'
                  'webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=%s')
    target_url = target_url % stock
    response = urllib2.urlopen(target_url)
    html = response.read()
    return html

hsi = query_page('HSI')
soup = bs(hsi, 'html.parser')

import pdb
pdb.set_trace()
