import tvdb_v4_official
from pprint import pprint


def main():
    tvdb = tvdb_v4_official.TVDB("0c337cac-4ac3-4a65-944f-ffcb1eb29a17")

    series = tvdb.get_series_episodes(78500, "alternate")["episodes"]

    for eps in series:
        pprint(eps)
        print("")


if __name__ == '__main__':
    main()
