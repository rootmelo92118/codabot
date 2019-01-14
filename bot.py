from Linephu.linepy import *
from Linephu.akad.ttypes import *

client = LINE()

oepoll = OEPoll(client)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.text.startswith("/invite "):
                str1 = find_between_r(msg.text, "/invite ", "")
                client.inviteIntoGroup(msg.to, [str1])
            else:
                pass
        else:
            pass
    except Exception as error:
        print(error)
        print("\n\nSEND_MESSAGE\n\n")
        return


oepoll.addOpInterruptWithDict({
    OpType.SEND_MESSAGE: SEND_MESSAGE
})

def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""


while True:
    oepoll.trace()
