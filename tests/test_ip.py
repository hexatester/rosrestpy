from ros import Ros, IPModule
from ros.ip import Address, ARP, Cloud, DHCPClient, DHCPRelay, DHCPServerModule
from ros.ip.dhcp_server import DHCPServer, DHCPNetwork, DHCPLease
from ros.ip.dns import DNS, DNSCache, DNSStatic
from ros.ip.firewall import (
    IPFirewallModule,
    IPFirewallFilter,
    IPFirewallMangle,
    IPFirewallNAT,
)
from ros.ip.hotspot import (
    HotspotModule,
    HotspotProfile,
    HotspotServer,
    HotspotUserModule,
    HotspotUser,
    HotspotActive,
    HotspotHost,
)
from ros.ip.hotspot.user import HotspotUserModule, HotspotUser, HotspotUserProfile


class TestIP:
    def test_ip(self, ros: Ros):
        assert isinstance(ros.ip, IPModule)

    def test_address(self, ros: Ros):
        for address in ros.ip.address():
            assert isinstance(address, Address)

    def test_arp(self, ros: Ros):
        for arp in ros.ip.arp():
            assert isinstance(arp, ARP)

    def test_cloud(self, ros: Ros):
        assert isinstance(ros.ip.cloud, Cloud)

    def test_dhcp_client(self, ros: Ros):
        for client in ros.ip.dhcp_client():
            assert isinstance(client, DHCPClient)

    def test_dhcp_relay(self, ros: Ros):
        for relay in ros.ip.dhcp_relay():
            assert isinstance(relay, DHCPRelay)


class TestDHCPServer:
    def test_dhcp_server(self, ros: Ros):
        assert isinstance(ros.ip.dhcp_server, DHCPServerModule)

    def test_item(self, ros: Ros):
        for item in ros.ip.dhcp_server():
            assert isinstance(item, DHCPServer)

    def test_lease(self, ros: Ros):
        for item in ros.ip.dhcp_server.lease():
            assert isinstance(item, DHCPLease)

    def test_network(self, ros: Ros):
        for network in ros.ip.dhcp_server.network():
            assert isinstance(network, DHCPNetwork)


class TestDNS:
    def test_dns(self, ros: Ros):
        assert isinstance(ros.ip.dns, DNS)

    def test_cache(self, ros: Ros):
        for i in ros.ip.dns.cache():
            assert isinstance(i, DNSCache)

    def test_cache_flush(self, ros: Ros):
        assert ros.ip.dns.flush() is None

    def test_static(self, ros: Ros):
        for i in ros.ip.dns.static():
            assert isinstance(i, DNSStatic)


class TestIPFirewall:
    def test_firewall(self, ros: Ros):
        assert isinstance(ros.ip.firewall, IPFirewallModule)

    def test_firewall_filter(self, ros: Ros):
        for i in ros.ip.firewall.filter():
            assert isinstance(i, IPFirewallFilter)

    def test_firewall_mangle(self, ros: Ros):
        for i in ros.ip.firewall.mangle():
            assert isinstance(i, IPFirewallMangle)

    def test_firewall_nat(self, ros: Ros):
        for i in ros.ip.firewall.nat():
            assert isinstance(i, IPFirewallNAT)


class TestHotspot:
    def test_hotspot(self, ros: Ros):
        assert isinstance(ros.ip.hotspot, HotspotModule)

    def test_hotspot_list(self, ros: Ros):
        for i in ros.ip.hotspot():
            assert isinstance(i, HotspotServer)

    def test_hotspot_profile(self, ros: Ros):
        for i in ros.ip.hotspot.profile():
            assert isinstance(i, HotspotProfile)

    def test_hotspot_user(self, ros: Ros):
        assert isinstance(ros.ip.hotspot.user, HotspotUserModule)

    def test_hotspot_user_list(self, ros: Ros):
        for i in ros.ip.hotspot.user():
            assert isinstance(i, HotspotUser)

    def test_hotspot_user_profile(self, ros: Ros):
        for i in ros.ip.hotspot.user.profile():
            assert isinstance(i, HotspotUserProfile)

    def test_hotspot_active(self, ros: Ros):
        for i in ros.ip.hotspot.active():
            assert isinstance(i, HotspotActive)

    def test_hotspot_host(self, ros: Ros):
        for i in ros.ip.hotspot.host():
            assert isinstance(i, HotspotHost)
