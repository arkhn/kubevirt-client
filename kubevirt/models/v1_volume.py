# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Volume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cloud_init_config_drive': 'V1CloudInitConfigDriveSource',
        'cloud_init_no_cloud': 'V1CloudInitNoCloudSource',
        'config_map': 'V1ConfigMapVolumeSource',
        'container_disk': 'V1ContainerDiskSource',
        'data_volume': 'V1DataVolumeSource',
        'downward_api': 'V1DownwardAPIVolumeSource',
        'downward_metrics': 'V1DownwardMetricsVolumeSource',
        'empty_disk': 'V1EmptyDiskSource',
        'ephemeral': 'V1EphemeralVolumeSource',
        'host_disk': 'V1HostDisk',
        'memory_dump': 'V1MemoryDumpVolumeSource',
        'name': 'str',
        'persistent_volume_claim': 'V1PersistentVolumeClaimVolumeSource',
        'secret': 'V1SecretVolumeSource',
        'service_account': 'V1ServiceAccountVolumeSource',
        'sysprep': 'V1SysprepSource'
    }

    attribute_map = {
        'cloud_init_config_drive': 'cloudInitConfigDrive',
        'cloud_init_no_cloud': 'cloudInitNoCloud',
        'config_map': 'configMap',
        'container_disk': 'containerDisk',
        'data_volume': 'dataVolume',
        'downward_api': 'downwardAPI',
        'downward_metrics': 'downwardMetrics',
        'empty_disk': 'emptyDisk',
        'ephemeral': 'ephemeral',
        'host_disk': 'hostDisk',
        'memory_dump': 'memoryDump',
        'name': 'name',
        'persistent_volume_claim': 'persistentVolumeClaim',
        'secret': 'secret',
        'service_account': 'serviceAccount',
        'sysprep': 'sysprep'
    }

    def __init__(self, cloud_init_config_drive=None, cloud_init_no_cloud=None, config_map=None, container_disk=None, data_volume=None, downward_api=None, downward_metrics=None, empty_disk=None, ephemeral=None, host_disk=None, memory_dump=None, name=None, persistent_volume_claim=None, secret=None, service_account=None, sysprep=None):
        """
        V1Volume - a model defined in Swagger
        """

        self._cloud_init_config_drive = None
        self._cloud_init_no_cloud = None
        self._config_map = None
        self._container_disk = None
        self._data_volume = None
        self._downward_api = None
        self._downward_metrics = None
        self._empty_disk = None
        self._ephemeral = None
        self._host_disk = None
        self._memory_dump = None
        self._name = None
        self._persistent_volume_claim = None
        self._secret = None
        self._service_account = None
        self._sysprep = None

        if cloud_init_config_drive is not None:
          self.cloud_init_config_drive = cloud_init_config_drive
        if cloud_init_no_cloud is not None:
          self.cloud_init_no_cloud = cloud_init_no_cloud
        if config_map is not None:
          self.config_map = config_map
        if container_disk is not None:
          self.container_disk = container_disk
        if data_volume is not None:
          self.data_volume = data_volume
        if downward_api is not None:
          self.downward_api = downward_api
        if downward_metrics is not None:
          self.downward_metrics = downward_metrics
        if empty_disk is not None:
          self.empty_disk = empty_disk
        if ephemeral is not None:
          self.ephemeral = ephemeral
        if host_disk is not None:
          self.host_disk = host_disk
        if memory_dump is not None:
          self.memory_dump = memory_dump
        self.name = name
        if persistent_volume_claim is not None:
          self.persistent_volume_claim = persistent_volume_claim
        if secret is not None:
          self.secret = secret
        if service_account is not None:
          self.service_account = service_account
        if sysprep is not None:
          self.sysprep = sysprep

    @property
    def cloud_init_config_drive(self):
        """
        Gets the cloud_init_config_drive of this V1Volume.
        CloudInitConfigDrive represents a cloud-init Config Drive user-data source. The Config Drive data will be added as a disk to the vmi. A proper cloud-init installation is required inside the guest. More info: https://cloudinit.readthedocs.io/en/latest/topics/datasources/configdrive.html

        :return: The cloud_init_config_drive of this V1Volume.
        :rtype: V1CloudInitConfigDriveSource
        """
        return self._cloud_init_config_drive

    @cloud_init_config_drive.setter
    def cloud_init_config_drive(self, cloud_init_config_drive):
        """
        Sets the cloud_init_config_drive of this V1Volume.
        CloudInitConfigDrive represents a cloud-init Config Drive user-data source. The Config Drive data will be added as a disk to the vmi. A proper cloud-init installation is required inside the guest. More info: https://cloudinit.readthedocs.io/en/latest/topics/datasources/configdrive.html

        :param cloud_init_config_drive: The cloud_init_config_drive of this V1Volume.
        :type: V1CloudInitConfigDriveSource
        """

        self._cloud_init_config_drive = cloud_init_config_drive

    @property
    def cloud_init_no_cloud(self):
        """
        Gets the cloud_init_no_cloud of this V1Volume.
        CloudInitNoCloud represents a cloud-init NoCloud user-data source. The NoCloud data will be added as a disk to the vmi. A proper cloud-init installation is required inside the guest. More info: http://cloudinit.readthedocs.io/en/latest/topics/datasources/nocloud.html

        :return: The cloud_init_no_cloud of this V1Volume.
        :rtype: V1CloudInitNoCloudSource
        """
        return self._cloud_init_no_cloud

    @cloud_init_no_cloud.setter
    def cloud_init_no_cloud(self, cloud_init_no_cloud):
        """
        Sets the cloud_init_no_cloud of this V1Volume.
        CloudInitNoCloud represents a cloud-init NoCloud user-data source. The NoCloud data will be added as a disk to the vmi. A proper cloud-init installation is required inside the guest. More info: http://cloudinit.readthedocs.io/en/latest/topics/datasources/nocloud.html

        :param cloud_init_no_cloud: The cloud_init_no_cloud of this V1Volume.
        :type: V1CloudInitNoCloudSource
        """

        self._cloud_init_no_cloud = cloud_init_no_cloud

    @property
    def config_map(self):
        """
        Gets the config_map of this V1Volume.
        ConfigMapSource represents a reference to a ConfigMap in the same namespace. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/

        :return: The config_map of this V1Volume.
        :rtype: V1ConfigMapVolumeSource
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this V1Volume.
        ConfigMapSource represents a reference to a ConfigMap in the same namespace. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/

        :param config_map: The config_map of this V1Volume.
        :type: V1ConfigMapVolumeSource
        """

        self._config_map = config_map

    @property
    def container_disk(self):
        """
        Gets the container_disk of this V1Volume.
        ContainerDisk references a docker image, embedding a qcow or raw disk. More info: https://kubevirt.gitbooks.io/user-guide/registry-disk.html

        :return: The container_disk of this V1Volume.
        :rtype: V1ContainerDiskSource
        """
        return self._container_disk

    @container_disk.setter
    def container_disk(self, container_disk):
        """
        Sets the container_disk of this V1Volume.
        ContainerDisk references a docker image, embedding a qcow or raw disk. More info: https://kubevirt.gitbooks.io/user-guide/registry-disk.html

        :param container_disk: The container_disk of this V1Volume.
        :type: V1ContainerDiskSource
        """

        self._container_disk = container_disk

    @property
    def data_volume(self):
        """
        Gets the data_volume of this V1Volume.
        DataVolume represents the dynamic creation a PVC for this volume as well as the process of populating that PVC with a disk image.

        :return: The data_volume of this V1Volume.
        :rtype: V1DataVolumeSource
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        """
        Sets the data_volume of this V1Volume.
        DataVolume represents the dynamic creation a PVC for this volume as well as the process of populating that PVC with a disk image.

        :param data_volume: The data_volume of this V1Volume.
        :type: V1DataVolumeSource
        """

        self._data_volume = data_volume

    @property
    def downward_api(self):
        """
        Gets the downward_api of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :return: The downward_api of this V1Volume.
        :rtype: V1DownwardAPIVolumeSource
        """
        return self._downward_api

    @downward_api.setter
    def downward_api(self, downward_api):
        """
        Sets the downward_api of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :param downward_api: The downward_api of this V1Volume.
        :type: V1DownwardAPIVolumeSource
        """

        self._downward_api = downward_api

    @property
    def downward_metrics(self):
        """
        Gets the downward_metrics of this V1Volume.
        DownwardMetrics adds a very small disk to VMIs which contains a limited view of host and guest metrics. The disk content is compatible with vhostmd (https://github.com/vhostmd/vhostmd) and vm-dump-metrics.

        :return: The downward_metrics of this V1Volume.
        :rtype: V1DownwardMetricsVolumeSource
        """
        return self._downward_metrics

    @downward_metrics.setter
    def downward_metrics(self, downward_metrics):
        """
        Sets the downward_metrics of this V1Volume.
        DownwardMetrics adds a very small disk to VMIs which contains a limited view of host and guest metrics. The disk content is compatible with vhostmd (https://github.com/vhostmd/vhostmd) and vm-dump-metrics.

        :param downward_metrics: The downward_metrics of this V1Volume.
        :type: V1DownwardMetricsVolumeSource
        """

        self._downward_metrics = downward_metrics

    @property
    def empty_disk(self):
        """
        Gets the empty_disk of this V1Volume.
        EmptyDisk represents a temporary disk which shares the vmis lifecycle. More info: https://kubevirt.gitbooks.io/user-guide/disks-and-volumes.html

        :return: The empty_disk of this V1Volume.
        :rtype: V1EmptyDiskSource
        """
        return self._empty_disk

    @empty_disk.setter
    def empty_disk(self, empty_disk):
        """
        Sets the empty_disk of this V1Volume.
        EmptyDisk represents a temporary disk which shares the vmis lifecycle. More info: https://kubevirt.gitbooks.io/user-guide/disks-and-volumes.html

        :param empty_disk: The empty_disk of this V1Volume.
        :type: V1EmptyDiskSource
        """

        self._empty_disk = empty_disk

    @property
    def ephemeral(self):
        """
        Gets the ephemeral of this V1Volume.
        Ephemeral is a special volume source that \"wraps\" specified source and provides copy-on-write image on top of it.

        :return: The ephemeral of this V1Volume.
        :rtype: V1EphemeralVolumeSource
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral):
        """
        Sets the ephemeral of this V1Volume.
        Ephemeral is a special volume source that \"wraps\" specified source and provides copy-on-write image on top of it.

        :param ephemeral: The ephemeral of this V1Volume.
        :type: V1EphemeralVolumeSource
        """

        self._ephemeral = ephemeral

    @property
    def host_disk(self):
        """
        Gets the host_disk of this V1Volume.
        HostDisk represents a disk created on the cluster level

        :return: The host_disk of this V1Volume.
        :rtype: V1HostDisk
        """
        return self._host_disk

    @host_disk.setter
    def host_disk(self, host_disk):
        """
        Sets the host_disk of this V1Volume.
        HostDisk represents a disk created on the cluster level

        :param host_disk: The host_disk of this V1Volume.
        :type: V1HostDisk
        """

        self._host_disk = host_disk

    @property
    def memory_dump(self):
        """
        Gets the memory_dump of this V1Volume.
        MemoryDump is attached to the virt launcher and is populated with a memory dump of the vmi

        :return: The memory_dump of this V1Volume.
        :rtype: V1MemoryDumpVolumeSource
        """
        return self._memory_dump

    @memory_dump.setter
    def memory_dump(self, memory_dump):
        """
        Sets the memory_dump of this V1Volume.
        MemoryDump is attached to the virt launcher and is populated with a memory dump of the vmi

        :param memory_dump: The memory_dump of this V1Volume.
        :type: V1MemoryDumpVolumeSource
        """

        self._memory_dump = memory_dump

    @property
    def name(self):
        """
        Gets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the vmi. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :return: The name of this V1Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the vmi. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :param name: The name of this V1Volume.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def persistent_volume_claim(self):
        """
        Gets the persistent_volume_claim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. Directly attached to the vmi via qemu. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :return: The persistent_volume_claim of this V1Volume.
        :rtype: V1PersistentVolumeClaimVolumeSource
        """
        return self._persistent_volume_claim

    @persistent_volume_claim.setter
    def persistent_volume_claim(self, persistent_volume_claim):
        """
        Sets the persistent_volume_claim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. Directly attached to the vmi via qemu. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :param persistent_volume_claim: The persistent_volume_claim of this V1Volume.
        :type: V1PersistentVolumeClaimVolumeSource
        """

        self._persistent_volume_claim = persistent_volume_claim

    @property
    def secret(self):
        """
        Gets the secret of this V1Volume.
        SecretVolumeSource represents a reference to a secret data in the same namespace. More info: https://kubernetes.io/docs/concepts/configuration/secret/

        :return: The secret of this V1Volume.
        :rtype: V1SecretVolumeSource
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1Volume.
        SecretVolumeSource represents a reference to a secret data in the same namespace. More info: https://kubernetes.io/docs/concepts/configuration/secret/

        :param secret: The secret of this V1Volume.
        :type: V1SecretVolumeSource
        """

        self._secret = secret

    @property
    def service_account(self):
        """
        Gets the service_account of this V1Volume.
        ServiceAccountVolumeSource represents a reference to a service account. There can only be one volume of this type! More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :return: The service_account of this V1Volume.
        :rtype: V1ServiceAccountVolumeSource
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """
        Sets the service_account of this V1Volume.
        ServiceAccountVolumeSource represents a reference to a service account. There can only be one volume of this type! More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :param service_account: The service_account of this V1Volume.
        :type: V1ServiceAccountVolumeSource
        """

        self._service_account = service_account

    @property
    def sysprep(self):
        """
        Gets the sysprep of this V1Volume.
        Represents a Sysprep volume source.

        :return: The sysprep of this V1Volume.
        :rtype: V1SysprepSource
        """
        return self._sysprep

    @sysprep.setter
    def sysprep(self, sysprep):
        """
        Sets the sysprep of this V1Volume.
        Represents a Sysprep volume source.

        :param sysprep: The sysprep of this V1Volume.
        :type: V1SysprepSource
        """

        self._sysprep = sysprep

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
