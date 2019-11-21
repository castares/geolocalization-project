from companiesdb import connectCollection


def main():
    # Connects to the database
    db, coll = connectCollection('companies', 'companies')
    # Creates a new collection extracting all the offices from non deadpooled companies.
    db.create_collection("offices")
    all_comps = list(coll.find())
    for e in all_comps:
        for office in e['offices']:
            latitude = office['latitude']
            longitude = office['longitude']
            if latitude and longitude:
                print(latitude, longitude)
                geoJSON = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(longitude), float(latitude)]
                    },
                    "properties": {
                        "name": e["name"],
                        "country": office["country_code"],
                        "company_money_raised": e['total_money_raised'],
                        "foundation_year": e["founded_year"],
                        "category": e['category_code'],
                        "deadpooled_year": e['deadpooled_year']}
                }
                db.offices.insert_one(geoJSON)
    # Create new collections:
    db.create_collection("starbucks")
    db.create_collection("schools")
    db.create_collection("airports")
    db.create_collection("bars")


if __name__ == "__main__":
    main()
