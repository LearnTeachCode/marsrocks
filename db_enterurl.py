#Grab URLs from NASA API with accompanying data (URL, imageid, timestamp) and populate into db
import urllib2
import json
import datetime
import re

from project import db
from project.models import Photo


#grabbing top-level urls
mainpage=urllib2.urlopen('http://json.jpl.nasa.gov/data.json')
mainpagefile=mainpage.read()
mainpagejson=json.loads(mainpagefile)
allrovers=mainpagejson.keys()

for rover in allrovers:
    imgurl=mainpagejson[rover]['image_manifest']

#grabbing second-level urls
    secondpage=urllib2.urlopen(imgurl)
    secondfile=secondpage.read()
    secondjson=json.loads(secondfile)

    solindex=0
    sollen=len(secondjson['sols'])
    # while(solindex<sollen):
    while(solindex<10):
        solurl=secondjson['sols'][solindex]['url']

#grabbing third-level urls
        url=urllib2.urlopen(solurl)
        datafile=url.read()
        jsonurl=json.loads(datafile)
        toplevelkeys=jsonurl.keys()

        listentries=[]
        listindex=0
        tlkindex = 0
        tlkarraylen=len(toplevelkeys)
        imgindex=0
        for tlk in toplevelkeys:
            if isinstance(jsonurl[tlk],list)==True:
                tlklen=len(jsonurl[tlk])
                if tlklen!=0:
                    while(tlkindex<tlklen):
                        imglen=len(jsonurl[tlk][tlkindex]['images'])
                        while(imgindex<imglen):
                            url=jsonurl[tlk][tlkindex]['images'][imgindex]['url']
                            imgid=jsonurl[tlk][tlkindex]['images'][imgindex]['imageid']
                            if 'time' in jsonurl[tlk][tlkindex]['images'][imgindex]:
                                timestamp=jsonurl[tlk][tlkindex]['images'][imgindex]['time']['creation_timestamp_utc']
                                # fixes the timestamp when a date from JSON is messed up
                                if re.match(r".{19}([Z])", timestamp):
                                    timestamp = timestamp[:19] + timestamp[20:]
                                if re.match(r".*?\d$", timestamp):
                                    timestamp = timestamp + 'Z'
                                #converting JSON time string into Python datetime object
                                create_date=datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
                            else:
                                create_date=None
                            data=[url,imgid,create_date]
                            print data
                            #inserting data into db
                            db.session.add(Photo(url,imgid,create_date))
                            imgindex=imgindex+1
                        tlkindex=tlkindex+1
                        imgindex=0
                    tlkindex=0
        solindex=solindex+1
#committing
db.session.commit()
