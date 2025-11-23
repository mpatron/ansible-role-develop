import pytest

def test_package_nginx_installed(host):
    pkg = host.package("nginx")
    assert pkg.is_installed

def test_nginx_running_and_enabled(host):
    service = host.service("nginx")
    assert service.is_running
    assert service.is_enabled
