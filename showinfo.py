import tvdb_v4_official
from pprint import pprint


def main():
    # NEEDS KEY
    tvdb = tvdb_v4_official.TVDB()

    series = tvdb.get_series_episodes(78500, "alternate")["episodes"]

    for eps in series:
        pprint(eps)
        print("")


if __name__ == '__main__':
    main()
