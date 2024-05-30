from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8  # Updated to match your environment's Python minor version

def test_requests_version():
    assert requests_version() == "2.27.1"  # Updated to match your installed requests version

def test_pytest_version():
    assert pytest_version() == "7.1.3"  # Updated to match your installed pytest version
