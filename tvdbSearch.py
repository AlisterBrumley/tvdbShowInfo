import tvdb_v4_official
import typer
import urllib.error
from typing import Optional
from typing_extensions import Annotated
from pprint import pprint


# takes selection, checks typer and returns correct type info
def type_switch(db, type, id):
    match type:
        case "series":
            return db.get_series(id)
        case "company":
            return db.get_company(id)
        case "list":
            return db.get_list_extended(id)
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


# user query
def search_query():
    query = input("Search: ")

    if not query:
        return search_query()
    else:
        return query


# user select
def select(result_length):
    selection = input("Selection: ")

    if not selection:
        return select(result_length)

    # is int
    try:
        selection = int(selection)
    except ValueError:
        return select(result_length)

    if int(selection) >= result_length:
        return select(result_length)

    return selection


# prints search results
def res_print(res):
    for cnt, dict in enumerate(res):
        cnt = str(cnt).zfill(2)
        name = dict["name"]
        type = dict["type"]

        # using .get because it returns None if None rather then raising exception
        if not dict.get("year"):
            year = "----"
        else:
            year = dict["year"]

        print(cnt + ") " + year + " - " + type + " - " + name)


# prints lists
def list_print(db, list):
    info_list = []
    for cnt, dict in enumerate(list):
        cnt = str(cnt)

        if dict.get("seriesId"):
            id = dict["seriesId"]
            info = db.get_series(id)
            type = "series"
        elif dict.get("movieId"):
            id = dict["movieId"]
            info = db.get_movie(id)
            type = "movie"

        info_list.append(info)
        name = info["name"]
        year = info["year"]

        print(cnt + ") " + year + " - " + type + " - " + name)

    return info_list


def main(key: str, query: Annotated[Optional[str], typer.Argument()] = None):
    # init and auth
    try:
        tvdb = tvdb_v4_official.TVDB(key)
    except urllib.error.URLError as e:
        print("NETWORK ERROR!")
        print(e)
        exit(1)
    except Exception as e:
        print("UNKNOWN ERROR OCCURED:")
        print(e)
        exit(1)

    # asking the user for the query
    if query is None:
        query = search_query()

    # getting results from tvdb
    try:
        results = tvdb.search(query)
    except urllib.error.URLError as e:
        print("NETWORK ERROR!")
        print(e)
        exit(1)
    except Exception as e:
        print("UNKNOWN ERROR OCCURED:")
        print(e)
        exit(1)

    res_len = len(results)
    if not results:
        print("no results! exiting...")
        exit(1)

    # printing results
    res_print(results)

    # getting user selection
    selection = select(res_len)
    sel_type = results[selection]["type"]
    sel_id = results[selection]["tvdb_id"]

    # checking type and getting main info
    try:
        info = type_switch(tvdb, sel_type, sel_id)
    except urllib.error.URLError as e:
        print("NETWORK ERROR!")
        print(e)
        exit(1)
    except Exception as e:
        print("UNKNOWN ERROR OCCURED:")
        print(e)
        exit(1)

    # printing the info we got
    if sel_type != "list":
        pprint(info)
        exit(0)

    # if a list, continue to print the list and allow selection within that
    print("Selection is a list, contents as follows:")
    list_contents = info[0]["entities"]
    try:
        list_res = list_print(tvdb, list_contents)
    except urllib.error.URLError as e:
        print("NETWORK ERROR!")
        print(e)
        exit(1)
    except Exception as e:
        print("UNKNOWN ERROR OCCURED:")
        print(e)
        exit(1)

    list_len = len(list_res)
    list_sel = select(list_len)
    
    pprint(list_res[list_sel])


if __name__ == "__main__":
    typer.run(main)
