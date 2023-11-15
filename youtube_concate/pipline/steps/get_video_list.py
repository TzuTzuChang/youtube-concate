import urllib.request
import json

from youtube_concate.pipline.steps.step import Step
from youtube_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, inputs):

        channel_id = inputs['channel_id']

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        # maxResults：最大的量 25
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            # 一頁一頁拿，會重複送請求
            # 當 resp 回傳沒有 nextPageToken 時，會噴錯，故做特例處理
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

        print(len(video_links))
        print(video_links)
        return video_links
