# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class JobStatusMeta(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        "total": "int",
        "processed": "int",
        "upload_method": "JobStatusUploadMethod",
        "is_registered": "bool",
    }

    attribute_map = {
        "total": "total",
        "processed": "processed",
        "upload_method": "uploadMethod",
        "is_registered": "isRegistered",
    }

    def __init__(
        self,
        total=None,
        processed=None,
        upload_method=None,
        is_registered=None,
        _configuration=None,
    ):  # noqa: E501
        """JobStatusMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total = None
        self._processed = None
        self._upload_method = None
        self._is_registered = None
        self.discriminator = None

        self.total = total
        self.processed = processed
        if upload_method is not None:
            self.upload_method = upload_method
        if is_registered is not None:
            self.is_registered = is_registered

    @property
    def total(self):
        """Gets the total of this JobStatusMeta.  # noqa: E501


        :return: The total of this JobStatusMeta.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this JobStatusMeta.


        :param total: The total of this JobStatusMeta.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total is None:
            raise ValueError(
                "Invalid value for `total`, must not be `None`"
            )  # noqa: E501

        self._total = total

    @property
    def processed(self):
        """Gets the processed of this JobStatusMeta.  # noqa: E501


        :return: The processed of this JobStatusMeta.  # noqa: E501
        :rtype: int
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """Sets the processed of this JobStatusMeta.


        :param processed: The processed of this JobStatusMeta.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and processed is None:
            raise ValueError(
                "Invalid value for `processed`, must not be `None`"
            )  # noqa: E501

        self._processed = processed

    @property
    def upload_method(self):
        """Gets the upload_method of this JobStatusMeta.  # noqa: E501


        :return: The upload_method of this JobStatusMeta.  # noqa: E501
        :rtype: JobStatusUploadMethod
        """
        return self._upload_method

    @upload_method.setter
    def upload_method(self, upload_method):
        """Sets the upload_method of this JobStatusMeta.


        :param upload_method: The upload_method of this JobStatusMeta.  # noqa: E501
        :type: JobStatusUploadMethod
        """

        self._upload_method = upload_method

    @property
    def is_registered(self):
        """Gets the is_registered of this JobStatusMeta.  # noqa: E501

        Flag which indicates whether the job was registered or not.  # noqa: E501

        :return: The is_registered of this JobStatusMeta.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this JobStatusMeta.

        Flag which indicates whether the job was registered or not.  # noqa: E501

        :param is_registered: The is_registered of this JobStatusMeta.  # noqa: E501
        :type: bool
        """

        self._is_registered = is_registered

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(JobStatusMeta, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobStatusMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStatusMeta):
            return True

        return self.to_dict() != other.to_dict()
