#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
insta_gram.py

Created by Chris Ackermann + Peter Ng on 2011-08-25.
Copyright (C) 2013 Chris Ackermann + Peter Ng. All rights reserved.

"""

import requests
import json
from instagram.client import InstagramAPI
from urllib import quote


class Instagram(object):

    def __init__(self, *args, **kwargs):
        self.instagram = self._get_insta_gram()

    def get_image_metadata(self, instagram_surl):
        oembed_data = None
        try:
            oembed_data = self.get_image_ombed(instagram_surl)
        except Exception as reason:
            print("Error retrieving oembed data for %s, %s" % (instagram_surl, reason))

        media_data = None
        try:
            if oembed_data:
                media_data = self.instagram.media(oembed_data['media_id'])
        except Exception as reason:
            print("Error retrieving image metadata for %s, %s" % (
                instagram_surl, reason))

        return {
            'oembed': oembed_data,
            'media': media_data
        }

    def get_image_ombed(self, image_url):
        response = requests.get("http://api.instagram.com/oembed?url=%s" % quote(image_url))
        if response.status_code == 200:
            return json.loads(response.text)
        raise RuntimeError("Unable to retrieve oembed data, http response = %s" %
            (response.status_code))

    def _get_insta_gram(self):
        return InstagramAPI(access_token=self._get_instagram_token())

    def _get_instagram_token(self):
        readfile = open('instagram.token', 'rU')
        if readfile:
            token = readfile.read(-1)
            token = token.strip()
            if token is None or token == '':
                raise RuntimeError('No instagram token or file found!')
            return token
