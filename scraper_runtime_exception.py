#!/usr/bin/python
# -*- coding: utf8 -*-

"""
ScraperCLI実行時例外クラス
"""
class scraper_runtime_exception(Exception):
    def __init__(self):
        super(scraper_runtime_exception, self).__init__()

    def __init__(self, message):
        super(scraper_runtime_exception, self).__init__(message)