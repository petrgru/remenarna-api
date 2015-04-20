from  lxml.html import *
import urllib2
import os.path
#base_url='http://www.vskprofi.cz/vyhledavani?type=sku&search=PTFE53N&sku=OK'

def get_url_data(ordernum):
    base_url='http://www.vskprofi.cz/vyhledavani?type=sku&search='+ordernum+'&sku=OK'
    doc = parse(base_url).getroot()
    data=[]
    for div in doc.cssselect('td'):
        #print div.text_content()
        data.append(div.text_content())
    print data
    links = doc.xpath('//td/a/@href')
    file_links = [player for player in links]
    print file_links

    for link in file_links:
        if not os.path.exists(link):
            url = "http://www.vskprofi.cz" + link
            file = urllib2.urlopen(url)
            output = open('../..' + link,'wb')
            output.write(file.read())
            output.close()
    return data,file_links