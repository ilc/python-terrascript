#tests/test_provider_bgpat_dnsimple.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:32:20 UTC)

def test_provider_import():
    import terrascript.provider.bgpat.dnsimple


def test_resource_import():
    from terrascript.resource.bgpat.dnsimple import dnsimple_email_forward

    from terrascript.resource.bgpat.dnsimple import dnsimple_record





# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.bgpat.dnsimple
#      
#      t = terrascript.provider.bgpat.dnsimple.dnsimple()
#      s = str(t)
#      
#      assert 'https://github.com/bgpat/terraform-provider-dnsimple' in s
#      assert '0.5.1' in s
