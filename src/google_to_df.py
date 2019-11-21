import companiesdb as comp
import pandas as pd
from collections import Counter


def countcollection(collection):
    db, coll = comp.connectCollection("companies", collection)
    items = list(db[collection].find())
    count = []
    for e in items:
        count.append(e['properties']['reference'])
    return count


def addtodf(count, column):
    x = Counter(count)
    items_df = pd.DataFrame.from_dict(x, orient='index')
    items_df = items_df.reset_index()
    items_df.columns = ['Name', column]
    return items_df


def main():
    ranking = pd.read_csv('../output/ranking.csv')
    collections = ['starbucks_2', 'schools_2', 'airports_2', 'bars_2']
    for e in collections:
        add = addtodf(countcollection(e), e)
        ranking = ranking.merge(add, how="inner", on='Name')
    print(ranking)


if __name__ == "__main__":
    main()
