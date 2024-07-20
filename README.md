![logo](static/survivordata.png)

# Survivor

Flask app that displays data from the first 40 seasons of Survivor queried from an SQLite database.

## About

## Acknowledgments
I started this database with data from [Survivor Wiki](https://survivor.fandom.com/wiki/Main_Page), and added additional information to it.

## Contribute
If anyone is interested in keeping this project going, I've tried to design the site to be easily adaptable to new information. If someone simply wants to add new players and seasons to the existing columns, you can do that by cloning this repository and then updating the `survivor.db` file either through entering new queries or editing the `Survivor_Contestants.xlsx` file, deleting the current `survivor.db` file, and then running the `excel2sql.py` file. ***Note that this will only work with an `.xlsx` file.***

The only update to the code you need to make for simply adding players/seasons is to go into `queries.py` and change the variable `num_seasons` to match how many seasons are in the database. 

Once the database is updated send me a pull request. If all looks good and I merge the info and graphs should auto update with the new deploy.
