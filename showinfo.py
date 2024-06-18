import tvdb_v4_official
import typer
from pprint import pprint


def main(key: str, tvdb_id: int):
    tvdb = tvdb_v4_official.TVDB(key)

    series = tvdb.get_series(tvdb_id, "default")
    pprint(series)


if __name__ == '__main__':
    typer.run(main)
