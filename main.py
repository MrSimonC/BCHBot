from slackclient import SlackClient
import time
import os


class RTM:
    def __init__(self):
        self.sc = SlackClient(os.environ['SLACK_BCHBOT'])
        print('Token is ' + os.environ['SLACK_BCHBOT'])
        self.event = None

    def start(self):
        if self.sc.rtm_connect():
            while True:
                events = self.sc.rtm_read()
                for event in events:
                    if self.directed_at_bot(event):
                        self.event = event
                        self.process()
                time.sleep(1)
        else:
            print('Connection Failed, invalid token?')

    @staticmethod
    def directed_at_bot(event):
        if 'type' in event \
                and event['type'] == 'message' \
                and 'bot_id' not in event \
                and 'text' in event \
                and (event['channel'][:1] == 'D'):
            return True
        return False

    def send(self, message, channel=None):
        if channel is None:
            channel = self.event['channel']
        self.sc.api_call('chat.postMessage', as_user=True, channel=channel, text=message)

    def process(self):
        input_message = self.event['text']
        self.send(input_message)

if __name__ == '__main__':
    print('Script Running')
    rtm = RTM()
    rtm.start()
