#
# SortingHat settings for Bitergia Analytics Platform
#
# This file defines the required settings to run SortingHat
# for Bitergia Analytics Platform extending the default
# SortingHat settings.
#

from sortinghat.config.settings import *  # noqa: F403,F401

#
# OpenInfraID Oauth client keys
#

OPENINFRA_CLIENT_ID = os.environ.get('SORTINGHAT_OPENINFRA_CLIENT_ID', None)
OPENINFRA_CLIENT_SECRET = os.environ.get('SORTINGHAT_OPENINFRA_CLIENT_SECRET', None)

#
# Eclipse Foundation keys
#

ECLIPSE_FOUNDATION_USER_ID = os.environ.get('SORTINGHAT_ECLIPSE_FOUNDATION_USER_ID', None)
ECLIPSE_FOUNDATION_PASSWORD = os.environ.get('SORTINGHAT_ECLIPSE_FOUNDATION_PASSWORD', None)

#
# Trusted data sources for matching by username
#

MATCH_TRUSTED_SOURCES = os.environ.get('SORTINGHAT_MATCH_TRUSTED_SOURCES',
                                       'github,gitlab,slack,openinfra').split(',')
