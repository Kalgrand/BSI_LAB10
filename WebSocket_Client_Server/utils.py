def pad(s):
    pad = 16 - len(s) % 16
    return s + pad * chr(pad)

def unpad(s):
    offset = ord(s[-1])
    return s[:-offset]

def fill_to_block(message, size):
    reminder = len(message)%size
    if(reminder == 0):
        return message
    else:
        for i in range(0, size-reminder):
            message += " "
        return message
