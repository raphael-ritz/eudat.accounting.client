# -*- coding: utf-8 -*-
"""
=================================
eudat.accounting.iRODScollectorPG
=================================

Command line handling
"""

import argparse
import logging
import sys

import psycopg2

from eudat.accounting.client import __version__, LOG, utils
from eudat.accounting.client.__main__ import Application as ApplicationBase

# copied from the script running at MPCDF at the moment
ICAT_CONNSTR = "dbname=ICAT"
# change the query because of the new resources-type
ICAT_QUERY = """SELECT r_meta_main.meta_attr_value as resource_id, COUNT(*) as num_objects, CAST(SUM(data_size) as bigint) as size
        FROM r_data_main
        JOIN r_objt_metamap ON (r_objt_metamap.object_id=r_data_main.coll_id)
        JOIN r_meta_main ON (r_meta_main.meta_id=r_objt_metamap.meta_id)
        WHERE r_meta_main.meta_attr_name = 'resource_id'
        AND r_data_main.data_path like  '/home/irodseud/%'
        GROUP BY r_meta_main.meta_attr_value"""

def row_to_record(row):
    return {
        'account': row['resource_id'],
        'number': row['num_objects'],
        'value': row['size'],
    } 


def main(argv=sys.argv):
    """Main function called from console command
    """
    logging.basicConfig(filename='.accounting.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    exit_code = 1
    try:
        app = Application(argv)
        app.run()
        exit_code = 0
    except KeyboardInterrupt:
        exit_code = 0
    except Exception as exc:
        LOG.exception(exc)
    sys.exit(exit_code)


class Application(ApplicationBase):
    """The main Application class of the old iRODScollector
    Signature is the same as for the simple client - except for 
    the required arguments."""

    def run(self):
        LOG.info("iRODScollectorPG called with: " + str(self.args))
        print "iRODScollectorPG called with: %s" % str(self.args)

        # Connect to ICAT
        conn = psycopg2.connect(ICAT_CONNSTR)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        # Query data from ICAT
        cur.execute(ICAT_QUERY)
        rows = cur.fetchall()
        records = [row_to_record(row) for row in rows]
        
        # Disconnect from ICAT
        cur.close()
        conn.close()

