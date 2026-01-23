import unittest
from agent_sdk.utils.url import parse_cli_url

class TestURLParsing(unittest.TestCase):
    
    def test_parse_port_only_url(self):
        host, port = parse_cli_url("8080")
        self.assertEqual(host, "localhost")
        self.assertEqual(port, 8080)

    def test_parse_full_url(self):
        host, port = parse_cli_url("http://127.0.0.1:3000")
        self.assertEqual(host, "127.0.0.1")
        self.assertEqual(port, 3000)
        
    def test_parse_tcp_url(self):
        host, port = parse_cli_url("tcp://localhost:9999")
        self.assertEqual(host, "localhost")
        self.assertEqual(port, 9999)

    def test_parse_implicit_host(self):
        host, port = parse_cli_url(":4000")
        self.assertEqual(host, "localhost")
        self.assertEqual(port, 4000)

    def test_invalid_url_format(self):
        with self.assertRaises(ValueError):
            parse_cli_url("not-a-url-or-port")

    def test_invalid_port_too_high(self):
        with self.assertRaises(ValueError):
            parse_cli_url("65536")

    def test_invalid_port_zero(self):
        with self.assertRaises(ValueError):
            parse_cli_url("0")

    def test_invalid_port_negative(self):
        with self.assertRaises(ValueError):
            parse_cli_url("-1")

    def test_parse_host_port_url(self):
        host, port = parse_cli_url("127.0.0.1:9000")
        self.assertEqual(host, "127.0.0.1")
        self.assertEqual(port, 9000)

    def test_parse_https_url(self):
        host, port = parse_cli_url("https://copilot.local:443")
        self.assertEqual(host, "copilot.local")
        self.assertEqual(port, 443)

if __name__ == "__main__":
    unittest.main()
