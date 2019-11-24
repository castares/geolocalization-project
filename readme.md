# Geoindexing and MongoDB project: Finding a new office for your recently acquired gaming company.

### The Project:

This project is part of Ironhack's Data Analytics Bootcamp. The objective is to find the best localization for a new office to a hypothetical gaming company. To start, we got [a kaggle's dataset with companies information from Crunchbase](https://www.kaggle.com/mauriciocap/crunchbase2013) and a wishlist from the employees with requirements for the localization.

### The Code:

1. __create_collections.py__ produces a MongoDB collection inside our original Companies database, with all the available offices at the original dataset on a standard GeoJSON format. Also creates other collections that will be used later. 

2. __companiesdb.py__ analyzes the collection created above, using both Pymongo and standard Python code, to define a set of target locations, near corporations and near tech startups.

3. __google_api_requests.py__ takes a target_offices.json file created on step 2 to request to Google Places API some locations required to be in our optimal office area.  

4. __ranking.py__ processes the output from both *companiesdb.py* and *google_api_requests.py* on a Pandas dataframe to rank the target locations following the employees wishlist. 

### The result:

As a result of these process, and looking for an office in Great Britain, we found an optimal area in west London, as you can see on the map below. The code for creating the map and the ranking process can be found on the folium.ipynb file. 

![Folium Map Screenshot](./output/folium_localization.png)