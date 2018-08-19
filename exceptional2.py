def convert(s):
    """ Convert to an int"""
    try:
        x = int(s)
        print("Convertion succeeded! x=",x)
    except ValueError:
        print("Convertion failed")
        x = -1    
    return x