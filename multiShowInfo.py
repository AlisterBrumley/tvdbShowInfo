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
    out_list = [
        outPath / "series.json",
        outPath / "series_extended.json",
        outPath / "series_episodes.json",
        # outPath / "series_episodes_default.json",
        outPath / "series_episodes_alternate.json",
        outPath / "series_translation.json",
        # outPath / "series_next_aired.json",
        # outPath / "seasons.json",
        # outPath / "seasons_extended.json",
        # outPath / "series_translation_alt.json",
        outPath / "episode.json",
        outPath / "episode_extended.json"
    ]

    # #### GETTING INFO
    info_list = [
        tvdb.get_series(tvdb_id),
        tvdb.get_series_extended(tvdb_id),
        tvdb.get_series_episodes(tvdb_id),
        # tvdb.get_series_episodes(tvdb_id, "default"),  # Seems to be the same as above
        tvdb.get_series_episodes(tvdb_id, "alternate"),
        tvdb.get_series_translation(tvdb_id, "eng"),
        # tvdb.get_series_nextAired(tvdb_id),  # same data as series? check with currently airing show
        # tvdb.get_season(tvdb_id), # needs season ID, not show ID
        # tvdb.get_season_extended(tvdb_id),
        # tvdb.get_series_translation(tvdb_id, "eng", "alternate"), # IS THERE A WAY TO GET ALT METADATA?
        tvdb.get_episode(9594346),
        tvdb.get_episode_extended(9594346),
    ]

    # #### OUTPUT INFO
    for out_path, info in zip(out_list, info_list):
        output(out_path, info)


if __name__ == "__main__":
    typer.run(main)
