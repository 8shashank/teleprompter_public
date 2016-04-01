from Caption import Caption
from Downloader import Downloader
from Search import Search


def runProgram(youtube_search_query, text_to_find):
    dl = Downloader()
    celeb_videos = Search.search(youtube_search_query)
    links = [Caption.YOUTUBE_LINK + x for x in celeb_videos]
    print links
    count = 0
    for videoid in celeb_videos:
        cap = Caption(videoid)
        results = cap.find(text_to_find)
        for result in results:
            dl.download(result, text_to_find + str(count))
            count += 1

runProgram("President Obama discusses", "Kenya")
