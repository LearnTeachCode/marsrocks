import sys
import urllib2
import json

#grabbing top-level urls
mainpage=urllib2.urlopen('http://json.jpl.nasa.gov/data.json')
mainpagefile=mainpage.read()
mainpagejson=json.loads(mainpagefile)
allrovers=mainpagejson.keys()

for rover in allrovers:
        imgurl=mainpagejson[rover]['image_manifest']
        file = open(rover+".txt",'a')
        file.write("[")

#grabbing second-level urls
        secondpage=urllib2.urlopen(imgurl)
        secondfile=secondpage.read()
        secondjson=json.loads(secondfile)

        solindex=0
        sollen=len(secondjson['sols'])
        while(solindex<sollen):
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
                                else:
                                    timestamp="-"
                                data={}
                                data['url']=url
                                data['imageid']=imgid
                                data['created_at']=timestamp
                                datadump = json.dumps(data)
                                print datadump
                                file.write(datadump+',')
                                # listentries.append(data)
                                imgindex=imgindex+1
                            tlkindex=tlkindex+1
                            imgindex=0
                        tlkindex=0
            solindex=solindex+1
#printing list of dictionary entries into text file
        # for item in listentries:
        #     print>>file, item
        file.write("]")
        file.close()


