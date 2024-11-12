from VideoGen.llava import Requests

class LLVA:
    def __init__(self, prompt=None, api_key=None, **kwargs):
        if not prompt:
            raise ValueError("You Prompt was empty")
        if not api_key:
            raise ValueError("Where the api key you can get api key here https://t.me/XBOTSUPPORTS")
        self.requests = Requests(api_key)
        self.prompt = prompt

    def generate_video(self, **kwargs):
        video_content = self.requests.get_video(self.prompt)
        with open("video.mp4", "wb") as f:
            f.write(video_content)
        return "video.mp4"
