import tvdb_v4_official
import typer
import json
from pathlib import Path


def main(key: str, tvdb_id: int):

    tvdb = tvdb_v4_official.TVDB(key)

    outPath = Path.cwd() / "dump"
    outSeries = outPath / "series.json"
    outSE = outPath / "series_extended.json"

    # outSeries.touch()
    # outSE.touch()

    # # OUTPUTTING TO JSON
    # # TWO DIFFERENT WAYS OF DOING, DUMP AND DUMPS
    # # INDENT HAS TO BE >0 OTHERWISE IT PRINTS WEIRD
    # # ENSURE_ASCII HAS TO BE FALSE
    # # TO ENSURE NON-ENGLISH GETS PRINTED
    # DUMPS IS ACTUALLY FOR STRINGS
    # BUT WE CAN SEND IT TO A FILE
    series = tvdb.get_series(tvdb_id)
    outSeries.write_text(json.dumps(series, indent=4, ensure_ascii=False))

    # DUMPS IS SUPPOSED TO BE FOR FILES
    # BUT FILE HAS TO BE OPENED WITH 'W' FIRST
    series_extended = tvdb.get_series_extended(tvdb_id)
    json.dump(series_extended, outSE.open("w"), indent=4, ensure_ascii=False)

    series_episodes = tvdb.get_series_episodes(tvdb_id, "alternate")


if __name__ == "__main__":
    typer.run(main)
