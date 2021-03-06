# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBootVolumeDetails(object):
    """
    UpdateBootVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBootVolumeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBootVolumeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateBootVolumeDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBootVolumeDetails.
        :type freeform_tags: dict(str, str)

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this UpdateBootVolumeDetails.
        :type size_in_gbs: int

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'size_in_gbs': 'int'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'size_in_gbs': 'sizeInGBs'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._size_in_gbs = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBootVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateBootVolumeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBootVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateBootVolumeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateBootVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateBootVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateBootVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateBootVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBootVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateBootVolumeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBootVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateBootVolumeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this UpdateBootVolumeDetails.
        The size to resize the volume to in GBs. Has to be larger than the current size.


        :return: The size_in_gbs of this UpdateBootVolumeDetails.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this UpdateBootVolumeDetails.
        The size to resize the volume to in GBs. Has to be larger than the current size.


        :param size_in_gbs: The size_in_gbs of this UpdateBootVolumeDetails.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
