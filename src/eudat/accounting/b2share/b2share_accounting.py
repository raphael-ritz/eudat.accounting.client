# Copyright (c) 2018 CSC - IT Center for Science Ltd.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests


class B2SHAREAccounting(object):

    def __init__(self, conf, logger):
        self.logger = logger
        self.url = conf.b2share_url
        self.community = conf.b2share_community

    def report(self, args):

        url = self.url + "/api/records/?q=community:" + self.community
        try:
            r = requests.get(url, verify=True)
        except requests.exceptions.RequestException as e:
            self.logger.error('get community records request failed:' + str(e))
            return 0, 0
        if r.status_code != requests.codes.ok:
            self.logger.warn('get community records status code:' + r.status_code)

        total_amount = 0
        for record in r.json()['hits']['hits']:
            if 'files' in record:
                for record_file in record['files']:
                    total_amount += record_file['size']

        return (r.json()['hits']['total'], total_amount) if (r.status_code == requests.codes.ok) else (0, 0)
