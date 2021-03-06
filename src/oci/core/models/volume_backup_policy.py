# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeBackupPolicy(object):
    """
    A policy for automatically creating volume backups according to a
    recurring schedule. Has a set of one or more schedules that control when and
    how backups are created.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeBackupPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this VolumeBackupPolicy.
        :type display_name: str

        :param id:
            The value to assign to the id property of this VolumeBackupPolicy.
        :type id: str

        :param schedules:
            The value to assign to the schedules property of this VolumeBackupPolicy.
        :type schedules: list[VolumeBackupSchedule]

        :param time_created:
            The value to assign to the time_created property of this VolumeBackupPolicy.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeBackupPolicy.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VolumeBackupPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VolumeBackupPolicy.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'id': 'str',
            'schedules': 'list[VolumeBackupSchedule]',
            'time_created': 'datetime',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'schedules': 'schedules',
            'time_created': 'timeCreated',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._id = None
        self._schedules = None
        self._time_created = None
        self._compartment_id = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeBackupPolicy.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this VolumeBackupPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeBackupPolicy.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VolumeBackupPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeBackupPolicy.
        The OCID of the volume backup policy.


        :return: The id of this VolumeBackupPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeBackupPolicy.
        The OCID of the volume backup policy.


        :param id: The id of this VolumeBackupPolicy.
        :type: str
        """
        self._id = id

    @property
    def schedules(self):
        """
        **[Required]** Gets the schedules of this VolumeBackupPolicy.
        The collection of schedules that this policy will apply.


        :return: The schedules of this VolumeBackupPolicy.
        :rtype: list[VolumeBackupSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this VolumeBackupPolicy.
        The collection of schedules that this policy will apply.


        :param schedules: The schedules of this VolumeBackupPolicy.
        :type: list[VolumeBackupSchedule]
        """
        self._schedules = schedules

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeBackupPolicy.
        The date and time the volume backup policy was created. Format defined by RFC3339.


        :return: The time_created of this VolumeBackupPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeBackupPolicy.
        The date and time the volume backup policy was created. Format defined by RFC3339.


        :param time_created: The time_created of this VolumeBackupPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VolumeBackupPolicy.
        The OCID of the compartment that contains the volume backup.


        :return: The compartment_id of this VolumeBackupPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeBackupPolicy.
        The OCID of the compartment that contains the volume backup.


        :param compartment_id: The compartment_id of this VolumeBackupPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VolumeBackupPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VolumeBackupPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VolumeBackupPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VolumeBackupPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VolumeBackupPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VolumeBackupPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VolumeBackupPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VolumeBackupPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
