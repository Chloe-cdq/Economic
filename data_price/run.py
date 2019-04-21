#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database import *
from network import *
from plot import *

data=get_data_from_network()
create_database(data)
create_plot()
