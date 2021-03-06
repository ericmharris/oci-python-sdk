# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupDestinationDetails(object):
    """
    Backup destination details
    """

    #: A constant which can be used with the type property of a BackupDestinationDetails.
    #: This constant has a value of "NFS"
    TYPE_NFS = "NFS"

    #: A constant which can be used with the type property of a BackupDestinationDetails.
    #: This constant has a value of "RECOVERY_APPLIANCE"
    TYPE_RECOVERY_APPLIANCE = "RECOVERY_APPLIANCE"

    #: A constant which can be used with the type property of a BackupDestinationDetails.
    #: This constant has a value of "OBJECT_STORE"
    TYPE_OBJECT_STORE = "OBJECT_STORE"

    #: A constant which can be used with the type property of a BackupDestinationDetails.
    #: This constant has a value of "LOCAL"
    TYPE_LOCAL = "LOCAL"

    def __init__(self, **kwargs):
        """
        Initializes a new BackupDestinationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BackupDestinationDetails.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE", "OBJECT_STORE", "LOCAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param id:
            The value to assign to the id property of this BackupDestinationDetails.
        :type id: str

        :param vpc_user:
            The value to assign to the vpc_user property of this BackupDestinationDetails.
        :type vpc_user: str

        :param vpc_password:
            The value to assign to the vpc_password property of this BackupDestinationDetails.
        :type vpc_password: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'vpc_user': 'str',
            'vpc_password': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'vpc_user': 'vpcUser',
            'vpc_password': 'vpcPassword',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type = None
        self._id = None
        self._vpc_user = None
        self._vpc_password = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BackupDestinationDetails.
        Type of the database backup destination.

        Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE", "OBJECT_STORE", "LOCAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this BackupDestinationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BackupDestinationDetails.
        Type of the database backup destination.


        :param type: The type of this BackupDestinationDetails.
        :type: str
        """
        allowed_values = ["NFS", "RECOVERY_APPLIANCE", "OBJECT_STORE", "LOCAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def id(self):
        """
        Gets the id of this BackupDestinationDetails.
        The `OCID`__ of the backup destination.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this BackupDestinationDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BackupDestinationDetails.
        The `OCID`__ of the backup destination.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this BackupDestinationDetails.
        :type: str
        """
        self._id = id

    @property
    def vpc_user(self):
        """
        Gets the vpc_user of this BackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.


        :return: The vpc_user of this BackupDestinationDetails.
        :rtype: str
        """
        return self._vpc_user

    @vpc_user.setter
    def vpc_user(self, vpc_user):
        """
        Sets the vpc_user of this BackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.


        :param vpc_user: The vpc_user of this BackupDestinationDetails.
        :type: str
        """
        self._vpc_user = vpc_user

    @property
    def vpc_password(self):
        """
        Gets the vpc_password of this BackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.


        :return: The vpc_password of this BackupDestinationDetails.
        :rtype: str
        """
        return self._vpc_password

    @vpc_password.setter
    def vpc_password(self, vpc_password):
        """
        Sets the vpc_password of this BackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.


        :param vpc_password: The vpc_password of this BackupDestinationDetails.
        :type: str
        """
        self._vpc_password = vpc_password

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BackupDestinationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BackupDestinationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BackupDestinationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BackupDestinationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
