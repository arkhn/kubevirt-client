# coding: utf-8

"""


    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DiskSource(object):
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
        'file': 'str',
        'startup_policy': 'str',
        'protocol': 'str',
        'name': 'str',
        'host': 'V1DiskSourceHost'
    }

    attribute_map = {
        'file': 'file',
        'startup_policy': 'startupPolicy',
        'protocol': 'protocol',
        'name': 'name',
        'host': 'host'
    }

    def __init__(self, file=None, startup_policy=None, protocol=None, name=None, host=None):
        """
        V1DiskSource - a model defined in Swagger
        """

        self._file = None
        self._startup_policy = None
        self._protocol = None
        self._name = None
        self._host = None
        self.discriminator = None

        if file is not None:
          self.file = file
        if startup_policy is not None:
          self.startup_policy = startup_policy
        if protocol is not None:
          self.protocol = protocol
        if name is not None:
          self.name = name
        if host is not None:
          self.host = host

    @property
    def file(self):
        """
        Gets the file of this V1DiskSource.

        :return: The file of this V1DiskSource.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this V1DiskSource.

        :param file: The file of this V1DiskSource.
        :type: str
        """

        self._file = file

    @property
    def startup_policy(self):
        """
        Gets the startup_policy of this V1DiskSource.

        :return: The startup_policy of this V1DiskSource.
        :rtype: str
        """
        return self._startup_policy

    @startup_policy.setter
    def startup_policy(self, startup_policy):
        """
        Sets the startup_policy of this V1DiskSource.

        :param startup_policy: The startup_policy of this V1DiskSource.
        :type: str
        """

        self._startup_policy = startup_policy

    @property
    def protocol(self):
        """
        Gets the protocol of this V1DiskSource.

        :return: The protocol of this V1DiskSource.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1DiskSource.

        :param protocol: The protocol of this V1DiskSource.
        :type: str
        """

        self._protocol = protocol

    @property
    def name(self):
        """
        Gets the name of this V1DiskSource.

        :return: The name of this V1DiskSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1DiskSource.

        :param name: The name of this V1DiskSource.
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """
        Gets the host of this V1DiskSource.

        :return: The host of this V1DiskSource.
        :rtype: V1DiskSourceHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1DiskSource.

        :param host: The host of this V1DiskSource.
        :type: V1DiskSourceHost
        """

        self._host = host

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
        if not isinstance(other, V1DiskSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
