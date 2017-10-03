# coding: utf-8

"""


    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.apiskubevirt_iov1alpha1_api import ApiskubevirtIov1alpha1Api


class TestApiskubevirtIov1alpha1Api(unittest.TestCase):
    """ ApiskubevirtIov1alpha1Api unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.apiskubevirt_iov1alpha1_api.ApiskubevirtIov1alpha1Api()

    def tearDown(self):
        pass

    def test_console(self):
        """
        Test case for console

        Open a websocket connection to a serial console on the specified VM.
        """
        pass

    def test_create_namespaced_migration(self):
        """
        Test case for create_namespaced_migration

        Create a Migration object.
        """
        pass

    def test_create_namespaced_virtual_machine(self):
        """
        Test case for create_namespaced_virtual_machine

        Create a VirtualMachine object.
        """
        pass

    def test_create_namespaced_virtual_machine_replica_set(self):
        """
        Test case for create_namespaced_virtual_machine_replica_set

        Create a VirtualMachineReplicaSet object.
        """
        pass

    def test_delete_namespaced_migration(self):
        """
        Test case for delete_namespaced_migration

        Delete a Migration object.
        """
        pass

    def test_delete_namespaced_virtual_machine(self):
        """
        Test case for delete_namespaced_virtual_machine

        Delete a VirtualMachine object.
        """
        pass

    def test_delete_namespaced_virtual_machine_replica_set(self):
        """
        Test case for delete_namespaced_virtual_machine_replica_set

        Delete a VirtualMachineReplicaSet object.
        """
        pass

    def test_deletecollection_namespaced_migration(self):
        """
        Test case for deletecollection_namespaced_migration

        Delete a collection of Migration objects.
        """
        pass

    def test_deletecollection_namespaced_virtual_machine(self):
        """
        Test case for deletecollection_namespaced_virtual_machine

        Delete a collection of VirtualMachine objects.
        """
        pass

    def test_deletecollection_namespaced_virtual_machine_replica_set(self):
        """
        Test case for deletecollection_namespaced_virtual_machine_replica_set

        Delete a collection of VirtualMachineReplicaSet objects.
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        Get KubeVirt API Resources
        """
        pass

    def test_kube_connection_healthz_func(self):
        """
        Test case for kube_connection_healthz_func

        Health endpoint
        """
        pass

    def test_list_migration_for_all_namespaces(self):
        """
        Test case for list_migration_for_all_namespaces

        Get a list all of Migration objects.
        """
        pass

    def test_list_namespaced_migration_list(self):
        """
        Test case for list_namespaced_migration_list

        Get a list of Migration objects.
        """
        pass

    def test_list_namespaced_virtual_machine_list(self):
        """
        Test case for list_namespaced_virtual_machine_list

        Get a list of VirtualMachine objects.
        """
        pass

    def test_list_namespaced_virtual_machine_replica_set_list(self):
        """
        Test case for list_namespaced_virtual_machine_replica_set_list

        Get a list of VirtualMachineReplicaSet objects.
        """
        pass

    def test_list_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_for_all_namespaces

        Get a list all of VirtualMachine objects.
        """
        pass

    def test_list_virtual_machine_replica_set_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_replica_set_for_all_namespaces

        Get a list all of VirtualMachineReplicaSet objects.
        """
        pass

    def test_read_namespaced_migration(self):
        """
        Test case for read_namespaced_migration

        Get a Migration object.
        """
        pass

    def test_read_namespaced_virtual_machine(self):
        """
        Test case for read_namespaced_virtual_machine

        Get a VirtualMachine object.
        """
        pass

    def test_read_namespaced_virtual_machine_replica_set(self):
        """
        Test case for read_namespaced_virtual_machine_replica_set

        Get a VirtualMachineReplicaSet object.
        """
        pass

    def test_replace_namespaced_migration(self):
        """
        Test case for replace_namespaced_migration

        Update a Migration object.
        """
        pass

    def test_replace_namespaced_virtual_machine(self):
        """
        Test case for replace_namespaced_virtual_machine

        Update a VirtualMachine object.
        """
        pass

    def test_replace_namespaced_virtual_machine_replica_set(self):
        """
        Test case for replace_namespaced_virtual_machine_replica_set

        Update a VirtualMachineReplicaSet object.
        """
        pass

    def test_spice(self):
        """
        Test case for spice

        Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.
        """
        pass

    def test_update_namespaced_migration(self):
        """
        Test case for update_namespaced_migration

        Patch a Migration object.
        """
        pass

    def test_update_namespaced_virtual_machine(self):
        """
        Test case for update_namespaced_virtual_machine

        Patch a VirtualMachine object.
        """
        pass

    def test_update_namespaced_virtual_machine_replica_set(self):
        """
        Test case for update_namespaced_virtual_machine_replica_set

        Patch a VirtualMachineReplicaSet object.
        """
        pass

    def test_watch_migration_list_for_all_namespaces(self):
        """
        Test case for watch_migration_list_for_all_namespaces

        Watch a MigrationList object.
        """
        pass

    def test_watch_namespaced_migration(self):
        """
        Test case for watch_namespaced_migration

        Watch a Migration object.
        """
        pass

    def test_watch_namespaced_virtual_machine(self):
        """
        Test case for watch_namespaced_virtual_machine

        Watch a VirtualMachine object.
        """
        pass

    def test_watch_namespaced_virtual_machine_replica_set(self):
        """
        Test case for watch_namespaced_virtual_machine_replica_set

        Watch a VirtualMachineReplicaSet object.
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces

        Watch a VirtualMachineList object.
        """
        pass

    def test_watch_virtual_machine_replica_set_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_replica_set_list_for_all_namespaces

        Watch a VirtualMachineReplicaSetList object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
