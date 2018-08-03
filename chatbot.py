from slackclient import SlackClient
import time

class slackCommunication(object):

    def __init__(self):
        self.slack_client = SlackClient("xoxb-409482645218-409250591140-29KbeDlCk9fCs9o5cq68fpRa")
        self.appName = 'mybot'


    def slackConnect(self):
        return self.slack_client.rtm_connect()

    def slackReadRTM(self):
        #print(self.slack_client.rtm_read())
        return self.slack_client.rtm_read()

    def parseSlackInput(self, input, botID):
        botATID = botID
        if len(input) > 0:
            input = input[0]
            if 'text' in input and input['type'] == 'message':
                user = input['user']
                message = input['text']
                channel = input['channel']
                return [str(user), str(message), str(channel)]
            else:
                return [None, None, None]

    def getBotID(self, botusername):
        api_call = self.slack_client.api_call('users.list')
        users = api_call['members']
        for user in users:
            if 'name' in user and botusername in user.get('name') and not user.get('deleted'):
                return user.get('id')


    def writeToSlack(self,channel, message):
        return self.slack_client.api_call("chat.postMessage", channel = channel, text = message, as_user = True)


class mainFunc(slackCommunication):

    def __init__(self):
        super(mainFunc, self).__init__()
        botID = self.getBotID(self.appName)

    def takeAction(self, input):
        reply_message = ""
        greetings_words = ['hi', 'holla', 'hello', 'ssup', 'hey']
        if input:
            user, message, channel = input
            if message in greetings_words:
                reply_message = self.greeting_action(message)
            return self.writeToSlack(channel, reply_message)

    def greeting_action(self, message):
        return 'Hey I am the Bot :p'


    def run(self):
        self.slackConnect()
        botID = self.getBotID(self.appName)
        while True:
            print("Running...")
            self.takeAction(self.parseSlackInput(self.slackReadRTM(), botID))
            time.sleep(1)




if __name__ == '__main__':
    instance = mainFunc()
    instance.run()
