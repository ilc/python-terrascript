#tests/test_provider_camptocamp_jwt.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:33:02 UTC)

def test_provider_import():
    import terrascript.provider.camptocamp.jwt


def test_resource_import():
    from terrascript.resource.camptocamp.jwt import jwt_hashed_token

    from terrascript.resource.camptocamp.jwt import jwt_signed_token





# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.camptocamp.jwt
#      
#      t = terrascript.provider.camptocamp.jwt.jwt()
#      s = str(t)
#      
#      assert 'https://github.com/camptocamp/terraform-provider-jwt' in s
#      assert '0.0.3' in s
