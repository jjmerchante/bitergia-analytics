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
