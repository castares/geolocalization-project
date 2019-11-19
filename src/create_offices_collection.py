from companiesdb import connectCollection


def main():
    db, coll = connectCollection('companies', 'companies')
    db.create_collection("offices")
    all_comps = list(coll.find({"deadpooled_year": {"$eq": None}}))
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
                        "category": e['category_code']
                    }
                }
                db.offices.insert_one(geoJSON)


if __name__ == "__main__":
    main()
