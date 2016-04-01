import urllib2
import json


class Search:
    API_KEY = ""
    VIDEOS_TO_GET = 50

    @staticmethod
    def search(query):
        url = Search.construct_url(query)
        print url
        result_list = json.loads(urllib2.urlopen(url).read())["items"]
        print result_list
        return [x["id"]["videoId"] for x in result_list]

    @staticmethod
    def construct_url(query):
        return "https://www.googleapis.com/youtube/v3/search?key=" + Search.API_KEY +\
            "&part=snippet&relevanceLanguage=en&maxResults=" + str(Search.VIDEOS_TO_GET) + \
            "&type=video&videoCaption=closedCaption" + \
            "&q=" + urllib2.quote(query)
