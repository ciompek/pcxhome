#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from project import config as cfg

#if __name__ == '__main__':
#    port = int(os.environ.get("PORT", 8080))
#    app.run('0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", cfg.server['port']))
	app.run('0.0.0.0', port=port, debug=cfg.server['debug'])
