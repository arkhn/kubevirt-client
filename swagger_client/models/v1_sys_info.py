# coding: utf-8

"""


    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1SysInfo(object):
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
        'type': 'str',
        'system': 'list[V1Entry]',
        'bios': 'list[V1Entry]',
        'base_board': 'list[V1Entry]'
    }

    attribute_map = {
        'type': 'type',
        'system': 'system',
        'bios': 'bios',
        'base_board': 'baseBoard'
    }

    def __init__(self, type=None, system=None, bios=None, base_board=None):
        """
        V1SysInfo - a model defined in Swagger
        """

        self._type = None
        self._system = None
        self._bios = None
        self._base_board = None
        self.discriminator = None

        self.type = type
        self.system = system
        self.bios = bios
        self.base_board = base_board

    @property
    def type(self):
        """
        Gets the type of this V1SysInfo.

        :return: The type of this V1SysInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1SysInfo.

        :param type: The type of this V1SysInfo.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def system(self):
        """
        Gets the system of this V1SysInfo.

        :return: The system of this V1SysInfo.
        :rtype: list[V1Entry]
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this V1SysInfo.

        :param system: The system of this V1SysInfo.
        :type: list[V1Entry]
        """
        if system is None:
            raise ValueError("Invalid value for `system`, must not be `None`")

        self._system = system

    @property
    def bios(self):
        """
        Gets the bios of this V1SysInfo.

        :return: The bios of this V1SysInfo.
        :rtype: list[V1Entry]
        """
        return self._bios

    @bios.setter
    def bios(self, bios):
        """
        Sets the bios of this V1SysInfo.

        :param bios: The bios of this V1SysInfo.
        :type: list[V1Entry]
        """
        if bios is None:
            raise ValueError("Invalid value for `bios`, must not be `None`")

        self._bios = bios

    @property
    def base_board(self):
        """
        Gets the base_board of this V1SysInfo.

        :return: The base_board of this V1SysInfo.
        :rtype: list[V1Entry]
        """
        return self._base_board

    @base_board.setter
    def base_board(self, base_board):
        """
        Sets the base_board of this V1SysInfo.

        :param base_board: The base_board of this V1SysInfo.
        :type: list[V1Entry]
        """
        if base_board is None:
            raise ValueError("Invalid value for `base_board`, must not be `None`")

        self._base_board = base_board

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
        if not isinstance(other, V1SysInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
