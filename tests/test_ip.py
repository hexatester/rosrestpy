from ros import IPModule
from ros.ip import Address, ARP, Cloud, DHCPClient, DHCPRelay, DHCPServerModule
from ros.ip.dhcp_server import DHCPServer, DHCPNetwork
from ros.ip.dns import DNS, DNSCache, DNSStatic


class TestIP:
    def test_ip(self, ros):
        assert isinstance(ros.ip, IPModule)

    def test_address(self, ros):
        for address in ros.ip.address:
            assert isinstance(address, Address)

    def test_arp(self, ros):
        for arp in ros.ip.arp:
            assert isinstance(arp, ARP)

    def test_cloud(self, ros):
        assert isinstance(ros.ip.cloud, Cloud)

    def test_dhcp_client(self, ros):
        for client in ros.ip.dhcp_client:
            assert isinstance(client, DHCPClient)

    def test_dhcp_relay(self, ros):
        for relay in ros.ip.dhcp_relay:
            assert isinstance(relay, DHCPRelay)


class TestDHCPServer:
    def test_dhcp_server(self, ros):
        assert isinstance(ros.ip.dhcp_server, DHCPServerModule)

    def test_item(self, ros):
        for item in ros.ip.dhcp_server.print():
            assert isinstance(item, DHCPServer)

    def test_network(self, ros):
        for network in ros.ip.dhcp_server.network:
            assert isinstance(network, DHCPNetwork)


class TestDNS:
    def test_dns(self, ros):
        assert isinstance(ros.ip.dns, DNS)

    def test_cache(self, ros):
        for i in ros.ip.dns.cache:
            assert isinstance(i, DNSCache)

    def test_cache_flush(self, ros):
        assert ros.ip.dns.flush() is None

    def test_static(self, ros):
        for i in ros.ip.dns.static:
            assert isinstance(i, DNSStatic)
