# -*- coding: utf-8 -*-
"""
Add your group member names here

"""

import csv
import pandas as pd


''' Create Variables here'''

# Lists
years = [] # Used in countYears dictionary
allGenres = [] # Used in Genre count
given = [] # Used in remove_duplicates function
sort = [] # List with variables not duplicated
# Dictionaries

moviesdict = {}
allMovies = {}

# File Variables
movies_small = open('movies_small.csv','r')
movies_small_content = movies_small.readlines()
genre_movies = open('genre_movies.txt','w')

# Write remove_duplicates function to remove duplicates from an input list

def remove_duplicates(given):
    removed = []
    #Takes a list and removes all duplicate items
    
    #Args: given = the list that we want duplicates removed from
    for i in given:
        if i not in removed:
            removed.append(i)
    removed.sort()
    return removed

# Write display_counts function to display movie year counts from an input dictionary

def display_counts(diction):
    print('Year','','','','Count')
    print('\n')
    
    for key, value in diction.items():
        print(key,'','','', value)
    

# Read movies_small.csv file as Dictionary

for line in movies_small_content:
    line = line.strip()
    value = line.split(',')
    moviesdict.update( {value[0]:value[1:3]})


    
    # Build countYears dictionary, allGenres list and allMovies dictionary from movie file 
    
    begin, end  = line.find('('), line.find(')')

    if begin != -1 and end != -1: 
        line = line[:begin] + line[end+1:] + " " + line[begin+1:end]
        year = line[-4:]
        year = str(year)
        if year.isnumeric():
            years.append(year)
countYears = {i:years.count(i) for i in years} # Builds dictionary of years and the count of movies


for line in movies_small_content: # Read each line in movies_small.csv
    line = line.strip()
    value = line.rsplit(',',1) # Takes the string left after the last comma
    value = value[1] # readjusts so value only includes Genres
    value = value.rsplit('|')
    allGenres = allGenres + value
    
    
for line in movies_small_content:
    line = line.strip()
    value = line.split(',')
    genre = value[-1]
    movie = value[1:-1]
    genre = genre.split('|')
    movie = ''.join(map(str,movie))
    allMovies.update({movie:genre})
    

    # use remove_duplicates function when building allGenres list

allGenres = remove_duplicates(allGenres)
allGenres = allGenres[0:-2]

    ### Part A: Display count of movies by year chronologically using display_counts function ###
'''
display_counts(countYears)
'''
    ### Part B: Output Movies with year by Genre Alphabetically to genre_movies.txt file ###
csv_reader = None
with open ('movies_small.csv') as csv_file:
    movies_small = list(csv.reader(csv_file, delimiter=','))

fp = open("genre_movies.txt", "w")
for genre in sorted(allGenres):
    genre_movies = []
    fp.write(genre + '\n')
    for row in movies_small[1:]:
        if len(row) == len(movies_small[0]):
            row = { movies_small[0] [i] : row[i] for i in range(len(movies_small[0]))}
            if genre in row['genres'].split('|'):
                genre_movies.append(row['title'])
    fp.write('\n'.join(sorted(genre_movies)) + "\n")
fp.close()


    # Create genre_movies.txt file to write and build countGenres dictionary from movie file
fp = open('movies_small.csv')
fp = fp.read()
for row in fp:
    if 

# Display genres with counts in descending order    

    
### Part C: Get total rating points for each movie and write to movie_ratings.txt file ###
# Read ratings_small.csv file
    
     # Build allRatings dictionary from rating file
     
     
     
     # Build avgRatings dictionary from allRatings dictionary 
     # and write movies with year, total ratings and counts to movie_ratings.txt file
     
     

# Display Top 10 movies with highest average ratings in descending order
