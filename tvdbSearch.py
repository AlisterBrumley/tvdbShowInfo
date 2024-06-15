import tvdb_v4_official
import typer
from pprint import pprint


def main(key: str):
    tvdb = tvdb_v4_official.TVDB(key)

    query = input("Search: ")

    results = tvdb.search(query)

    for cnt, dict in enumerate(results):
        cnt = str(cnt)
        name = dict["name"]

        if not dict.get("year"):
            year = "[Year Missing]"
        else:
            year = dict["year"]

        print(cnt + ") " + name + " " + year)

    selection = int(input("Selection: "))
    # ONLY WORKS WITH SERIES CURRENTLY
    # HAVE TO CHECK ID FOR MOVIE/SERIES etc AND RETURN RESULT
    # OR TYPE?
    sel_result = tvdb.get_series(results[selection]["tvdb_id"])
    pprint(sel_result)


if __name__ == "__main__":
    typer.run(main)
