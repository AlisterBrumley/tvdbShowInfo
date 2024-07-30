import tvdb_v4_official
import typer
from datetime import datetime
from pprint import pprint

# timing code for grabbing whole set vs part of set
def main(key: str):
    tvdb = tvdb_v4_official.TVDB(key)

    time = datetime.now()
    info = tvdb.get_episode_extended(9594346)
    elapsed_time = datetime.now() - time
    print(elapsed_time)

    ttime = datetime.now()
    infoo = tvdb.get_episode_extended(9594346)["companies"]
    elapsed_ttime = datetime.now() - ttime
    print(elapsed_ttime)


if __name__ == '__main__':
    typer.run(main)
