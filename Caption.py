import urllib2
import HTMLParser
import xml.etree.cElementTree as et
import datetime
import math

parser = HTMLParser.HTMLParser()


class Snippet:

    def __init__(self, start, dur, vidid):
        self.videoid = vidid
        self.start = self.seconds_to_timestamp(math.floor(float(start)))
        self.duration = self.seconds_to_timestamp(math.ceil(float(dur)))

    def seconds_to_timestamp(self, secs):
        return str(datetime.timedelta(seconds=secs))


class Caption:

    API_LINK = "http://video.google.com/timedtext?lang=en&v="
    YOUTUBE_LINK = "https://www.youtube.com/watch?v="

    def __init__(self, video_id):
        self.url = self.API_LINK + video_id
        self.video_id = video_id
        self.badCaption = False
        try:
            self.raw_text = self.download()
            self.tree = et.fromstring(self.raw_text)
        except Exception, e:
            print e.message
            print self.url
            print 'Could not download caption from ' + Caption.YOUTUBE_LINK + video_id
            self.badCaption = True

    def download(self):
        content = urllib2.urlopen(self.url).read()
        return content.replace("\\n", " ").replace("&amp;#39;", "'")

    def find(self, query):
        if self.badCaption:
            return list()
        query = query.lower()
        results = list()
        count = 0
        for el in self.tree.findall('text'):
            if query in el.text.lower():
                print str(count) + " " + el.text
                results.append(
                    Snippet(el.attrib['start'], el.attrib['dur'], self.video_id))
        return results
