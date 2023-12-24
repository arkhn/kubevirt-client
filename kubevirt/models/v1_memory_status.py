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


class V1MemoryStatus(object):
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
        'guest_at_boot': 'K8sIoApimachineryPkgApiResourceQuantity',
        'guest_current': 'K8sIoApimachineryPkgApiResourceQuantity',
        'guest_requested': 'K8sIoApimachineryPkgApiResourceQuantity'
    }

    attribute_map = {
        'guest_at_boot': 'guestAtBoot',
        'guest_current': 'guestCurrent',
        'guest_requested': 'guestRequested'
    }

    def __init__(self, guest_at_boot=None, guest_current=None, guest_requested=None):
        """
        V1MemoryStatus - a model defined in Swagger
        """

        self._guest_at_boot = None
        self._guest_current = None
        self._guest_requested = None

        if guest_at_boot is not None:
          self.guest_at_boot = guest_at_boot
        if guest_current is not None:
          self.guest_current = guest_current
        if guest_requested is not None:
          self.guest_requested = guest_requested

    @property
    def guest_at_boot(self):
        """
        Gets the guest_at_boot of this V1MemoryStatus.
        GuestAtBoot specifies with how much memory the VirtualMachine intiallly booted with.

        :return: The guest_at_boot of this V1MemoryStatus.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._guest_at_boot

    @guest_at_boot.setter
    def guest_at_boot(self, guest_at_boot):
        """
        Sets the guest_at_boot of this V1MemoryStatus.
        GuestAtBoot specifies with how much memory the VirtualMachine intiallly booted with.

        :param guest_at_boot: The guest_at_boot of this V1MemoryStatus.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._guest_at_boot = guest_at_boot

    @property
    def guest_current(self):
        """
        Gets the guest_current of this V1MemoryStatus.
        GuestCurrent specifies how much memory is currently available for the VirtualMachine.

        :return: The guest_current of this V1MemoryStatus.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._guest_current

    @guest_current.setter
    def guest_current(self, guest_current):
        """
        Sets the guest_current of this V1MemoryStatus.
        GuestCurrent specifies how much memory is currently available for the VirtualMachine.

        :param guest_current: The guest_current of this V1MemoryStatus.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._guest_current = guest_current

    @property
    def guest_requested(self):
        """
        Gets the guest_requested of this V1MemoryStatus.
        GuestRequested specifies how much memory was requested (hotplug) for the VirtualMachine.

        :return: The guest_requested of this V1MemoryStatus.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._guest_requested

    @guest_requested.setter
    def guest_requested(self, guest_requested):
        """
        Sets the guest_requested of this V1MemoryStatus.
        GuestRequested specifies how much memory was requested (hotplug) for the VirtualMachine.

        :param guest_requested: The guest_requested of this V1MemoryStatus.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._guest_requested = guest_requested

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
        if not isinstance(other, V1MemoryStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other