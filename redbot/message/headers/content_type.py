#!/usr/bin/env python

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2008-2013 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import redbot.speak as rs
from redbot.message import headers as rh
from redbot.message import http_syntax as syntax


@rh.GenericHeaderSyntax
@rh.CheckFieldSyntax(
    r'(?:%(TOKEN)s/%(TOKEN)s(?:\s*;\s*%(PARAMETER)s)*)' % syntax.__dict__,
    rh.rfc2616 % "sec-14.17"
)
def parse(subject, value, red):
    try:
        media_type, params = value.split(";", 1)
    except ValueError:
        media_type, params = value, ''
    media_type = media_type.lower()
    param_dict = rh.parse_params(red, subject, params, ['charset'])
    # TODO: check charset to see if it's known
    return (media_type, param_dict)
    
@rh.SingleFieldValue
def join(subject, values, red):
    return values[-1]
    
class BasicCTTest(rh.HeaderTest):
    name = 'Content-Type'
    inputs = ['text/plain; charset=utf-8']
    expected_out = ("text/plain", {"charset": "utf-8"})
    expected_err = []