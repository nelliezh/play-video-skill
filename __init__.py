from mycroft import MycroftSkill, intent_file_handler


class PlayVideo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('video.play.intent')
    def handle_video_play(self, message):
        self.speak_dialog('video.play')


def create_skill():
    return PlayVideo()

