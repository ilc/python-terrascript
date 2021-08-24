#tests/test_provider_hashicorp_ad.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:31:39 UTC)

def test_provider_import():
    import terrascript.provider.hashicorp.ad


def test_resource_import():
    from terrascript.resource.hashicorp.ad import ad_computer

    from terrascript.resource.hashicorp.ad import ad_gplink

    from terrascript.resource.hashicorp.ad import ad_gpo

    from terrascript.resource.hashicorp.ad import ad_gpo_security

    from terrascript.resource.hashicorp.ad import ad_group

    from terrascript.resource.hashicorp.ad import ad_group_membership

    from terrascript.resource.hashicorp.ad import ad_ou

    from terrascript.resource.hashicorp.ad import ad_user




def test_datasource_import():
    from terrascript.data.hashicorp.ad import ad_computer

    from terrascript.data.hashicorp.ad import ad_gpo

    from terrascript.data.hashicorp.ad import ad_group

    from terrascript.data.hashicorp.ad import ad_ou

    from terrascript.data.hashicorp.ad import ad_user



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.hashicorp.ad
#      
#      t = terrascript.provider.hashicorp.ad.ad()
#      s = str(t)
#      
#      assert 'https://github.com/hashicorp/terraform-provider-ad' in s
#      assert '0.4.3' in s
