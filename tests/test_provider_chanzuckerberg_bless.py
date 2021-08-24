#tests/test_provider_chanzuckerberg_bless.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:32:06 UTC)

def test_provider_import():
    import terrascript.provider.chanzuckerberg.bless


def test_resource_import():
    from terrascript.resource.chanzuckerberg.bless import bless_ca

    from terrascript.resource.chanzuckerberg.bless import bless_ecdsa_ca




def test_datasource_import():
    from terrascript.data.chanzuckerberg.bless import bless_kms_public_key



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.chanzuckerberg.bless
#      
#      t = terrascript.provider.chanzuckerberg.bless.bless()
#      s = str(t)
#      
#      assert 'https://github.com/chanzuckerberg/terraform-provider-bless' in s
#      assert '0.5.0' in s
