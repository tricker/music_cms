###Overview

This is simple skeleton of a Django web app.  The subject matter is a simple Music Lover's CMS to track albums and
the songs on those albums.  It is runnable in it's current state. Your goal is to fill out the functionality.
  
First fork this github repo in your github account, then do all development in your fork.  When you are ready to submit
your work, issue a github pull request to the upstream master.

###Operating the App

First install Django!  then...

#####Start server

`python manage.py runserver`

#####Add a few albums

http://127.0.0.1:8000/admin/

#####See a list of all albums

http://127.0.0.1:8000/albums/

#####Admin creds

* username: admin
* password: funinthesun

###Task 1

Add a Song model object, and associate it to the Album object, the cardinality should be *Many Songs to One Album*.

Song has a few fields:

* Name - String, name of song
* length - Int, length of song in seconds
* author - String, author of song

###Task 2

Add a view for `/album/xyz` that displays the album's meta data as well as all of the associated songs from the model
you added in Task 1, where xyz is the primary key of the song. The first view that is already implemented: `/albums/`
has the view generation embedded in python code.  Be smarter in your new songs view and introduce a templating system.

###Task 3

Add a similar view as added in Task 2, but make this one return a json response. Use the same uri as Task 2: `/album/xyz`
Explore the concept of content negotiation.   This json response should contain both the album details as well as all
of the associated songs in Json format.

###Bonus Points:

Add unit tests

###Hints

I'm less concerned with visual layout / css/ javascript wizardry, 1997 web design palette is fine.  I'm looking for well
written python code and idiomatic use of Django.