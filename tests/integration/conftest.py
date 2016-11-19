import contextlib
import os

import pytest
import transaction
import webtest
from sqlalchemy.orm import scoped_session

from pyramid_api import main
from pyramid_api import models
from pyramid_api.database import tables


@pytest.fixture
def testapp(app_settings):
    app = main({}, **app_settings)
    return webtest.TestApp(app)
