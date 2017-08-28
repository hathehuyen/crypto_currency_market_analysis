#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class CoinMarketCap(object):
    _session = None
    __DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
    __DEFAULT_TIMEOUT = 120

    def __init__(self, base_url=__DEFAULT_BASE_URL, request_timeout=__DEFAULT_TIMEOUT):
        self.base_url = base_url
        self.request_timeout = request_timeout

    @property
    def session(self):
        if not self._session:
            self._session = requests.Session()
            self._session.headers.update({'Content-Type': 'application/json'})
            self._session.headers.update({'User-agent': 'coin market cap data mining'})
        return self._session

    def __request(self, endpoint, params):
        response_object = self.session.get(self.base_url + endpoint, params=params, timeout=self.request_timeout)

        if response_object.status_code != 200:
            raise Exception('Error, http status code is ', response_object.status_code)
        try:
            response = response_object.json()
        except:
            raise Exception("Could not parse response as JSON, response code was %s, bad json content was '%s'" % (
                response_object.status_code, response_object.content))

        return response

    def ticker(self, currency="", **kwargs):
        params = {}
        params.update(kwargs)
        response = self.__request('ticker/' + currency, params)
        return response

    def stats(self, **kwargs):
        params = {}
        params.update(kwargs)
        response = self.__request('global/', params)
        return response
