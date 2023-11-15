import urllib.request
import json

from youtube_concate.settings import API_KEY

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):
    api_key = API_KEY

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    # maxResults：最大的量 25
    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
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
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
print(video_list)