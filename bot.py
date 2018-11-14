from Linephu.linepy import *
from Linephu.akad.ttypes import *

client = LINE()

oepoll = OEPoll(client)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.text.startswith("更新: "):
                n = 2
                str1 = find_between_r(msg.text, "更新: ", "~")
                str2 = find_between_r(msg.text, "~", "")
                int3 = int(str1)
                int4 = int(str2)
                int5 = int3 + int4
                str6 = str(int5 / 2)
                client.sendMessage(msg.to, "!coda " + str6)
            else:
                pass
        else:
            pass
    except Exception as error:
        print(error)
        print("\n\nRECEIVE_MESSAGE\n\n")
        return


oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
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
