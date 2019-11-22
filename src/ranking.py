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
    ranking.rename(columns={
        'starbucks_2': 'Starbucks',
        'schools_2': 'Schools',
        'airports_2': 'Airports',
        'bars_2': 'Clubs'
    }, inplace=True)
    ranking['Ranking'] = (-(ranking['Companies Close'] * 43.5) + (ranking['Tech Startups'] * 30) + (ranking['Starbucks']
                                                                                                    * 10) + (ranking['Airports'] * 20) + (ranking['Clubs'] * 43.5))
    ranking.sort_values(by='Ranking', ascending=False, inplace=True)
    ranking.to_csv("../output/ranking.csv", index=False)
    print(ranking)


if __name__ == "__main__":
    main()
