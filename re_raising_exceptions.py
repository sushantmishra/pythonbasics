def convert(s):
    """ Convert to an int"""
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print("Convertion error : {}".format(str(e)))
    raise