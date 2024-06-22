import tvdb_v4_official
import typer
from typing import Optional
from typing_extensions import Annotated
from pprint import pprint


def type_switch(db, type, id):
    match type:
        case "series":
            return db.get_series(id)
        case "company":
            return db.get_company(id)
        case "list":
            return db.get_list(id)
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


def search_query():
    query = input("Search: ")

    if not query:
        return search_query()
    else:
        return query


def select():
    selection = input("Selection: ")

    if not selection:
        return select()

    try:
        return int(selection)
    except ValueError:
        return select()


def main(key: str, query: Annotated[Optional[str], typer.Argument()] = None):
    # init and auth
    tvdb = tvdb_v4_official.TVDB(key)

    # asking the user for the query
    if query is None:
        query = search_query()

    # getting results from tvdb
    results = tvdb.search(query)
    if not results:
        print("no results! exiting...")
        exit(1)

    # printing results
    for cnt, dict in enumerate(results):
        cnt = str(cnt)
        name = dict["name"]

        if not dict.get("year"):
            year = "[Year Missing]"
        else:
            year = dict["year"]

        print(cnt + ") " + name + " " + year)

    # getting user selection
    selection = select()
    # TESTING ONLY, TO REMOVE WHEN COMPLETE
    pprint(selection)

    # getting basic info about selection
    sel_type = results[selection]["type"]
    sel_id = results[selection]["tvdb_id"]

    # TESTING ONLY, TO REMOVE WHEN COMPLETE
    # pprint(sel_type)

    # checking type and getting main info
    info = type_switch(tvdb, sel_type, sel_id)

    # printing the info we got
    pprint(info)


if __name__ == "__main__":
    typer.run(main)
