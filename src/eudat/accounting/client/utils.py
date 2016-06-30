# utilties module from eudat.accounting.client
# collects methods that could be useful for client code as well

USERKEY = "ACCOUNTING_USER"
PWKEY = "ACCOUNTING_PW"

import os
import sys
from eudat.accounting.client import LOG

def getCredentials(args):
    """Extracts and returns (username, password) from args.
    Looks into environment varaibles ACCOUNTING_USER and
    ACCOUNTING_PW respectively if not found in args.
    Terminates if not found"""

    user = args.user
    if not user:
        user = os.getenv(USERKEY)
    pw = args.password
    if not pw:
        pw = os.getenv(PWKEY)

    if not user:
        msg = "No user id provided"
        LOG.error(msg)
        sys.exit(msg)
    if not pw:
        msg = "No password provided"
        LOG.error(msg)
        sys.exit(msg)
    LOG.info("Credentials found")
    return (user, pw)
