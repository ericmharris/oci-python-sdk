# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferApplianceCertificate(object):
    """
    TransferApplianceCertificate model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TransferApplianceCertificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate:
            The value to assign to the certificate property of this TransferApplianceCertificate.
        :type certificate: str

        """
        self.swagger_types = {
            'certificate': 'str'
        }

        self.attribute_map = {
            'certificate': 'certificate'
        }

        self._certificate = None

    @property
    def certificate(self):
        """
        Gets the certificate of this TransferApplianceCertificate.

        :return: The certificate of this TransferApplianceCertificate.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this TransferApplianceCertificate.

        :param certificate: The certificate of this TransferApplianceCertificate.
        :type: str
        """
        self._certificate = certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
