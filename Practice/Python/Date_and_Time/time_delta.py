from datetime import datetime as dt
if __name__ == '__main__':
    fmt = "%a %d %b %Y %H:%M:%S %z"
    for _ in range(int(input())):
        print(int(abs((dt.strptime(input(), fmt) - dt.strptime(input(), fmt)).total_seconds())))
