import sys
def main(filename):
    try:
        f = open(filename,mode="rt",encoding="UTF-8")
        for line in f:
            sys.stdout.write(line)
    finally:
        f.close()
    
if __name__ == '__main__':
    main(sys.argv[1])