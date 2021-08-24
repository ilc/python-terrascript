#tests/test_provider_vmware_nsxt.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:33:27 UTC)

def test_provider_import():
    import terrascript.provider.vmware.nsxt


def test_resource_import():
    from terrascript.resource.vmware.nsxt import nsxt_algorithm_type_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_dhcp_relay_profile

    from terrascript.resource.vmware.nsxt import nsxt_dhcp_relay_service

    from terrascript.resource.vmware.nsxt import nsxt_dhcp_server_ip_pool

    from terrascript.resource.vmware.nsxt import nsxt_dhcp_server_profile

    from terrascript.resource.vmware.nsxt import nsxt_ether_type_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_firewall_section

    from terrascript.resource.vmware.nsxt import nsxt_icmp_type_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_igmp_type_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_ip_block

    from terrascript.resource.vmware.nsxt import nsxt_ip_block_subnet

    from terrascript.resource.vmware.nsxt import nsxt_ip_discovery_switching_profile

    from terrascript.resource.vmware.nsxt import nsxt_ip_pool

    from terrascript.resource.vmware.nsxt import nsxt_ip_pool_allocation_ip_address

    from terrascript.resource.vmware.nsxt import nsxt_ip_protocol_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_ip_set

    from terrascript.resource.vmware.nsxt import nsxt_l4_port_set_ns_service

    from terrascript.resource.vmware.nsxt import nsxt_lb_client_ssl_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_cookie_persistence_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_fast_tcp_application_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_fast_udp_application_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_application_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_forwarding_rule

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_request_rewrite_rule

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_response_rewrite_rule

    from terrascript.resource.vmware.nsxt import nsxt_lb_http_virtual_server

    from terrascript.resource.vmware.nsxt import nsxt_lb_https_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_icmp_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_passive_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_pool

    from terrascript.resource.vmware.nsxt import nsxt_lb_server_ssl_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_service

    from terrascript.resource.vmware.nsxt import nsxt_lb_source_ip_persistence_profile

    from terrascript.resource.vmware.nsxt import nsxt_lb_tcp_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_tcp_virtual_server

    from terrascript.resource.vmware.nsxt import nsxt_lb_udp_monitor

    from terrascript.resource.vmware.nsxt import nsxt_lb_udp_virtual_server

    from terrascript.resource.vmware.nsxt import nsxt_logical_dhcp_port

    from terrascript.resource.vmware.nsxt import nsxt_logical_dhcp_server

    from terrascript.resource.vmware.nsxt import nsxt_logical_port

    from terrascript.resource.vmware.nsxt import nsxt_logical_router_centralized_service_port

    from terrascript.resource.vmware.nsxt import nsxt_logical_router_downlink_port

    from terrascript.resource.vmware.nsxt import nsxt_logical_router_link_port_on_tier0

    from terrascript.resource.vmware.nsxt import nsxt_logical_router_link_port_on_tier1

    from terrascript.resource.vmware.nsxt import nsxt_logical_switch

    from terrascript.resource.vmware.nsxt import nsxt_logical_tier0_router

    from terrascript.resource.vmware.nsxt import nsxt_logical_tier1_router

    from terrascript.resource.vmware.nsxt import nsxt_mac_management_switching_profile

    from terrascript.resource.vmware.nsxt import nsxt_nat_rule

    from terrascript.resource.vmware.nsxt import nsxt_ns_group

    from terrascript.resource.vmware.nsxt import nsxt_ns_service_group

    from terrascript.resource.vmware.nsxt import nsxt_policy_bgp_config

    from terrascript.resource.vmware.nsxt import nsxt_policy_bgp_neighbor

    from terrascript.resource.vmware.nsxt import nsxt_policy_context_profile

    from terrascript.resource.vmware.nsxt import nsxt_policy_dhcp_relay

    from terrascript.resource.vmware.nsxt import nsxt_policy_dhcp_server

    from terrascript.resource.vmware.nsxt import nsxt_policy_dhcp_v4_static_binding

    from terrascript.resource.vmware.nsxt import nsxt_policy_dhcp_v6_static_binding

    from terrascript.resource.vmware.nsxt import nsxt_policy_dns_forwarder_zone

    from terrascript.resource.vmware.nsxt import nsxt_policy_domain

    from terrascript.resource.vmware.nsxt import nsxt_policy_evpn_config

    from terrascript.resource.vmware.nsxt import nsxt_policy_evpn_tenant

    from terrascript.resource.vmware.nsxt import nsxt_policy_evpn_tunnel_endpoint

    from terrascript.resource.vmware.nsxt import nsxt_policy_fixed_segment

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_community_list

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_dns_forwarder

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_policy

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_prefix_list

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_redistribution_config

    from terrascript.resource.vmware.nsxt import nsxt_policy_gateway_route_map

    from terrascript.resource.vmware.nsxt import nsxt_policy_group

    from terrascript.resource.vmware.nsxt import nsxt_policy_intrusion_service_policy

    from terrascript.resource.vmware.nsxt import nsxt_policy_intrusion_service_profile

    from terrascript.resource.vmware.nsxt import nsxt_policy_ip_address_allocation

    from terrascript.resource.vmware.nsxt import nsxt_policy_ip_block

    from terrascript.resource.vmware.nsxt import nsxt_policy_ip_pool

    from terrascript.resource.vmware.nsxt import nsxt_policy_ip_pool_block_subnet

    from terrascript.resource.vmware.nsxt import nsxt_policy_ip_pool_static_subnet

    from terrascript.resource.vmware.nsxt import nsxt_policy_lb_pool

    from terrascript.resource.vmware.nsxt import nsxt_policy_lb_service

    from terrascript.resource.vmware.nsxt import nsxt_policy_lb_virtual_server

    from terrascript.resource.vmware.nsxt import nsxt_policy_nat_rule

    from terrascript.resource.vmware.nsxt import nsxt_policy_ospf_area

    from terrascript.resource.vmware.nsxt import nsxt_policy_ospf_config

    from terrascript.resource.vmware.nsxt import nsxt_policy_predefined_gateway_policy

    from terrascript.resource.vmware.nsxt import nsxt_policy_predefined_security_policy

    from terrascript.resource.vmware.nsxt import nsxt_policy_qos_profile

    from terrascript.resource.vmware.nsxt import nsxt_policy_security_policy

    from terrascript.resource.vmware.nsxt import nsxt_policy_segment

    from terrascript.resource.vmware.nsxt import nsxt_policy_service

    from terrascript.resource.vmware.nsxt import nsxt_policy_static_route

    from terrascript.resource.vmware.nsxt import nsxt_policy_static_route_bfd_peer

    from terrascript.resource.vmware.nsxt import nsxt_policy_tier0_gateway

    from terrascript.resource.vmware.nsxt import nsxt_policy_tier0_gateway_ha_vip_config

    from terrascript.resource.vmware.nsxt import nsxt_policy_tier0_gateway_interface

    from terrascript.resource.vmware.nsxt import nsxt_policy_tier1_gateway

    from terrascript.resource.vmware.nsxt import nsxt_policy_tier1_gateway_interface

    from terrascript.resource.vmware.nsxt import nsxt_policy_vlan_segment

    from terrascript.resource.vmware.nsxt import nsxt_policy_vm_tags

    from terrascript.resource.vmware.nsxt import nsxt_qos_switching_profile

    from terrascript.resource.vmware.nsxt import nsxt_spoofguard_switching_profile

    from terrascript.resource.vmware.nsxt import nsxt_static_route

    from terrascript.resource.vmware.nsxt import nsxt_switch_security_switching_profile

    from terrascript.resource.vmware.nsxt import nsxt_vlan_logical_switch

    from terrascript.resource.vmware.nsxt import nsxt_vm_tags




