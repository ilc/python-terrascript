#tests/test_provider_mumoshu_eksctl.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:32:21 UTC)

def test_provider_import():
    import terrascript.provider.mumoshu.eksctl


def test_resource_import():
    from terrascript.resource.mumoshu.eksctl import eksctl_cluster

    from terrascript.resource.mumoshu.eksctl import eksctl_courier_alb

    from terrascript.resource.mumoshu.eksctl import eksctl_courier_route53_record

    from terrascript.resource.mumoshu.eksctl import eksctl_iamserviceaccount

    from terrascript.resource.mumoshu.eksctl import eksctl_nodegroup





# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.mumoshu.eksctl
#      
#      t = terrascript.provider.mumoshu.eksctl.eksctl()
#      s = str(t)
#      
#      assert 'https://github.com/mumoshu/terraform-provider-eksctl' in s
#      assert '0.16.2' in s
