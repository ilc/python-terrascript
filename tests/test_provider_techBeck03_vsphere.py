#tests/test_provider_techBeck03_vsphere.py
# Automatically generated by tools/makecode.py (24-Aug-2021 11:34:38 UTC)

def test_provider_import():
    import terrascript.provider.techBeck03.vsphere


def test_resource_import():
    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_host_group

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_vm_affinity_rule

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_vm_anti_affinity_rule

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_vm_dependency_rule

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_vm_group

    from terrascript.resource.techBeck03.vsphere import vsphere_compute_cluster_vm_host_rule

    from terrascript.resource.techBeck03.vsphere import vsphere_content_library

    from terrascript.resource.techBeck03.vsphere import vsphere_content_library_item

    from terrascript.resource.techBeck03.vsphere import vsphere_custom_attribute

    from terrascript.resource.techBeck03.vsphere import vsphere_datacenter

    from terrascript.resource.techBeck03.vsphere import vsphere_datastore_cluster

    from terrascript.resource.techBeck03.vsphere import vsphere_datastore_cluster_vm_anti_affinity_rule

    from terrascript.resource.techBeck03.vsphere import vsphere_distributed_port_group

    from terrascript.resource.techBeck03.vsphere import vsphere_distributed_virtual_switch

    from terrascript.resource.techBeck03.vsphere import vsphere_dpm_host_override

    from terrascript.resource.techBeck03.vsphere import vsphere_drs_vm_override

    from terrascript.resource.techBeck03.vsphere import vsphere_entity_permissions

    from terrascript.resource.techBeck03.vsphere import vsphere_file

    from terrascript.resource.techBeck03.vsphere import vsphere_folder

    from terrascript.resource.techBeck03.vsphere import vsphere_ha_vm_override

    from terrascript.resource.techBeck03.vsphere import vsphere_host

    from terrascript.resource.techBeck03.vsphere import vsphere_host_port_group

    from terrascript.resource.techBeck03.vsphere import vsphere_host_virtual_switch

    from terrascript.resource.techBeck03.vsphere import vsphere_license

    from terrascript.resource.techBeck03.vsphere import vsphere_nas_datastore

    from terrascript.resource.techBeck03.vsphere import vsphere_resource_pool

    from terrascript.resource.techBeck03.vsphere import vsphere_role

    from terrascript.resource.techBeck03.vsphere import vsphere_storage_drs_vm_override

    from terrascript.resource.techBeck03.vsphere import vsphere_tag

    from terrascript.resource.techBeck03.vsphere import vsphere_tag_category

    from terrascript.resource.techBeck03.vsphere import vsphere_vapp_container

    from terrascript.resource.techBeck03.vsphere import vsphere_vapp_entity

    from terrascript.resource.techBeck03.vsphere import vsphere_virtual_disk

    from terrascript.resource.techBeck03.vsphere import vsphere_virtual_machine

    from terrascript.resource.techBeck03.vsphere import vsphere_virtual_machine_snapshot

    from terrascript.resource.techBeck03.vsphere import vsphere_vm_storage_policy

    from terrascript.resource.techBeck03.vsphere import vsphere_vmfs_datastore

    from terrascript.resource.techBeck03.vsphere import vsphere_vnic




def test_datasource_import():
    from terrascript.data.techBeck03.vsphere import vsphere_compute_cluster

    from terrascript.data.techBeck03.vsphere import vsphere_content_library

    from terrascript.data.techBeck03.vsphere import vsphere_content_library_item

    from terrascript.data.techBeck03.vsphere import vsphere_custom_attribute

    from terrascript.data.techBeck03.vsphere import vsphere_datacenter

    from terrascript.data.techBeck03.vsphere import vsphere_datastore

    from terrascript.data.techBeck03.vsphere import vsphere_datastore_cluster

    from terrascript.data.techBeck03.vsphere import vsphere_distributed_virtual_switch

    from terrascript.data.techBeck03.vsphere import vsphere_dynamic

    from terrascript.data.techBeck03.vsphere import vsphere_folder

    from terrascript.data.techBeck03.vsphere import vsphere_host

    from terrascript.data.techBeck03.vsphere import vsphere_host_pci_device

    from terrascript.data.techBeck03.vsphere import vsphere_host_thumbprint

    from terrascript.data.techBeck03.vsphere import vsphere_network

    from terrascript.data.techBeck03.vsphere import vsphere_resource_pool

    from terrascript.data.techBeck03.vsphere import vsphere_role

    from terrascript.data.techBeck03.vsphere import vsphere_storage_policy

    from terrascript.data.techBeck03.vsphere import vsphere_tag

    from terrascript.data.techBeck03.vsphere import vsphere_tag_category

    from terrascript.data.techBeck03.vsphere import vsphere_vapp_container

    from terrascript.data.techBeck03.vsphere import vsphere_virtual_machine

    from terrascript.data.techBeck03.vsphere import vsphere_vmfs_disks



# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#     
#      import terrascript.provider.techBeck03.vsphere
#      
#      t = terrascript.provider.techBeck03.vsphere.vsphere()
#      s = str(t)
#      
#      assert 'https://github.com/techBeck03/terraform-provider-vsphere' in s
#      assert '1.24.3-patch' in s
