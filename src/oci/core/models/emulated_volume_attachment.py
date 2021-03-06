# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .volume_attachment import VolumeAttachment
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmulatedVolumeAttachment(VolumeAttachment):
    """
    An Emulated volume attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmulatedVolumeAttachment object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.EmulatedVolumeAttachment.attachment_type` attribute
        of this class is ``emulated`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachment_type:
            The value to assign to the attachment_type property of this EmulatedVolumeAttachment.
        :type attachment_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this EmulatedVolumeAttachment.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmulatedVolumeAttachment.
        :type compartment_id: str

        :param device:
            The value to assign to the device property of this EmulatedVolumeAttachment.
        :type device: str

        :param display_name:
            The value to assign to the display_name property of this EmulatedVolumeAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this EmulatedVolumeAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this EmulatedVolumeAttachment.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this EmulatedVolumeAttachment.
        :type is_read_only: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmulatedVolumeAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this EmulatedVolumeAttachment.
        :type time_created: datetime

        :param volume_id:
            The value to assign to the volume_id property of this EmulatedVolumeAttachment.
        :type volume_id: str

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this EmulatedVolumeAttachment.
        :type is_pv_encryption_in_transit_enabled: bool

        """
        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'device': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'volume_id': 'str',
            'is_pv_encryption_in_transit_enabled': 'bool'
        }

        self.attribute_map = {
            'attachment_type': 'attachmentType',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'device': 'device',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'volume_id': 'volumeId',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled'
        }

        self._attachment_type = None
        self._availability_domain = None
        self._compartment_id = None
        self._device = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._is_read_only = None
        self._lifecycle_state = None
        self._time_created = None
        self._volume_id = None
        self._is_pv_encryption_in_transit_enabled = None
        self._attachment_type = 'emulated'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
