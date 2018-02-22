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

import psycopg2
import os


class B2SHAREAccounting(object):

    def __init__(self, conf):
        self.account = conf.account
        self.dbname = os.environ.get('B2SHARE_POSTGRESQL_DBNAME', conf.db_name)
        self.user = os.environ.get('B2SHARE_POSTGRESQL_USER', conf.db_user)
        self.password = os.environ.get('B2SHARE_POSTGRESQL_PASSWORD', conf.db_password)
        self.host = os.environ.get('B2SHARE_POSTGRESQL_HOST', conf.db_host)
        self.db_connect_info = 'host={0} dbname={1} user={2} password={3}'.format(self.host, self.dbname,
                                                                                  self.user, self.password)

    def report(self, args):
        db_conn = None
        accounting = {}

        try:
            db_conn = psycopg2.connect(self.db_connect_info)

            cur = db_conn.cursor()
            cur.execute("select id,json from records_metadata;")

            for record_id, record in cur:
                if record is None:
                        continue

                community = record['community']
                if community not in accounting:
                        accounting[community] = 1
                else:
                        accounting[community] += 1
            cur.close()

        except psycopg2.Error, e:
            print "Error", e

        finally:
            if db_conn:
                db_conn.close()

        return accounting[self.account], 0
