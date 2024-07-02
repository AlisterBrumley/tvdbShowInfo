import tvdb_v4_official
import typer
import json
from pathlib import Path

#                       NOTES!!!!!!
# # OUTPUTTING TO JSON
# # TWO DIFFERENT WAYS OF DOING, DUMP AND DUMPS
# # INDENT HAS TO BE >0 OTHERWISE IT PRINTS WEIRD
# # ENSURE_ASCII HAS TO BE FALSE
# # TO ENSURE NON-ENGLISH GETS PRINTED
# DUMPS IS ACTUALLY FOR STRINGS
# BUT WE CAN SEND IT TO A FILE
# series = tvdb.get_series(tvdb_id)
# outSeries.write_text(json.dumps(series, indent=4, ensure_ascii=False))

# DUMPS IS SUPPOSED TO BE FOR FILES
# BUT FILE HAS TO BE OPENED WITH 'W' FIRST
# series_extended = tvdb.get_series_extended(tvdb_id)
# json.dump(series_extended, outSE.open("w"), indent=4, ensure_ascii=False)


def output(outfile, info):
    outfile.write_text(json.dumps(info, indent=4, ensure_ascii=False))


def main(key: str, tvdb_id: int):

    # #### AUTH
    tvdb = tvdb_v4_official.TVDB(key)

    # #### SET BASE PATH
    outPath = Path.cwd() / "dump"

    # #### SET OUT PATH
    # maybe define these all as part of a list and then iterate through writing them
    # , after made a tuple? why?
    # outSeries = outPath / "series.json"
    # outSEx = outPath / "series_extended.json"
    # outSEp = outPath / "series_episodes.json"
    # outSEpD = outPath / "series_episodes_default.json"
    # outSEpA = outPath / "series_episodes_alternate.json"
    # outSTr = outPath / "series_translation.json"
    out_list = [
        outPath / "series.json",
        outPath / "series_extended.json",
        outPath / "series_episodes.json",
        # outPath / "series_episodes_default.json",
        outPath / "series_episodes_alternate.json",
        outPath / "series_translation.json",
        # outPath / "series_next_aired.json",
    ]

    # #### GETTING INFO
    # series = tvdb.get_series(tvdb_id)
    # series_extended = tvdb.get_series_extended(tvdb_id)
    # series_episodes = tvdb.get_series_episodes(tvdb_id)
    # series_ep_def = tvdb.get_series_episodes(tvdb_id, "default")
    # series_ep_alt = tvdb.get_series_episodes(tvdb_id, "alternate")
    # series_tranlation = tvdb.get_series_translation(tvdb_id, "english") # NEED TO FIND CORRECT STR
    info_list = [
        tvdb.get_series(tvdb_id),
        tvdb.get_series_extended(tvdb_id),
        tvdb.get_series_episodes(tvdb_id),
        # tvdb.get_series_episodes(tvdb_id, "default"),  # Seems to be the same as above
        tvdb.get_series_episodes(tvdb_id, "alternate"),
        tvdb.get_series_translation(tvdb_id, "eng"),
        # tvdb.get_series_nextAired(tvdb_id),  # same data as series? check with currently airing show
    ]

    # #### OUTPUT INFO
    # outSeries.write_text(json.dumps(series, indent=4, ensure_ascii=False))
    # output(outSeries, series)
    # output(outSEx, series_extended)
    # output(outSEp, series_episodes)
    # LIST OUTPUT
    for out_path, info in zip(out_list, info_list):
        output(out_path, info)


if __name__ == "__main__":
    typer.run(main)
