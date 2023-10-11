# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:16:36 2021

@author: Kiran
"""

import MySQLdb

connection = MySQLdb.connect(host='localhost',
                             database='pythonappdb',
                             user='root',password='secret')

print(connection)

