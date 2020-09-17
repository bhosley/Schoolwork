#!/bin/bash
# Script for Lab 2 part a
# Brandon Hosley 17/Sep/2020

# Create a movie rental Riak key-alue store
# Bucket - 'movies'
# json - releasedate, runningtime, and genres
# key - NameOfMovieInPascalCase

# 1. Add six movies from at least 2 genres
curl -v -X PUT http://riak:8098/riak/movies/OceansEleven -H "Content-Type: application/json" -d '{"genre" : "thriller", "releasedate" : "2001", "runningtime" : "1:56"}'
curl -v -X PUT http://riak:8098/riak/movies/TheDarkKnight -H "Content-Type: application/json" -d '{"genre" : "action", "releasedate" : "2008", "runningtime" : "2:32"}'
curl -v -X PUT http://riak:8098/riak/movies/SavingPrivateRyan -H "Content-Type: application/json" -d '{"genre" : "war", "releasedate" : "1998", "runningtime" : "2:49"}'
curl -v -X PUT http://riak:8098/riak/movies/HacksawRidge -H "Content-Type: application/json" -d '{"genre" : "war", "releasedate" : "2016", "runningtime" : "2:26"}'
curl -v -X PUT http://riak:8098/riak/movies/Inception -H "Content-Type: application/json" -d '{"genre" : "thriller", "releasedate" : "2010", "runningtime" : "2:28"}'
curl -v -X PUT http://riak:8098/riak/movies/Primer -H "Content-Type: application/json" -d '{"genre" : "thriller", "releasedate" : "2004", "runningtime" : "1:17"}'

# 2. Delete one of the movie records
curl -i -X DELETE http://riak:8098/riak/movies/TheDarkKnight

# 3. Create 3 branches (East, West, South).
#    Bucket should be 'branches'
#    Value should be json with name of branch
#    Link each of the remaining five movies to at least one branch
#    At least one should link two branches
#    Come up with an intuitive riaktag (ex. 'holds')
curl -X PUT http://riak:8098/riak/branches/East -H "Content-Type: application/json" -H "Link: \
</riak/movies/OceansEleven>;riaktag=\"holds\", \
</riak/movies/SavingPrivateRyan>;riaktag=\"holds\"" \ 
-d '{"branch" : "East"}'
#
curl -X PUT http://riak:8098/riak/branches/West -H "Content-Type: application/json" -H "Link: \
</riak/movies/HacksawRidge>;riaktag=\"holds\", \
</riak/movies/Inception>;riaktag=\"holds\"" \ 
-d '{"branch" : "West"}'
#
curl -X PUT http://riak:8098/riak/branches/South -H "Content-Type: application/json" -H "Link: \
</riak/movies/Primer>;riaktag=\"holds\", \
</riak/movies/Inception>;riaktag=\"holds\"" \ 
-d '{"branch" : "South"}'

# 4. Download a picture for one of the movies and 
wget --output-document=InceptionCover.jpg https://i.imgur.com/acUbMd5.jpg
#    add to a bucket names images with the key being image name
# 4. Then link to the corresponding movie
curl -X PUT http://riak:8098/riak/photos/InceptionCover.jpg -H "Content-type: image/jpeg" -H "Link: </riak/movies/Inception>; riaktag=\"photo\""  --data-binary @InceptionCover.jpg

# 5. Run Querries Listing:
# 5. All of the buckets
curl -X GET http://riak:8099/riak?buckets=true

# 5. All of the movies in a branch
curl http://riak:8098/riak/branches/East/movies,_,_ 

# 5. The movie with the picture and its branch

# 6. Hostname in the file should be changed to 'http://riak:8098/riak/'