import os
# import io
import re
import sys
import re
import yaml
from pprint import pprint as pp
from datetime import datetime, timezone, timedelta 
from collections import OrderedDict

from feedgen.feed import FeedGenerator

import markdown


from invoke import task


SROOT = os.path.dirname(os.path.abspath(__file__))
PROOT = os.path.abspath(os.path.join(SROOT, os.pardir))
print(f"SROOT:{SROOT}\nPROOT:{PROOT}\n")

from collections import namedtuple
from loguru import logger as LOG

# 移除默认的日志处理器
LOG.remove()
# LOG.add(sys.stderr, level="WARNING")
LOG.add(sys.stdout, level="DEBUG")
# LOG.add(sys.stdout, level="INFO")
# LOG.add(sys.stdout, level="WARNING")
# LOG.add(sys.stdout, level="ERROR")

CONF = {
    #   self info,
    "project": "MkDocsFlusher",
    "desc": "support all mkdocs site need updating",
    "version": "25.4.3.2142",
    "author": "Zoom.Quiet",
    "feedback": "askDAMA@googlegroups.com",
    "license": "MIT@2025..",
    "rpath": "./src",
    "summ": "SUMMARY.md",
    "buri": "https://zoomquiet.io",
    "follow":"feedId:69052357719365632+userId:68573755406424064",
    "last": 7,
    "docs": "./docs",
    "cfyml": "mkdocs.yml",
}

Config = namedtuple("Config", CONF.keys())
CFG = Config(**CONF)