

db, offices = comp.connectCollection('companies', 'offices')
target = comp.target_offices(offices, 'USA', 2009, 1)
m = folium.Map()


def plotTargetOffices(target_companies):
    for company in target_companies:
        folium.Marker(location=company['geometry']['coordinates'][::-1],
                      radius=2,
                      icon=folium.Icon(icon='cloud', color='blue')).add_to(m)


db, starbucks = comp.connectCollection('companies', 'starbucks')
starbucks_list = list(starbucks.find())


def plotStarbucks(starbucks_list):
    for starbucks in starbucks_list:
        folium.Marker(location=[starbucks['geometry']['location']['lat'],
                                starbucks['geometry']['location']['lng']],
                      radius=2,
                      icon=folium.Icon(color='green')).add_to(m)
