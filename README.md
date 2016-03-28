
Admin username: admin
Admin password: funinthesun

Task 1:

Add a Song model object, the cardinality should be "Many Songs to One Album".

Song has a few fields:

* Name - String, name of song
* length - Int, length of song in seconds
* author - String, author of song

Task 2:

Add a Json response.  when uri=  /album/xyz and content-type:application:json

returns the album details and all the songs in Json format.