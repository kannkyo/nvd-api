"""
    NVD API 2.0 Python API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: 15080890+kannkyo@users.noreply.github.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
import re  # noqa: F401
import sys  # noqa: F401

from nvd_api.low_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from nvd_api.low_api.exceptions import ApiAttributeError
from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_descriptions_inner import CveOasVulnerabilitiesInnerCveDescriptionsInner
from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_references_inner import CveOasVulnerabilitiesInnerCveReferencesInner


def lazy_import():
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_configurations_inner import CveOasVulnerabilitiesInnerCveConfigurationsInner
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_descriptions_inner import CveOasVulnerabilitiesInnerCveDescriptionsInner
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_metrics import CveOasVulnerabilitiesInnerCveMetrics
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_references_inner import CveOasVulnerabilitiesInnerCveReferencesInner
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_vendor_comments_inner import CveOasVulnerabilitiesInnerCveVendorCommentsInner
    from nvd_api.low_api.model.cve_oas_vulnerabilities_inner_cve_weaknesses_inner import CveOasVulnerabilitiesInnerCveWeaknessesInner
    globals()['CveOasVulnerabilitiesInnerCveConfigurationsInner'] = CveOasVulnerabilitiesInnerCveConfigurationsInner
    globals()['CveOasVulnerabilitiesInnerCveDescriptionsInner'] = CveOasVulnerabilitiesInnerCveDescriptionsInner
    globals()['CveOasVulnerabilitiesInnerCveMetrics'] = CveOasVulnerabilitiesInnerCveMetrics
    globals()['CveOasVulnerabilitiesInnerCveReferencesInner'] = CveOasVulnerabilitiesInnerCveReferencesInner
    globals()['CveOasVulnerabilitiesInnerCveVendorCommentsInner'] = CveOasVulnerabilitiesInnerCveVendorCommentsInner
    globals()['CveOasVulnerabilitiesInnerCveWeaknessesInner'] = CveOasVulnerabilitiesInnerCveWeaknessesInner


class CveOasVulnerabilitiesInnerCve(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('id',): {
            'regex': {
                'pattern': r'^CVE-[0-9]{4}-[0-9]{4,}$',  # noqa: E501
            },
        },
        ('descriptions',): {
            'min_items': 1,
        },
        ('references',): {
            'max_items': 500,
            'min_items': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'published': (datetime,),  # noqa: E501
            'last_modified': (datetime,),  # noqa: E501
            'descriptions': ([CveOasVulnerabilitiesInnerCveDescriptionsInner],),  # noqa: E501
            'references': ([CveOasVulnerabilitiesInnerCveReferencesInner],),  # noqa: E501
            'source_identifier': (str,),  # noqa: E501
            'vuln_status': (str,),  # noqa: E501
            'evaluator_comment': (str,),  # noqa: E501
            'evaluator_solution': (str,),  # noqa: E501
            'evaluator_impact': (str,),  # noqa: E501
            'cisa_exploit_add': (date,),  # noqa: E501
            'cisa_action_due': (date,),  # noqa: E501
            'cisa_required_action': (str,),  # noqa: E501
            'cisa_vulnerability_name': (str,),  # noqa: E501
            'metrics': (CveOasVulnerabilitiesInnerCveMetrics,),  # noqa: E501
            'weaknesses': ([CveOasVulnerabilitiesInnerCveWeaknessesInner],),  # noqa: E501
            'configurations': ([CveOasVulnerabilitiesInnerCveConfigurationsInner],),  # noqa: E501
            'vendor_comments': ([CveOasVulnerabilitiesInnerCveVendorCommentsInner],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'published': 'published',  # noqa: E501
        'last_modified': 'lastModified',  # noqa: E501
        'descriptions': 'descriptions',  # noqa: E501
        'references': 'references',  # noqa: E501
        'source_identifier': 'sourceIdentifier',  # noqa: E501
        'vuln_status': 'vulnStatus',  # noqa: E501
        'evaluator_comment': 'evaluatorComment',  # noqa: E501
        'evaluator_solution': 'evaluatorSolution',  # noqa: E501
        'evaluator_impact': 'evaluatorImpact',  # noqa: E501
        'cisa_exploit_add': 'cisaExploitAdd',  # noqa: E501
        'cisa_action_due': 'cisaActionDue',  # noqa: E501
        'cisa_required_action': 'cisaRequiredAction',  # noqa: E501
        'cisa_vulnerability_name': 'cisaVulnerabilityName',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'weaknesses': 'weaknesses',  # noqa: E501
        'configurations': 'configurations',  # noqa: E501
        'vendor_comments': 'vendorComments',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, published, last_modified, descriptions, references, *args, **kwargs):  # noqa: E501
        """CveOasVulnerabilitiesInnerCve - a model defined in OpenAPI

        Args:
            id (str):
            published (datetime):
            last_modified (datetime):
            descriptions ([CveOasVulnerabilitiesInnerCveDescriptionsInner]):
            references ([CveOasVulnerabilitiesInnerCveReferencesInner]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            source_identifier (str): [optional]  # noqa: E501
            vuln_status (str): [optional]  # noqa: E501
            evaluator_comment (str): [optional]  # noqa: E501
            evaluator_solution (str): [optional]  # noqa: E501
            evaluator_impact (str): [optional]  # noqa: E501
            cisa_exploit_add (date): [optional]  # noqa: E501
            cisa_action_due (date): [optional]  # noqa: E501
            cisa_required_action (str): [optional]  # noqa: E501
            cisa_vulnerability_name (str): [optional]  # noqa: E501
            metrics (CveOasVulnerabilitiesInnerCveMetrics): [optional]  # noqa: E501
            weaknesses ([CveOasVulnerabilitiesInnerCveWeaknessesInner]): [optional]  # noqa: E501
            configurations ([CveOasVulnerabilitiesInnerCveConfigurationsInner]): [optional]  # noqa: E501
            vendor_comments ([CveOasVulnerabilitiesInnerCveVendorCommentsInner]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.published = published
        self.last_modified = last_modified
        self.descriptions = descriptions
        self.references = references
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id: str, published: datetime, last_modified: datetime, descriptions: list[CveOasVulnerabilitiesInnerCveDescriptionsInner], references: list[CveOasVulnerabilitiesInnerCveReferencesInner], *args, **kwargs):  # noqa: E501
        """CveOasVulnerabilitiesInnerCve - a model defined in OpenAPI

        Args:
            id (str):
            published (datetime):
            last_modified (datetime):
            descriptions ([CveOasVulnerabilitiesInnerCveDescriptionsInner]):
            references ([CveOasVulnerabilitiesInnerCveReferencesInner]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            source_identifier (str): [optional]  # noqa: E501
            vuln_status (str): [optional]  # noqa: E501
            evaluator_comment (str): [optional]  # noqa: E501
            evaluator_solution (str): [optional]  # noqa: E501
            evaluator_impact (str): [optional]  # noqa: E501
            cisa_exploit_add (date): [optional]  # noqa: E501
            cisa_action_due (date): [optional]  # noqa: E501
            cisa_required_action (str): [optional]  # noqa: E501
            cisa_vulnerability_name (str): [optional]  # noqa: E501
            metrics (CveOasVulnerabilitiesInnerCveMetrics): [optional]  # noqa: E501
            weaknesses ([CveOasVulnerabilitiesInnerCveWeaknessesInner]): [optional]  # noqa: E501
            configurations ([CveOasVulnerabilitiesInnerCveConfigurationsInner]): [optional]  # noqa: E501
            vendor_comments ([CveOasVulnerabilitiesInnerCveVendorCommentsInner]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.published = published
        self.last_modified = last_modified
        self.descriptions = descriptions
        self.references = references
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
