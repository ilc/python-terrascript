#tests/test_provider_hashicorp_ciscoasa.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:32:10 UTC)

def test_provider_import():
    import terrascript.provider.hashicorp.ciscoasa


def test_resource_import():
    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_access_in_rules

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_access_out_rules

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_acl

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_network_object

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_network_object_group

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_network_service_group

    from terrascript.resource.hashicorp.ciscoasa import ciscoasa_static_route





# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.hashicorp.ciscoasa
#      
#      t = terrascript.provider.hashicorp.ciscoasa.ciscoasa()
#      s = str(t)
#      
#      assert 'https://github.com/hashicorp/terraform-provider-ciscoasa' in s
#      assert '1.2.0' in s
