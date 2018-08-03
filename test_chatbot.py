import pytest

input = [{'type': 'message', 'user': 'UC0NJ9KTJ', 'text': 'hello', 'client_msg_id': '572faa29-88b6-4a89-a004-889cfac2facd', 'team': 'TC1E6JZ6E', 'channel': 'DC2PUKQ7Q', 'event_ts': '1533204593.000059', 'ts': '1533204593.000059'}]

@pytest.fixture
def slackCommunication():
    from chatbot import slackCommunication
    return slackCommunication()

@pytest.fixture
def mainFunc():
    from chatbot import mainFunc
    return mainFunc()

#________Slack Communication Tests_________

def test_slackConnect(slackCommunication):
    assert slackCommunication.slackConnect() == True

def test_parseSlackInput(slackCommunication):
    assert slackCommunication.parseSlackInput(input, 'UC0NJ9KTJ') == ['UC0NJ9KTJ', 'hello', 'DC2PUKQ7Q']

def test_getBotID(slackCommunication):
    assert slackCommunication.getBotID('mybot') == 'UC17CHD44'

def test_writeToSlack(slackCommunication):
    assert slackCommunication.writeToSlack('UC0NJ9KTJ', 'Testing Message')['ok'] == True

@pytest.mark.skip(reason="Not Fully Implemented")
def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print(slackCommunication.slackReadRTM())


#__________Main Function tests__________

def test_takeAction_Message(mainFunc):
    input = ['UC0NJ9KTJ', 'hello', 'DC2PUKQ7Q']
    assert mainFunc.takeAction(input)

def test_takeAction_None(mainFunc):
    input = [None, None, None]
    assert mainFunc.takeAction(input)
