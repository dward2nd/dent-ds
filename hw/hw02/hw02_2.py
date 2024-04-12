def to_timestamp(raw_second):
    hour = raw_second // 3600
    raw_second -= hour * 3600

    minute = raw_second // 60
    raw_second -= minute * 60

    second = raw_second

    return f"{hour:02d}:{minute:02d}:{second:02d}"


if __name__ == "__main__":
    raw_second = int(input())
    print(to_timestamp(raw_second))