def test_datasource_import():
    from terrascript.data.vmware.nsxt import nsxt_certificate

    from terrascript.data.vmware.nsxt import nsxt_edge_cluster

    from terrascript.data.vmware.nsxt import nsxt_firewall_section

    from terrascript.data.vmware.nsxt import nsxt_ip_pool

    from terrascript.data.vmware.nsxt import nsxt_logical_tier0_router

    from terrascript.data.vmware.nsxt import nsxt_logical_tier1_router

    from terrascript.data.vmware.nsxt import nsxt_mac_pool

    from terrascript.data.vmware.nsxt import nsxt_management_cluster

    from terrascript.data.vmware.nsxt import nsxt_ns_group

    from terrascript.data.vmware.nsxt import nsxt_ns_service

    from terrascript.data.vmware.nsxt import nsxt_policy_bfd_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_certificate

    from terrascript.data.vmware.nsxt import nsxt_policy_context_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_dhcp_server

    from terrascript.data.vmware.nsxt import nsxt_policy_edge_cluster

    from terrascript.data.vmware.nsxt import nsxt_policy_edge_node

    from terrascript.data.vmware.nsxt import nsxt_policy_gateway_policy

    from terrascript.data.vmware.nsxt import nsxt_policy_gateway_qos_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_group

    from terrascript.data.vmware.nsxt import nsxt_policy_intrusion_service_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_ip_block

    from terrascript.data.vmware.nsxt import nsxt_policy_ip_discovery_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_ip_pool

    from terrascript.data.vmware.nsxt import nsxt_policy_ipv6_dad_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_ipv6_ndra_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_lb_app_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_lb_client_ssl_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_lb_monitor

    from terrascript.data.vmware.nsxt import nsxt_policy_lb_persistence_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_lb_server_ssl_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_mac_discovery_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_qos_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_realization_info

    from terrascript.data.vmware.nsxt import nsxt_policy_security_policy

    from terrascript.data.vmware.nsxt import nsxt_policy_segment_realization

    from terrascript.data.vmware.nsxt import nsxt_policy_segment_security_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_service

    from terrascript.data.vmware.nsxt import nsxt_policy_site

    from terrascript.data.vmware.nsxt import nsxt_policy_spoofguard_profile

    from terrascript.data.vmware.nsxt import nsxt_policy_tier0_gateway

    from terrascript.data.vmware.nsxt import nsxt_policy_tier1_gateway

    from terrascript.data.vmware.nsxt import nsxt_policy_transport_zone

    from terrascript.data.vmware.nsxt import nsxt_policy_vm

    from terrascript.data.vmware.nsxt import nsxt_policy_vni_pool

    from terrascript.data.vmware.nsxt import nsxt_provider_info

    from terrascript.data.vmware.nsxt import nsxt_switching_profile

    from terrascript.data.vmware.nsxt import nsxt_transport_zone



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.vmware.nsxt
#      
#      t = terrascript.provider.vmware.nsxt.nsxt()
#      s = str(t)
#      
#      assert 'https://github.com/vmware/terraform-provider-nsxt' in s
#      assert '3.2.3' in s
