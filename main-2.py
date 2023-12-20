import os.path

if __name__ == '__main__':
    fn = 'fyx_chinamoney.csv'
    if not os.path.exists(fn):
        exit(0)
    f = open(fn, 'r')
    data = f.readlines()
    i = 0
    m = len(data)
    while i < m / 80 + 1:
        d = data[i * 80: i * 80 + 80]
        if len(d) == 0:
            break
        print(d)
        i += 1
    f.close()
