# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from nvd_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nvd_api import schemas  # noqa: F401

from nvd_api.model.cpe_oas import CpeOas

from . import path

# Query params
CpeNameIdSchema = schemas.UUIDSchema
CpeMatchStringSchema = schemas.StrSchema


class KeywordExactMatchSchema(
    schemas.BoolBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneBoolMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'KeywordExactMatchSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
KeywordSearchSchema = schemas.StrSchema
LastModStartDateSchema = schemas.DateTimeSchema
LastModEndDateSchema = schemas.DateTimeSchema
MatchCriteriaIdSchema = schemas.UUIDSchema


class ResultsPerPageSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 10000
        inclusive_minimum = 0


class StartIndexSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_minimum = 0
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'cpeNameId': typing.Union[CpeNameIdSchema, str, uuid.UUID, ],
        'cpeMatchString': typing.Union[CpeMatchStringSchema, str, ],
        'keywordExactMatch': typing.Union[KeywordExactMatchSchema, None, bool, ],
        'keywordSearch': typing.Union[KeywordSearchSchema, str, ],
        'lastModStartDate': typing.Union[LastModStartDateSchema, str, datetime, ],
        'lastModEndDate': typing.Union[LastModEndDateSchema, str, datetime, ],
        'matchCriteriaId': typing.Union[MatchCriteriaIdSchema, str, uuid.UUID, ],
        'resultsPerPage': typing.Union[ResultsPerPageSchema, decimal.Decimal, int, ],
        'startIndex': typing.Union[StartIndexSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_cpe_name_id = api_client.QueryParameter(
    name="cpeNameId",
    style=api_client.ParameterStyle.FORM,
    schema=CpeNameIdSchema,
    explode=True,
)
request_query_cpe_match_string = api_client.QueryParameter(
    name="cpeMatchString",
    style=api_client.ParameterStyle.FORM,
    schema=CpeMatchStringSchema,
    explode=True,
)
request_query_keyword_exact_match = api_client.QueryParameter(
    name="keywordExactMatch",
    style=api_client.ParameterStyle.FORM,
    schema=KeywordExactMatchSchema,
    explode=True,
)
request_query_keyword_search = api_client.QueryParameter(
    name="keywordSearch",
    style=api_client.ParameterStyle.FORM,
    schema=KeywordSearchSchema,
    explode=True,
)
request_query_last_mod_start_date = api_client.QueryParameter(
    name="lastModStartDate",
    style=api_client.ParameterStyle.FORM,
    schema=LastModStartDateSchema,
    explode=True,
)
request_query_last_mod_end_date = api_client.QueryParameter(
    name="lastModEndDate",
    style=api_client.ParameterStyle.FORM,
    schema=LastModEndDateSchema,
    explode=True,
)
request_query_match_criteria_id = api_client.QueryParameter(
    name="matchCriteriaId",
    style=api_client.ParameterStyle.FORM,
    schema=MatchCriteriaIdSchema,
    explode=True,
)
request_query_results_per_page = api_client.QueryParameter(
    name="resultsPerPage",
    style=api_client.ParameterStyle.FORM,
    schema=ResultsPerPageSchema,
    explode=True,
)
request_query_start_index = api_client.QueryParameter(
    name="startIndex",
    style=api_client.ParameterStyle.FORM,
    schema=StartIndexSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = CpeOas


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_cpes_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_cpes_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_cpes_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_cpes_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        CPE API
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_cpe_name_id,
            request_query_cpe_match_string,
            request_query_keyword_exact_match,
            request_query_keyword_search,
            request_query_last_mod_start_date,
            request_query_last_mod_end_date,
            request_query_match_criteria_id,
            request_query_results_per_page,
            request_query_start_index,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class GetCpes(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_cpes(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_cpes(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_cpes(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_cpes(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_cpes_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_cpes_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

