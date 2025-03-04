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


class DatasourceConfigS3(object):
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
        's3_region': 'str',
        's3_access_key_id': 'str',
        's3_secret_access_key': 'str'
    }

    attribute_map = {
        's3_region': 's3Region',
        's3_access_key_id': 's3AccessKeyId',
        's3_secret_access_key': 's3SecretAccessKey'
    }

    def __init__(self, s3_region=None, s3_access_key_id=None, s3_secret_access_key=None, _configuration=None):  # noqa: E501
        """DatasourceConfigS3 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._s3_region = None
        self._s3_access_key_id = None
        self._s3_secret_access_key = None
        self.discriminator = None

        self.s3_region = s3_region
        self.s3_access_key_id = s3_access_key_id
        self.s3_secret_access_key = s3_secret_access_key

    @property
    def s3_region(self):
        """Gets the s3_region of this DatasourceConfigS3.  # noqa: E501

        the region where your bucket is located (see https://docs.aws.amazon.com/general/latest/gr/s3.html for further information)  # noqa: E501

        :return: The s3_region of this DatasourceConfigS3.  # noqa: E501
        :rtype: str
        """
        return self._s3_region

    @s3_region.setter
    def s3_region(self, s3_region):
        """Sets the s3_region of this DatasourceConfigS3.

        the region where your bucket is located (see https://docs.aws.amazon.com/general/latest/gr/s3.html for further information)  # noqa: E501

        :param s3_region: The s3_region of this DatasourceConfigS3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and s3_region is None:
            raise ValueError("Invalid value for `s3_region`, must not be `None`")  # noqa: E501
        allowed_values = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "us-gov-west-1", "us-gov-east-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "sa-east-1", "cn-north-1", "cn-northwest-1", "ap-east-1", "ap-south-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "me-south-1"]  # noqa: E501
        if (self._configuration.client_side_validation and
                s3_region not in allowed_values):
            raise ValueError(
                "Invalid value for `s3_region` ({0}), must be one of {1}"  # noqa: E501
                .format(s3_region, allowed_values)
            )

        self._s3_region = s3_region

    @property
    def s3_access_key_id(self):
        """Gets the s3_access_key_id of this DatasourceConfigS3.  # noqa: E501

        the accessKeyId of the credential you are providing Lightly to use  # noqa: E501

        :return: The s3_access_key_id of this DatasourceConfigS3.  # noqa: E501
        :rtype: str
        """
        return self._s3_access_key_id

    @s3_access_key_id.setter
    def s3_access_key_id(self, s3_access_key_id):
        """Sets the s3_access_key_id of this DatasourceConfigS3.

        the accessKeyId of the credential you are providing Lightly to use  # noqa: E501

        :param s3_access_key_id: The s3_access_key_id of this DatasourceConfigS3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and s3_access_key_id is None:
            raise ValueError("Invalid value for `s3_access_key_id`, must not be `None`")  # noqa: E501

        self._s3_access_key_id = s3_access_key_id

    @property
    def s3_secret_access_key(self):
        """Gets the s3_secret_access_key of this DatasourceConfigS3.  # noqa: E501

        the secretAccessKey of the credential you are providing Lightly to use  # noqa: E501

        :return: The s3_secret_access_key of this DatasourceConfigS3.  # noqa: E501
        :rtype: str
        """
        return self._s3_secret_access_key

    @s3_secret_access_key.setter
    def s3_secret_access_key(self, s3_secret_access_key):
        """Sets the s3_secret_access_key of this DatasourceConfigS3.

        the secretAccessKey of the credential you are providing Lightly to use  # noqa: E501

        :param s3_secret_access_key: The s3_secret_access_key of this DatasourceConfigS3.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and s3_secret_access_key is None:
            raise ValueError("Invalid value for `s3_secret_access_key`, must not be `None`")  # noqa: E501

        self._s3_secret_access_key = s3_secret_access_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DatasourceConfigS3, dict):
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
        if not isinstance(other, DatasourceConfigS3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasourceConfigS3):
            return True

        return self.to_dict() != other.to_dict()
