"""Test HTTPError class."""

import pytest
from src.exceptions import HTTPError


def test_http_error_attributes():
    """Test the basic behaviour of HTTPError class."""
    e = HTTPError(404, "Not found")
    assert e.status_code == 404
    assert e.error == "Not found"


def test_http_error_raise():
    """Test the basic behaviour of HTTPError class."""
    with pytest.raises(HTTPError) as e:
        raise HTTPError(404, "Not found")


def test_http_error_exception_handling():
    """Test the basic behaviour of HTTPError class."""
    try:
        raise HTTPError(404, "Not found")
    except HTTPError as e:
        print(e)
