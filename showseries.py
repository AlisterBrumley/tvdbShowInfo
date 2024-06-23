import tvdb_v4_official
import typer
from pprint import pprint


def main(key: str, tvdb_id: int):
    tvdb = tvdb_v4_official.TVDB()

    try:
        series = tvdb.get_series(tvdb_id, "default")
    except ValueError:
        print("ID incorrect or not correct type!")
        exit(1)

    pprint(series)


if __name__ == '__main__':
    typer.run(main)
