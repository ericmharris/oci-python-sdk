# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Data(object):
    """
    The payload of the event. Information within `data` comes from the resource emitting the event.

    Example:

    -----
    {
    \"eventGroupingId\": null,
    \"eventName\": \"GetInstance\",
    \"compartmentId\": \"ocid1.tenancy.oc1..<unique_ID>\",
    \"compartmentName\": \"compartmentA\",
    \"resourceName\": \"my_instance\",
    \"resourceId\": \"ocid1.instance.oc1.phx.<unique_ID>\",
    \"availabilityDomain\": \"<availability_domain>\",
    \"freeformTags\": null,
    \"definedTags\": null,
    \"identity\": {
    \"principalName\": \"ExampleName\",
    \"principalId\": \"ocid1.user.oc1..<unique_ID>\",
    \"authType\": \"natv\",
    \"callerName\": null,
    \"callerId\": null,
    \"tenantId\": \"ocid1.tenancy.oc1..<unique_ID>\",
    \"ipAddress\": \"172.24.80.88\",
    \"credentials\": null,
    \"userAgent\": \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\",
    \"consoleSessionId\": null
    },
    \"request\": {
    \"id\": \"<unique_ID>\",
    \"path\": \"/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\",
    \"action\": \"GET\",
    \"parameters\": {},
    \"headers\": {
    \"opc-principal\": [
    \"{\\\"tenantId\\\":\\\"ocid1.tenancy.oc1..<unique_ID>\\\",\\\"subjectId\\\":\\\"ocid1.user.oc1..<unique_ID>\\\",\\\"claims\\\":[{\\\"key\\\":\\\"pstype\\\",\\\"value\\\":\\\"natv\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_host\\\",\\\"value\\\":\\\"iaas.r2.oracleiaas.com\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_opc-request-id\\\",\\\"value\\\":\\\"<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"ptype\\\",\\\"value\\\":\\\"user\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_date\\\",\\\"value\\\":\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_accept\\\",\\\"value\\\":\\\"application/json\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"authorization\\\",\\\"value\\\":\\\"Signature headers=\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\",keyId=\\\\\\\"ocid1.tenancy.oc1..<unique_ID>/ocid1.user.oc1..<unique_ID>/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\",algorithm=\\\\\\\"rsa-pss-sha256\\\\\\\",signature=\\\\\\\"<unique_ID>\\\\\\\",version=\\\\\\\"1\\\\\\\"\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_(request-target)\\\",\\\"value\\\":\\\"get /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"}]}\"
    ],
    \"Accept\": [
    \"application/json\"
    ],
    \"X-Oracle-Auth-Client-CN\": [
    \"splat-proxy-se-02302.node.ad2.r2\"
    ],
    \"X-Forwarded-Host\": [
    \"compute-api.svc.ad1.r2\"
    ],
    \"Connection\": [
    \"close\"
    ],
    \"User-Agent\": [
    \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\"
    ],
    \"X-Forwarded-For\": [
    \"172.24.80.88\"
    ],
    \"X-Real-IP\": [
    \"172.24.80.88\"
    ],
    \"oci-original-url\": [
    \"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\"
    ],
    \"opc-request-id\": [
    \"<unique_ID>\"
    ],
    \"Date\": [
    \"Wed, 18 Sep 2019 00:10:58 UTC\"
    ]
    }
    },
    \"response\": {
    \"status\": \"200\",
    \"responseTime\": \"2019-09-18T00:10:59.278Z\",
    \"headers\": {
    \"ETag\": [
    \"<unique_ID>\"
    ],
    \"Connection\": [
    \"close\"
    ],
    \"Content-Length\": [
    \"1828\"
    ],
    \"opc-request-id\": [
    \"<unique_ID>\"
    ],
    \"Date\": [
    \"Wed, 18 Sep 2019 00:10:59 GMT\"
    ],
    \"Content-Type\": [
    \"application/json\"
    ]
    },
    \"payload\": {
    \"resourceName\": \"my_instance\",
    \"id\": \"ocid1.instance.oc1.phx.<unique_ID>\"
    },
    \"message\": null
    },
    \"stateChange\": {
    \"previous\": null,
    \"current\": null
    },
    \"additionalDetails\": {
    \"imageId\": \"ocid1.image.oc1.phx.<unique_ID>\",
    \"shape\": \"VM.Standard1.1\",
    \"type\": \"CustomerVmi\"
    }
    }
    -----
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Data object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param event_grouping_id:
            The value to assign to the event_grouping_id property of this Data.
        :type event_grouping_id: str

        :param event_name:
            The value to assign to the event_name property of this Data.
        :type event_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Data.
        :type compartment_id: str

        :param compartment_name:
            The value to assign to the compartment_name property of this Data.
        :type compartment_name: str

        :param resource_name:
            The value to assign to the resource_name property of this Data.
        :type resource_name: str

        :param resource_id:
            The value to assign to the resource_id property of this Data.
        :type resource_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this Data.
        :type availability_domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Data.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Data.
        :type defined_tags: dict(str, dict(str, object))

        :param identity:
            The value to assign to the identity property of this Data.
        :type identity: Identity

        :param request:
            The value to assign to the request property of this Data.
        :type request: Request

        :param response:
            The value to assign to the response property of this Data.
        :type response: Response

        :param state_change:
            The value to assign to the state_change property of this Data.
        :type state_change: StateChange

        :param additional_details:
            The value to assign to the additional_details property of this Data.
        :type additional_details: dict(str, object)

        """
        self.swagger_types = {
            'event_grouping_id': 'str',
            'event_name': 'str',
            'compartment_id': 'str',
            'compartment_name': 'str',
            'resource_name': 'str',
            'resource_id': 'str',
            'availability_domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'identity': 'Identity',
            'request': 'Request',
            'response': 'Response',
            'state_change': 'StateChange',
            'additional_details': 'dict(str, object)'
        }

        self.attribute_map = {
            'event_grouping_id': 'eventGroupingId',
            'event_name': 'eventName',
            'compartment_id': 'compartmentId',
            'compartment_name': 'compartmentName',
            'resource_name': 'resourceName',
            'resource_id': 'resourceId',
            'availability_domain': 'availabilityDomain',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'identity': 'identity',
            'request': 'request',
            'response': 'response',
            'state_change': 'stateChange',
            'additional_details': 'additionalDetails'
        }

        self._event_grouping_id = None
        self._event_name = None
        self._compartment_id = None
        self._compartment_name = None
        self._resource_name = None
        self._resource_id = None
        self._availability_domain = None
        self._freeform_tags = None
        self._defined_tags = None
        self._identity = None
        self._request = None
        self._response = None
        self._state_change = None
        self._additional_details = None

    @property
    def event_grouping_id(self):
        """
        Gets the event_grouping_id of this Data.
        This value links multiple audit events that are part of the same API operation. For example,
        a long running API operations that emit an event at the start and the end of an operation
        would use the same value in this field for both events.


        :return: The event_grouping_id of this Data.
        :rtype: str
        """
        return self._event_grouping_id

    @event_grouping_id.setter
    def event_grouping_id(self, event_grouping_id):
        """
        Sets the event_grouping_id of this Data.
        This value links multiple audit events that are part of the same API operation. For example,
        a long running API operations that emit an event at the start and the end of an operation
        would use the same value in this field for both events.


        :param event_grouping_id: The event_grouping_id of this Data.
        :type: str
        """
        self._event_grouping_id = event_grouping_id

    @property
    def event_name(self):
        """
        Gets the event_name of this Data.
        Name of the API operation that generated this event.

        Example: `GetInstance`


        :return: The event_name of this Data.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this Data.
        Name of the API operation that generated this event.

        Example: `GetInstance`


        :param event_name: The event_name of this Data.
        :type: str
        """
        self._event_name = event_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Data.
        The `OCID`__ of the compartment of the resource
        emitting the event.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Data.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Data.
        The `OCID`__ of the compartment of the resource
        emitting the event.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Data.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_name(self):
        """
        Gets the compartment_name of this Data.
        The name of the compartment. This value is the friendly name associated with compartmentId.
        This value can change, but the service logs the value that appeared at the time of the audit
        event.

        Example: `CompartmentA`


        :return: The compartment_name of this Data.
        :rtype: str
        """
        return self._compartment_name

    @compartment_name.setter
    def compartment_name(self, compartment_name):
        """
        Sets the compartment_name of this Data.
        The name of the compartment. This value is the friendly name associated with compartmentId.
        This value can change, but the service logs the value that appeared at the time of the audit
        event.

        Example: `CompartmentA`


        :param compartment_name: The compartment_name of this Data.
        :type: str
        """
        self._compartment_name = compartment_name

    @property
    def resource_name(self):
        """
        Gets the resource_name of this Data.
        The name of the resource emitting the event.


        :return: The resource_name of this Data.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this Data.
        The name of the resource emitting the event.


        :param resource_name: The resource_name of this Data.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """
        Gets the resource_id of this Data.
        An `OCID`__ or some other ID for the resource
        emitting the event.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this Data.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this Data.
        An `OCID`__ or some other ID for the resource
        emitting the event.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this Data.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Data.
        The availability domain where the resource resides.


        :return: The availability_domain of this Data.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Data.
        The availability domain where the resource resides.


        :param availability_domain: The availability_domain of this Data.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Data.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
        type, or namespace. Exists for cross-compatibility only. For more information,
        see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Data.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Data.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
        type, or namespace. Exists for cross-compatibility only. For more information,
        see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Data.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Data.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more
        information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Data.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Data.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more
        information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Data.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def identity(self):
        """
        Gets the identity of this Data.

        :return: The identity of this Data.
        :rtype: Identity
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """
        Sets the identity of this Data.

        :param identity: The identity of this Data.
        :type: Identity
        """
        self._identity = identity

    @property
    def request(self):
        """
        Gets the request of this Data.

        :return: The request of this Data.
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this Data.

        :param request: The request of this Data.
        :type: Request
        """
        self._request = request

    @property
    def response(self):
        """
        Gets the response of this Data.

        :return: The response of this Data.
        :rtype: Response
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this Data.

        :param response: The response of this Data.
        :type: Response
        """
        self._response = response

    @property
    def state_change(self):
        """
        Gets the state_change of this Data.

        :return: The state_change of this Data.
        :rtype: StateChange
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        """
        Sets the state_change of this Data.

        :param state_change: The state_change of this Data.
        :type: StateChange
        """
        self._state_change = state_change

    @property
    def additional_details(self):
        """
        Gets the additional_details of this Data.
        A container object for attribues unique to the resource emitting the event.

        Example:

          -----
            {
              \"imageId\": \"ocid1.image.oc1.phx.<unique_ID>\",
              \"shape\": \"VM.Standard1.1\",
              \"type\": \"CustomerVmi\"
            }
          -----


        :return: The additional_details of this Data.
        :rtype: dict(str, object)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this Data.
        A container object for attribues unique to the resource emitting the event.

        Example:

          -----
            {
              \"imageId\": \"ocid1.image.oc1.phx.<unique_ID>\",
              \"shape\": \"VM.Standard1.1\",
              \"type\": \"CustomerVmi\"
            }
          -----


        :param additional_details: The additional_details of this Data.
        :type: dict(str, object)
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
