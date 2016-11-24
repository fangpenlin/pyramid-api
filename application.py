from paste.deploy.config import PrefixMiddleware

import pyramid_api

application = pyramid_api.main({})

# handle proxing headers
application = PrefixMiddleware(application)
