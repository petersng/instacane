#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
twit_ter.py

Created by Chris Ackermann + Peter Ng on 2011-08-25.
Copyright (c) 2011 Chris Ackermann + Peter Ng. All rights reserved.

"""

import twitter


class Twitter(object):

    def __init__(self, *args, **kwargs):
        self.twitter = self._get_twitter()

    def search(self, query, num_pages=3):
        all_results = []
        results = self.twitter.GetSearch(
            query, count=100, result_type='mixed')
        all_results, max_id = self._append_page(all_results,
            results, results[0].id)
        for i in range(0, num_pages - 1):
            results = self.twitter.GetSearch(
                query, count=100, max_id=max_id, result_type='mixed')
            all_results, max_id = self._append_page(all_results, results, max_id)
        return all_results

    def _append_page(self, all_results, results, max_id):
        for result in results:
            all_results.append(result)
            if result.id < max_id:
                max_id = result.id
        return all_results, max_id

    def _get_twitter(self):
        (consumer_key, consumer_secret,
            access_token, access_token_secret) = self._get_twitter_tokens()
        return twitter.Api(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token,
            access_token_secret=access_token_secret
        )

    def _get_twitter_tokens(self):
        readfile = open('twitter.token', 'rU')
        if readfile:
            consumer_key = readfile.readline().strip()
            consumer_secret = readfile.readline().strip()
            access_token = readfile.readline().strip()
            access_token_secret = readfile.readline().strip()
            return (consumer_key, consumer_secret,
                    access_token, access_token_secret)
