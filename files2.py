import sys
def read_series(filename):
    with open(filename,mode="rt",encoding="UTF-8") as f:
        return [line.strip() for line in f]
    
def main(filename):
    print(read_series(filename))
    
if __name__ == '__main__':
    main(sys.argv[1])