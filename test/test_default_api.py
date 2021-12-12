# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubevirt
from kubevirt.rest import ApiException
from kubevirt.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = kubevirt.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_create_migration_policy(self):
        """
        Test case for create_migration_policy

        
        """
        pass

    def test_create_namespaced_kube_virt(self):
        """
        Test case for create_namespaced_kube_virt

        
        """
        pass

    def test_create_namespaced_virtual_machine(self):
        """
        Test case for create_namespaced_virtual_machine

        
        """
        pass

    def test_create_namespaced_virtual_machine_flavor(self):
        """
        Test case for create_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance(self):
        """
        Test case for create_namespaced_virtual_machine_instance

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for create_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for create_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_create_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for create_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_create_namespaced_virtual_machine_restore(self):
        """
        Test case for create_namespaced_virtual_machine_restore

        
        """
        pass

    def test_create_namespaced_virtual_machine_snapshot(self):
        """
        Test case for create_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_create_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for create_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_create_virtual_machine_cluster_flavor(self):
        """
        Test case for create_virtual_machine_cluster_flavor

        
        """
        pass

    def test_delete_collection_migration_policy(self):
        """
        Test case for delete_collection_migration_policy

        
        """
        pass

    def test_delete_collection_namespaced_kube_virt(self):
        """
        Test case for delete_collection_namespaced_kube_virt

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine(self):
        """
        Test case for delete_collection_namespaced_virtual_machine

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_flavor(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_restore(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_restore

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_snapshot(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_delete_collection_virtual_machine_cluster_flavor(self):
        """
        Test case for delete_collection_virtual_machine_cluster_flavor

        
        """
        pass

    def test_delete_migration_policy(self):
        """
        Test case for delete_migration_policy

        
        """
        pass

    def test_delete_namespaced_kube_virt(self):
        """
        Test case for delete_namespaced_kube_virt

        
        """
        pass

    def test_delete_namespaced_virtual_machine(self):
        """
        Test case for delete_namespaced_virtual_machine

        
        """
        pass

    def test_delete_namespaced_virtual_machine_flavor(self):
        """
        Test case for delete_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance(self):
        """
        Test case for delete_namespaced_virtual_machine_instance

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_delete_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for delete_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_delete_namespaced_virtual_machine_restore(self):
        """
        Test case for delete_namespaced_virtual_machine_restore

        
        """
        pass

    def test_delete_namespaced_virtual_machine_snapshot(self):
        """
        Test case for delete_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_delete_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for delete_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_delete_virtual_machine_cluster_flavor(self):
        """
        Test case for delete_virtual_machine_cluster_flavor

        
        """
        pass

    def test_func1(self):
        """
        Test case for func1

        
        """
        pass

    def test_func7(self):
        """
        Test case for func7

        
        """
        pass

    def test_get_api_group_flavor_kubevirt_io(self):
        """
        Test case for get_api_group_flavor_kubevirt_io

        
        """
        pass

    def test_get_api_group_kubevirt_io(self):
        """
        Test case for get_api_group_kubevirt_io

        
        """
        pass

    def test_get_api_group_list(self):
        """
        Test case for get_api_group_list

        
        """
        pass

    def test_get_api_group_migrations_kubevirt_io(self):
        """
        Test case for get_api_group_migrations_kubevirt_io

        
        """
        pass

    def test_get_api_group_snapshot_kubevirt_io(self):
        """
        Test case for get_api_group_snapshot_kubevirt_io

        
        """
        pass

    def test_get_api_resources_flavor_kubevirt_io_v1alpha1(self):
        """
        Test case for get_api_resources_flavor_kubevirt_io_v1alpha1

        
        """
        pass

    def test_get_api_resources_kubevirt_io_v1(self):
        """
        Test case for get_api_resources_kubevirt_io_v1

        
        """
        pass

    def test_get_api_resources_migrations_kubevirt_io_v1alpha1(self):
        """
        Test case for get_api_resources_migrations_kubevirt_io_v1alpha1

        
        """
        pass

    def test_get_api_resources_snapshot_kubevirt_io_v1alpha1(self):
        """
        Test case for get_api_resources_snapshot_kubevirt_io_v1alpha1

        
        """
        pass

    def test_get_root_paths(self):
        """
        Test case for get_root_paths

        
        """
        pass

    def test_handle_dump_profiler(self):
        """
        Test case for handle_dump_profiler

        
        """
        pass

    def test_handle_start_profiler(self):
        """
        Test case for handle_start_profiler

        
        """
        pass

    def test_handle_stop_profiler(self):
        """
        Test case for handle_stop_profiler

        
        """
        pass

    def test_list_kube_virt_for_all_namespaces(self):
        """
        Test case for list_kube_virt_for_all_namespaces

        
        """
        pass

    def test_list_migration_policy(self):
        """
        Test case for list_migration_policy

        
        """
        pass

    def test_list_namespaced_kube_virt(self):
        """
        Test case for list_namespaced_kube_virt

        
        """
        pass

    def test_list_namespaced_virtual_machine(self):
        """
        Test case for list_namespaced_virtual_machine

        
        """
        pass

    def test_list_namespaced_virtual_machine_flavor(self):
        """
        Test case for list_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance(self):
        """
        Test case for list_namespaced_virtual_machine_instance

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for list_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for list_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_list_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for list_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_list_namespaced_virtual_machine_restore(self):
        """
        Test case for list_namespaced_virtual_machine_restore

        
        """
        pass

    def test_list_namespaced_virtual_machine_snapshot(self):
        """
        Test case for list_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_list_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for list_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_list_virtual_machine_cluster_flavor(self):
        """
        Test case for list_virtual_machine_cluster_flavor

        
        """
        pass

    def test_list_virtual_machine_flavor_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_flavor_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_migration_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_migration_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_preset_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_preset_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_instance_replica_set_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_instance_replica_set_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_restore_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_restore_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_snapshot_content_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_snapshot_content_for_all_namespaces

        
        """
        pass

    def test_list_virtual_machine_snapshot_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_snapshot_for_all_namespaces

        
        """
        pass

    def test_patch_migration_policy(self):
        """
        Test case for patch_migration_policy

        
        """
        pass

    def test_patch_namespaced_kube_virt(self):
        """
        Test case for patch_namespaced_kube_virt

        
        """
        pass

    def test_patch_namespaced_virtual_machine(self):
        """
        Test case for patch_namespaced_virtual_machine

        
        """
        pass

    def test_patch_namespaced_virtual_machine_flavor(self):
        """
        Test case for patch_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance(self):
        """
        Test case for patch_namespaced_virtual_machine_instance

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_patch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for patch_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_patch_namespaced_virtual_machine_restore(self):
        """
        Test case for patch_namespaced_virtual_machine_restore

        
        """
        pass

    def test_patch_namespaced_virtual_machine_snapshot(self):
        """
        Test case for patch_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_patch_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for patch_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_patch_virtual_machine_cluster_flavor(self):
        """
        Test case for patch_virtual_machine_cluster_flavor

        
        """
        pass

    def test_read_migration_policy(self):
        """
        Test case for read_migration_policy

        
        """
        pass

    def test_read_namespaced_kube_virt(self):
        """
        Test case for read_namespaced_kube_virt

        
        """
        pass

    def test_read_namespaced_virtual_machine(self):
        """
        Test case for read_namespaced_virtual_machine

        
        """
        pass

    def test_read_namespaced_virtual_machine_flavor(self):
        """
        Test case for read_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance(self):
        """
        Test case for read_namespaced_virtual_machine_instance

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for read_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for read_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_read_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for read_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_read_namespaced_virtual_machine_restore(self):
        """
        Test case for read_namespaced_virtual_machine_restore

        
        """
        pass

    def test_read_namespaced_virtual_machine_snapshot(self):
        """
        Test case for read_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_read_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for read_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_read_virtual_machine_cluster_flavor(self):
        """
        Test case for read_virtual_machine_cluster_flavor

        
        """
        pass

    def test_replace_migration_policy(self):
        """
        Test case for replace_migration_policy

        
        """
        pass

    def test_replace_namespaced_kube_virt(self):
        """
        Test case for replace_namespaced_kube_virt

        
        """
        pass

    def test_replace_namespaced_virtual_machine(self):
        """
        Test case for replace_namespaced_virtual_machine

        
        """
        pass

    def test_replace_namespaced_virtual_machine_flavor(self):
        """
        Test case for replace_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance(self):
        """
        Test case for replace_namespaced_virtual_machine_instance

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_replace_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for replace_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_replace_namespaced_virtual_machine_restore(self):
        """
        Test case for replace_namespaced_virtual_machine_restore

        
        """
        pass

    def test_replace_namespaced_virtual_machine_snapshot(self):
        """
        Test case for replace_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_replace_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for replace_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_replace_virtual_machine_cluster_flavor(self):
        """
        Test case for replace_virtual_machine_cluster_flavor

        
        """
        pass

    def test_v1_check_health(self):
        """
        Test case for v1_check_health

        
        """
        pass

    def test_v1_console(self):
        """
        Test case for v1_console

        
        """
        pass

    def test_v1_filesystemlist(self):
        """
        Test case for v1_filesystemlist

        
        """
        pass

    def test_v1_freeze(self):
        """
        Test case for v1_freeze

        
        """
        pass

    def test_v1_guestfs(self):
        """
        Test case for v1_guestfs

        
        """
        pass

    def test_v1_guestosinfo(self):
        """
        Test case for v1_guestosinfo

        
        """
        pass

    def test_v1_migrate(self):
        """
        Test case for v1_migrate

        
        """
        pass

    def test_v1_pause(self):
        """
        Test case for v1_pause

        
        """
        pass

    def test_v1_restart(self):
        """
        Test case for v1_restart

        
        """
        pass

    def test_v1_soft_reboot(self):
        """
        Test case for v1_soft_reboot

        
        """
        pass

    def test_v1_start(self):
        """
        Test case for v1_start

        
        """
        pass

    def test_v1_stop(self):
        """
        Test case for v1_stop

        
        """
        pass

    def test_v1_test(self):
        """
        Test case for v1_test

        
        """
        pass

    def test_v1_unfreeze(self):
        """
        Test case for v1_unfreeze

        
        """
        pass

    def test_v1_unpause(self):
        """
        Test case for v1_unpause

        
        """
        pass

    def test_v1_userlist(self):
        """
        Test case for v1_userlist

        
        """
        pass

    def test_v1_version(self):
        """
        Test case for v1_version

        
        """
        pass

    def test_v1_vnc(self):
        """
        Test case for v1_vnc

        
        """
        pass

    def test_v1alpha3_check_health(self):
        """
        Test case for v1alpha3_check_health

        
        """
        pass

    def test_v1alpha3_console(self):
        """
        Test case for v1alpha3_console

        
        """
        pass

    def test_v1alpha3_filesystemlist(self):
        """
        Test case for v1alpha3_filesystemlist

        
        """
        pass

    def test_v1alpha3_freeze(self):
        """
        Test case for v1alpha3_freeze

        
        """
        pass

    def test_v1alpha3_get_sub_api_group(self):
        """
        Test case for v1alpha3_get_sub_api_group

        
        """
        pass

    def test_v1alpha3_guestfs(self):
        """
        Test case for v1alpha3_guestfs

        
        """
        pass

    def test_v1alpha3_guestosinfo(self):
        """
        Test case for v1alpha3_guestosinfo

        
        """
        pass

    def test_v1alpha3_migrate(self):
        """
        Test case for v1alpha3_migrate

        
        """
        pass

    def test_v1alpha3_pause(self):
        """
        Test case for v1alpha3_pause

        
        """
        pass

    def test_v1alpha3_restart(self):
        """
        Test case for v1alpha3_restart

        
        """
        pass

    def test_v1alpha3_soft_reboot(self):
        """
        Test case for v1alpha3_soft_reboot

        
        """
        pass

    def test_v1alpha3_start(self):
        """
        Test case for v1alpha3_start

        
        """
        pass

    def test_v1alpha3_stop(self):
        """
        Test case for v1alpha3_stop

        
        """
        pass

    def test_v1alpha3_test(self):
        """
        Test case for v1alpha3_test

        
        """
        pass

    def test_v1alpha3_unfreeze(self):
        """
        Test case for v1alpha3_unfreeze

        
        """
        pass

    def test_v1alpha3_unpause(self):
        """
        Test case for v1alpha3_unpause

        
        """
        pass

    def test_v1alpha3_userlist(self):
        """
        Test case for v1alpha3_userlist

        
        """
        pass

    def test_v1alpha3_version(self):
        """
        Test case for v1alpha3_version

        
        """
        pass

    def test_v1alpha3_vnc(self):
        """
        Test case for v1alpha3_vnc

        
        """
        pass

    def test_v1alpha3dump_cluster_profiler(self):
        """
        Test case for v1alpha3dump_cluster_profiler

        
        """
        pass

    def test_v1alpha3get_api_sub_resources(self):
        """
        Test case for v1alpha3get_api_sub_resources

        
        """
        pass

    def test_v1alpha3start_cluster_profiler(self):
        """
        Test case for v1alpha3start_cluster_profiler

        
        """
        pass

    def test_v1alpha3stop_cluster_profiler(self):
        """
        Test case for v1alpha3stop_cluster_profiler

        
        """
        pass

    def test_v1alpha3usbredir(self):
        """
        Test case for v1alpha3usbredir

        
        """
        pass

    def test_v1alpha3vm_addvolume(self):
        """
        Test case for v1alpha3vm_addvolume

        
        """
        pass

    def test_v1alpha3vm_port_forward(self):
        """
        Test case for v1alpha3vm_port_forward

        
        """
        pass

    def test_v1alpha3vm_port_forward_with_protocol(self):
        """
        Test case for v1alpha3vm_port_forward_with_protocol

        
        """
        pass

    def test_v1alpha3vm_removevolume(self):
        """
        Test case for v1alpha3vm_removevolume

        
        """
        pass

    def test_v1alpha3vmi_addvolume(self):
        """
        Test case for v1alpha3vmi_addvolume

        
        """
        pass

    def test_v1alpha3vmi_port_forward(self):
        """
        Test case for v1alpha3vmi_port_forward

        
        """
        pass

    def test_v1alpha3vmi_port_forward_with_protocol(self):
        """
        Test case for v1alpha3vmi_port_forward_with_protocol

        
        """
        pass

    def test_v1alpha3vmi_removevolume(self):
        """
        Test case for v1alpha3vmi_removevolume

        
        """
        pass

    def test_v1dump_cluster_profiler(self):
        """
        Test case for v1dump_cluster_profiler

        
        """
        pass

    def test_v1get_api_sub_resources(self):
        """
        Test case for v1get_api_sub_resources

        
        """
        pass

    def test_v1start_cluster_profiler(self):
        """
        Test case for v1start_cluster_profiler

        
        """
        pass

    def test_v1stop_cluster_profiler(self):
        """
        Test case for v1stop_cluster_profiler

        
        """
        pass

    def test_v1usbredir(self):
        """
        Test case for v1usbredir

        
        """
        pass

    def test_v1vm_addvolume(self):
        """
        Test case for v1vm_addvolume

        
        """
        pass

    def test_v1vm_port_forward(self):
        """
        Test case for v1vm_port_forward

        
        """
        pass

    def test_v1vm_port_forward_with_protocol(self):
        """
        Test case for v1vm_port_forward_with_protocol

        
        """
        pass

    def test_v1vm_removevolume(self):
        """
        Test case for v1vm_removevolume

        
        """
        pass

    def test_v1vmi_addvolume(self):
        """
        Test case for v1vmi_addvolume

        
        """
        pass

    def test_v1vmi_port_forward(self):
        """
        Test case for v1vmi_port_forward

        
        """
        pass

    def test_v1vmi_port_forward_with_protocol(self):
        """
        Test case for v1vmi_port_forward_with_protocol

        
        """
        pass

    def test_v1vmi_removevolume(self):
        """
        Test case for v1vmi_removevolume

        
        """
        pass

    def test_watch_kube_virt_list_for_all_namespaces(self):
        """
        Test case for watch_kube_virt_list_for_all_namespaces

        
        """
        pass

    def test_watch_migration_policy_list_for_all_namespaces(self):
        """
        Test case for watch_migration_policy_list_for_all_namespaces

        
        """
        pass

    def test_watch_namespaced_kube_virt(self):
        """
        Test case for watch_namespaced_kube_virt

        
        """
        pass

    def test_watch_namespaced_virtual_machine(self):
        """
        Test case for watch_namespaced_virtual_machine

        
        """
        pass

    def test_watch_namespaced_virtual_machine_flavor(self):
        """
        Test case for watch_namespaced_virtual_machine_flavor

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance(self):
        """
        Test case for watch_namespaced_virtual_machine_instance

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_migration(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_migration

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_preset(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_preset

        
        """
        pass

    def test_watch_namespaced_virtual_machine_instance_replica_set(self):
        """
        Test case for watch_namespaced_virtual_machine_instance_replica_set

        
        """
        pass

    def test_watch_namespaced_virtual_machine_restore(self):
        """
        Test case for watch_namespaced_virtual_machine_restore

        
        """
        pass

    def test_watch_namespaced_virtual_machine_snapshot(self):
        """
        Test case for watch_namespaced_virtual_machine_snapshot

        
        """
        pass

    def test_watch_namespaced_virtual_machine_snapshot_content(self):
        """
        Test case for watch_namespaced_virtual_machine_snapshot_content

        
        """
        pass

    def test_watch_virtual_machine_cluster_flavor_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_cluster_flavor_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_flavor_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_flavor_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_migration_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_migration_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_preset_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_preset_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_instance_replica_set_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_instance_replica_set_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_restore_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_restore_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_snapshot_content_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_snapshot_content_list_for_all_namespaces

        
        """
        pass

    def test_watch_virtual_machine_snapshot_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_snapshot_list_for_all_namespaces

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
