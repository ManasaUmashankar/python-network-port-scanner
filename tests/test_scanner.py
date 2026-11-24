from src.scanner import validate_port_range, validate_ip_address

def test_valid_port_range():
    assert validate_port_range(1, 100)


def test_invalid_port_zero():
    assert not validate_port_range(0, 100)


def test_invalid_port_above_limit():
    assert not validate_port_range(1, 70000)


def test_start_greater_than_end():
    assert not validate_port_range(100, 50)


def test_single_port():
    assert validate_port_range(80, 80)

def test_valid_ipv4_address():
    assert validate_ip_address("127.0.0.1")


def test_invalid_ip_address():
    assert not validate_ip_address("999.999.999.999")


def test_ipv6_address_rejected():
    assert not validate_ip_address("::1")


def test_port_range_within_1000_limit():
    assert validate_port_range(1, 1000)


def test_port_range_exceeding_1000_limit():
    assert not validate_port_range(1, 1001)