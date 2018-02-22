import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(u'eudat.accounting.b2share').version
except:
    #LOG.warning("Could not get the package version from pkg_resources")
    __version__ = 'unknown'