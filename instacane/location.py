#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
location.py

Created by Chris Ackermann + Peter Ng on 2011-08-25.
Copyright (c) 2011 Chris Ackermann + Peter Ng. All rights reserved.

"""

import requests
import json


def get_location_gmaps(lat, lng):
    url = ('http://maps.google.com/maps/api/geocode/json?'
        'latlng=%s,%s&sensor=false' % (lat, lng))
    response = requests.get(url)
    loc_data = json.loads(response.text)
    if (loc_data['status'] == "OK"):
        formatted_location = loc_data['results'][0]['formatted_address']
        formatted_location = formatted_location[(
            formatted_location.find(",") + 2):len(formatted_location)]
        return formatted_location
    return {}


