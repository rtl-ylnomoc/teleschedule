from os import environ
# env vars are added in config.cfg like that:
# [{KEY}]
# {VALUE}
with open('config.cfg') as f:
    lines = f.readlines()
    [environ.update([(lines[i].strip()[1:-1], lines[i+1].strip())]) for i in range(0, len(lines), 2)]


if __name__ == '__main__':
    import source # start script