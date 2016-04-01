import pafy
from subprocess import call


class Downloader:
    count = 0

    def download(self, snippet, filename):
        if filename:
            filename += ".mp4"
        else:
            filename = str(Downloader.count) + "out.mp4"
            Downloader.count += 1
        self.createvideo(snippet.videoid, snippet.start,
                         snippet.duration, filename)

    def createvideo(self, id, starttime, duration, outputfile="out.mp4"):
        url = pafy.new(id).getbest().url
        starttime = starttime
        duration = duration
        cmd = ["ffmpeg", "-ss", starttime, "-i", url,
               "-t", duration, "-c", "copy", outputfile]
        call(cmd)
