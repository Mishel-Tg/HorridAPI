# credit by @Mrz_bots

from .requests import Requests

class LLVA:
    def __init__(self, prompt, api_key):
        self.requests = Requests(api_key)
        self.prompt = prompt

    def generate_video(self):
        video_content = self.requests.get_video(self.prompt)
        with open("video.mp4", "wb") as f:
            f.write(video_content)
        return "video.mp4"
