#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import logging
import requests
from bs4 import BeautifulSoup
from scraper_runtime_exception import scraper_runtime_exception

LOG = logging.getLogger('operator')
LOG_FORMAT = (
    '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')

"""
Main class, cli entry point
"""
class Main():

    @staticmethod
    def printHtmlTitle():

        # 引数がない場合例外をスロー
        if len(sys.argv) == 1:
            raise scraper_runtime_exception("引数が指定されていません。一つ以上の引数を指定してください。")

        url = sys.argv[1]
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        print(soup.title.string)

    