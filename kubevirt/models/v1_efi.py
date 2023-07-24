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


class V1EFI(object):
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
        'persistent': 'bool',
        'secure_boot': 'bool'
    }

    attribute_map = {
        'persistent': 'persistent',
        'secure_boot': 'secureBoot'
    }

    def __init__(self, persistent=None, secure_boot=None):
        """
        V1EFI - a model defined in Swagger
        """

        self._persistent = None
        self._secure_boot = None

        if persistent is not None:
          self.persistent = persistent
        if secure_boot is not None:
          self.secure_boot = secure_boot

    @property
    def persistent(self):
        """
        Gets the persistent of this V1EFI.
        If set to true, Persistent will persist the EFI NVRAM across reboots. Defaults to false

        :return: The persistent of this V1EFI.
        :rtype: bool
        """
        return self._persistent

    @persistent.setter
    def persistent(self, persistent):
        """
        Sets the persistent of this V1EFI.
        If set to true, Persistent will persist the EFI NVRAM across reboots. Defaults to false

        :param persistent: The persistent of this V1EFI.
        :type: bool
        """

        self._persistent = persistent

    @property
    def secure_boot(self):
        """
        Gets the secure_boot of this V1EFI.
        If set, SecureBoot will be enabled and the OVMF roms will be swapped for SecureBoot-enabled ones. Requires SMM to be enabled. Defaults to true

        :return: The secure_boot of this V1EFI.
        :rtype: bool
        """
        return self._secure_boot

    @secure_boot.setter
    def secure_boot(self, secure_boot):
        """
        Sets the secure_boot of this V1EFI.
        If set, SecureBoot will be enabled and the OVMF roms will be swapped for SecureBoot-enabled ones. Requires SMM to be enabled. Defaults to true

        :param secure_boot: The secure_boot of this V1EFI.
        :type: bool
        """

        self._secure_boot = secure_boot

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
        if not isinstance(other, V1EFI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
