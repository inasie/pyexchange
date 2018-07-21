# -*- coding: utf-8 -*-
import requests
import json
import logging


class HttpUtil:
    """
    http util
    """

    def get(self, url, params=None):
        '''
        get request
        :param str url: url
        :param set params: parameters
        '''
        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            logging.error('get(%s) failed(%d)' % (url, resp.status_code))
            if resp.text is not None:
                logging.error('resp: %s' % resp.text)
            return None
        return json.loads(resp.text)
