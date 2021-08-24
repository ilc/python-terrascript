#tests/test_provider_gavinbunney_bitbucketserver.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:32:06 UTC)

def test_provider_import():
    import terrascript.provider.gavinbunney.bitbucketserver


def test_resource_import():
    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_banner

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_default_reviewers_condition

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_global_permissions_group

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_global_permissions_user

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_group

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_license

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_mail_server

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_plugin

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_plugin_config

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_project

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_project_hook

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_project_permissions_group

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_project_permissions_user

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_repository

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_repository_hook

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_repository_permissions_group

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_repository_permissions_user

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_user

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_user_access_token

    from terrascript.resource.gavinbunney.bitbucketserver import bitbucketserver_user_group




def test_datasource_import():
    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_application_properties

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_cluster

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_global_permissions_groups

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_global_permissions_users

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_group_users

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_groups

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_plugin

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_project_hooks

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_project_permissions_groups

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_project_permissions_users

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_repository_hooks

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_repository_permissions_groups

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_repository_permissions_users

    from terrascript.data.gavinbunney.bitbucketserver import bitbucketserver_user



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.gavinbunney.bitbucketserver
#      
#      t = terrascript.provider.gavinbunney.bitbucketserver.bitbucketserver()
#      s = str(t)
#      
#      assert 'https://github.com/gavinbunney/terraform-provider-bitbucketserver' in s
#      assert '1.5.0' in s
