#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
run_service.py

Created by Chris Ackermann + Peter Ng on 2013-10-01.
Copyright (c) 2013 Chris Ackermann + Peter Ng. All rights reserved.

"""

import tornado
from tornado.web import Application


def run_service(port=8080):
    from instacane.handlers import InstacaneHandler
    from instacane.handlers import InstacaneFeedHandler

    settings = {}
    app = Application([
        (r"/", InstacaneHandler),
        (r"/feed", InstacaneFeedHandler)
    ], **settings)
    http = tornado.httpserver.HTTPServer(app)
    http.bind(port)
    http.start(1)

    print("Instacane is running on port %s" % port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run_service()
