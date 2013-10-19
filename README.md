Instacane
=========

This is a service that pulls tweeted Instagram photos (or anything really) from Twitter, pulls it's relevant Instagram data, and serves them out there for your viewing please.  The photos are displayed in a grid and change position with the ebb and flow of Twitter tweets/retweets.

It was made in the hours before Hurricane Irene in 2011 and redeployed for Hurricane Sandy in 2012 by [@chris_ackermann](http://twitter.com/chris_ackermann "Chris Ackermann") and [@petersng](http://twitter.com/petersng "Peter Ng").  This is much of the source code for it, cleaned up, and sanitized for the masses.  Please feel free to check it out, run it on your own, and submit improvements.

Here is some of the press about it:

* http://nyti.ms/16eBLis
* http://tcrn.ch/Tqpd3P
* http://huff.to/WVN66j
* http://cbsn.ws/PheEj2


---

You will need:

* Python 2.7
* Memcache
* MongoDB (Optional)
* Instagram API token
* Twitter API consumer key/secret, access token/secret

---

To fire it up the photo aggregator, you will need these pylibs:

* python-twitter
* python-instagram
* memcache
* requests
* pymongo

and to create two files:

* /path/to/instacane/instagram.token - 1 line, containing your Instagram access token.
* /path/to/instacane/twitter.token - 4 lines, containing your Twitter (in order) consumer key, consumer secret, access token, access token secret.

and run this:

    /path/to/instacane/load_photos.py

load_data.py makes the calls to Twitter and Instagram and loads the JSON data into memcache (for use with the web service) and archived into MongoDB.

---

To fire up the web service, you will need these pylibs:

* Tornado

and run this:

    /path/to/instacane/run_service.py -p <port>

The web service essentially pulls the recent data from memcache, runs it through the Tornado templating engine, and displays it.  You can run multiples of this service with different ports behind nginx, Apache, etc for better performance.   This has proven to be a pretty lightweight setup and has handled lots of traffic with one instance.

---

Possible improvements:

* Better, prettier, more dynamic UI w/no tables!
* Serve as static page, rather than via Nginx/Tornado.
* If served as static page, directly upload and serve from S3/Cloudfront, rather than worry about scaling instances/machines.
* Add support for Instagram video.
* Add support for Vines?

---

Copyright (C) 2013 Chris Ackermann + Peter S. Ng
