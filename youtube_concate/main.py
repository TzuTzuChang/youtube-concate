from youtube_concate.pipline.steps.get_video_list import GetVideoList
from youtube_concate.pipline.pipline import Pipline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
        ]

    p = Pipline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
