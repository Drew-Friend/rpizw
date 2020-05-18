standin = False

def disabled():
    if standin:
        return True
    else:
        return False


def send_value(value):
    #replace print with a serial method eventually
    print("Value {}".format(value))