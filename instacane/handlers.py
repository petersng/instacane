#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
handlers.py

Created by Chris Ackermann + Peter Ng on 2011-08-25.
Copyright (C) 2013 Chris Ackermann + Peter Ng. All rights reserved.

"""

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.httpserver
import json
import memcache


class InstacaneHandler(tornado.web.RequestHandler):

    page_title = "#instacane"
    page_header = "#instacane"
    page_subheader = "the story of hurricane sandy told through instagram"

    def __init__(self, *args, **kwargs):
        super(InstacaneHandler, self).__init__(*args, **kwargs)

    def get(self):
        if (self.get_argument("caption", "no") == "yes"):
            captions_enabled = True
        else:
            captions_enabled = False

        mc = memcache.Client(['localhost:11211'], debug=0)
        latest_photos = json.loads(mc.get("latest_photos"))
        latest_ts = mc.get("latest_ts")

        self.render(
            '../templates/instacane.html', title=self.page_title,
            page_header=self.page_header, page_subheader=self.page_subheader,
            latest_photos=latest_photos, captions_enabled=captions_enabled,
            latest_ts=latest_ts)


class InstacaneFeedHandler(tornado.web.RequestHandler):

    def __init__(self, *args, **kwargs):
        super(InstacaneFeedHandler, self).__init__(*args, **kwargs)

    def get(self):
        mc = memcache.Client(['localhost:11211'], debug=0)
        latest_photos = json.loads(mc.get("latest_photos"))
        feed_data = json.dumps(latest_photos)
        self.set_header("Content-Type", "application/json")
        self.write(feed_data)
        self.finish()

