import pytest
from _pytest.main import Session


def pytest_collection_modifyitems(session: Session, config, items: list):
    items.reverse()
    session.items = items
