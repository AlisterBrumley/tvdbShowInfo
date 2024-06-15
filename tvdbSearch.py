import tvdb_v4_official
from pprint import pprint


def main():
    tvdb = tvdb_v4_official.TVDB("0c337cac-4ac3-4a65-944f-ffcb1eb29a17")

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
    # HAVE TO CHECK ID FOR MOVIE/SERIES etc AND RETURN RESULT
    sel_result = tvdb.get_series(results[selection]["tvdb_id"])
    pprint(sel_result)


if __name__ == "__main__":
    main()
