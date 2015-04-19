#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Name:	    Least Significant Bits Processor
# Version:	0.1
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Zhi-Wei Cai.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import sys
import os.path
from PIL import Image

version = '0.1'
date    = 'Sunday, April 19, 2015 07:54 +0800'

print "LSB Processor v" + version + " (" + date + ")\nCopyright (c) 2015 Zhi-Wei Cai."

if len(sys.argv) < 2:
    sys.exit("Usage: python %s image_file" % os.path.basename(sys.argv[0]))

if not os.path.exists(sys.argv[1]):
    sys.exit("ERROR: File \"%s\" not found!" % sys.argv[1])

f, e = os.path.splitext(os.path.basename(sys.argv[1]))
f = 'lsb_' + f

p  = Image.open(sys.argv[1]).convert("RGB")
pa = p.copy()
pr = p.copy()
pg = p.copy()
pb = p.copy()

pax = pa.load()
prx = pr.load()
pgx = pg.load()
pbx = pb.load()

# Get the size of the image
w, h = p.size

# Process every pixel
for x in xrange(w):
    sys.stdout.write('\r >>> Processing image...\t(%2.f%%)' % float(x*100/w))
    sys.stdout.flush()
    for y in xrange(h):
        r, g, b = pax[x, y]
        k = r + g + b
        if k != 0:
            if 5 > r > 0:
                r = 255 - r
            if 5 > g > 0:
                g = 255 - g
            if 5 > b > 0:
                b = 255 - b
        pax[x, y] = (r, g, b)
        prx[x, y] = (r, 0, 0)
        pgx[x, y] = (0, g, 0)
        pbx[x, y] = (0, 0, b)

sys.stdout.write("\r >>> Exporting images...\t     ")
sys.stdout.flush()
pa.save(f + e)
pr.save(f + "_r" + e)
pg.save(f + "_g" + e)
pb.save(f + "_b" + e)

sys.stdout.write("\r >>> All done.          ")