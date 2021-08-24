#tests/test_provider_sacloud_sakuracloud.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:33:56 UTC)

def test_provider_import():
    import terrascript.provider.sacloud.sakuracloud


def test_resource_import():
    from terrascript.resource.sacloud.sakuracloud import sakuracloud_archive

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_archive_share

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_auto_backup

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_bridge

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_cdrom

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_container_registry

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_database

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_database_read_replica

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_disk

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_dns

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_dns_record

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_enhanced_db

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_esme

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_gslb

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_icon

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_internet

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_ipv4_ptr

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_load_balancer

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_local_router

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_mobile_gateway

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_nfs

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_note

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_packet_filter

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_packet_filter_rules

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_private_host

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_proxylb

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_proxylb_acme

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_server

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_sim

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_simple_monitor

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_ssh_key

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_ssh_key_gen

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_subnet

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_switch

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_vpc_router

    from terrascript.resource.sacloud.sakuracloud import sakuracloud_webaccel_certificate




def test_datasource_import():
    from terrascript.data.sacloud.sakuracloud import sakuracloud_archive

    from terrascript.data.sacloud.sakuracloud import sakuracloud_bridge

    from terrascript.data.sacloud.sakuracloud import sakuracloud_cdrom

    from terrascript.data.sacloud.sakuracloud import sakuracloud_container_registry

    from terrascript.data.sacloud.sakuracloud import sakuracloud_database

    from terrascript.data.sacloud.sakuracloud import sakuracloud_disk

    from terrascript.data.sacloud.sakuracloud import sakuracloud_dns

    from terrascript.data.sacloud.sakuracloud import sakuracloud_enhanced_db

    from terrascript.data.sacloud.sakuracloud import sakuracloud_esme

    from terrascript.data.sacloud.sakuracloud import sakuracloud_gslb

    from terrascript.data.sacloud.sakuracloud import sakuracloud_icon

    from terrascript.data.sacloud.sakuracloud import sakuracloud_internet

    from terrascript.data.sacloud.sakuracloud import sakuracloud_load_balancer

    from terrascript.data.sacloud.sakuracloud import sakuracloud_local_router

    from terrascript.data.sacloud.sakuracloud import sakuracloud_nfs

    from terrascript.data.sacloud.sakuracloud import sakuracloud_note

    from terrascript.data.sacloud.sakuracloud import sakuracloud_packet_filter

    from terrascript.data.sacloud.sakuracloud import sakuracloud_private_host

    from terrascript.data.sacloud.sakuracloud import sakuracloud_proxylb

    from terrascript.data.sacloud.sakuracloud import sakuracloud_server

    from terrascript.data.sacloud.sakuracloud import sakuracloud_server_vnc_info

    from terrascript.data.sacloud.sakuracloud import sakuracloud_simple_monitor

    from terrascript.data.sacloud.sakuracloud import sakuracloud_ssh_key

    from terrascript.data.sacloud.sakuracloud import sakuracloud_subnet

    from terrascript.data.sacloud.sakuracloud import sakuracloud_switch

    from terrascript.data.sacloud.sakuracloud import sakuracloud_vpc_router

    from terrascript.data.sacloud.sakuracloud import sakuracloud_webaccel

    from terrascript.data.sacloud.sakuracloud import sakuracloud_zone



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.sacloud.sakuracloud
#      
#      t = terrascript.provider.sacloud.sakuracloud.sakuracloud()
#      s = str(t)
#      
#      assert 'https://github.com/sacloud/terraform-provider-sakuracloud' in s
#      assert '2.12.0' in s
