import tvdb_v4_official
import typer
from pprint import pprint


def type_switch(db, type, id):
    match type:
        case "series":
            return db.get_series(id)
        case "company":
            return db.get_company(id)
        case "list":
            return  # RE RUN SEARCH THROUGH LIST
        case "movie":
            return db.get_movie(id)
        case "person":
            return db.get_person(id)
    # THESE SHOULD NOT OCCUR, UNCOMMENT TO RE-ENABLE
        # case "season":
        #     return db.get_season(id)
        # case "episode":
        #     return db.get_episode(id)
        # case "artwork":
        #     return db.get_artwork(id)
        # case "character":
        #     return db.get_character(id)


def main(key: str):
    tvdb = tvdb_v4_official.TVDB(key)

    query = input("Search: ")

    if not query:
        print("no search term entered! exiting...")
        exit(1)

    results = tvdb.search(query)

    if not results:
        print("no results! exiting...")
        exit(1)

    for cnt, dict in enumerate(results):
        cnt = str(cnt)
        name = dict["name"]

        if not dict.get("year"):
            year = "[Year Missing]"
        else:
            year = dict["year"]

        year = dict["type"]

        print(cnt + ") " + name + " " + year)

    # TODO MAKE FNC AND RECURSIVE RUN UNTIL SELECTION IN RANGE
    selection = int(input("Selection: "))

    sel_type = results[selection]["type"]
    sel_id = results[selection]["tvdb_id"]

    # TESTING ONLY, TO REMOVE WHEN COMPLETE
    pprint(sel_type)

    info = type_switch(tvdb, sel_type, sel_id)

    pprint(info)


if __name__ == "__main__":
    typer.run(main)
