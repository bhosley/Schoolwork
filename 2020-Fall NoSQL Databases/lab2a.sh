#!/bin/bash
# Script for Lab 2 part a
# Brandon Hosley 17/Sep/2020

# Create a movie rental Riak key-alue store
# Bucket - 'movies'
# json - releasedate, runningtime, and genres
# key - NameOfMovieInPascalCase

# 1. Add six movies from at least 2 genres

# 2. Delete one of the movie records

# 3. Create 3 branches (East, West, South).
# 3. Bucket should be 'branches'
# 3. Value should be json with name of branch
# 3. Link each of the remaining five movies to at least one branch
# 3. At least one should link two branches
# 3. Come up with an intuitive riaktag (ex. 'holds')

# 4. Download a picture for one of the movies and 
#    add to a bucket names images with the key being image name
# 4. Then link to the corresponding movie

# 5. Run Querries Listing:
# 5. All of the buckets
# 5. All of the movies in a branch
# 5. The movie with the picture and its branch

# 6. Hostname in the file should be changed to 'http://riak:8098/riak/'