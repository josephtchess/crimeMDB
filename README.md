[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XJErSDDc)

LINKS TO DATA:
Crime Data - 
https://catalog.data.gov/dataset/crime-data-from-2010-to-2019
https://catalog.data.gov/dataset/crime-data-from-2020-to-present
Movie Data - 
https://datasets.imdbws.com/

Reduced this data to only have movies that came out after Dec 31, 2009

Hello Guys! This is our IMDB movie and Crime database project!

We offer a wide variety (kinda) of queries the user can make to find movies and actors
Our special twist is that we extrapolate crime data that occured in the same year as movies and see how their genres and ratings correlate to those crimes!

To be able to run our 'application' (all in terminal on localhost) you just need the os package, sqlite3 package, and access to our database
to make the application run faster, it is highly recomended to run the given indexing python script that indexes all commonly used columns in our tables

Speaking of - our tables in the database are:
Crime Data - 2010 onwards in LA,
Movie information - 2010 onwards,
Actors/writers/directors information,
Relations table between actor info and movie info - where rows contain a movieID and a nameID until all actor IDs for a given movie have been listed, then moves on to the next movie,
Ratings - holds the ratings for a movie

After you have the database and applied indexing, all you need to do is run the client and follow the prompts
These prompts let you choose between just getting info on movies, or getting some interesting, highly inaccurate generalizations between the relations of certain movies and certain crimes.

----------------------------

TLDR
++++++++++++++++++++++++++++
DOWNLOAD client.py     }
DOWNLOAD makeIndexing.py  } --- SAME DIRECTORY       
DOWNLOAD IMBD.db       } 
INSTALL sqlite3 PACKAGE
INSTALL os.path PACKAGE
RUN makeIndexing.py
RUN client.py : )

Collaborators:
Anthony Roytenberg
Joseph Tarantin
