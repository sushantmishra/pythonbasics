def convert(s):
    """ Convert to an int"""
    x = -1
    try:
        x = int(s)
        print("Convertion succeeded! x=",x)
    except (ValueError,TypeError) as e:
        print("Convertion error : {}".format(str(e)))
    return x