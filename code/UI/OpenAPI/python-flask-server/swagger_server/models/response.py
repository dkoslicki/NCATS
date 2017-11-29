# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.response_result import ResponseResult
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Response(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, code: int=None, code_string: str=None, message: str=None, result: ResponseResult=None):
        """
        Response - a model defined in Swagger

        :param id: The id of this Response.
        :type id: int
        :param code: The code of this Response.
        :type code: int
        :param code_string: The code_string of this Response.
        :type code_string: str
        :param message: The message of this Response.
        :type message: str
        :param result: The result of this Response.
        :type result: ResponseResult
        """
        self.swagger_types = {
            'id': int,
            'code': int,
            'code_string': str,
            'message': str,
            'result': ResponseResult
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'code_string': 'codeString',
            'message': 'message',
            'result': 'result'
        }

        self._id = id
        self._code = code
        self._code_string = code_string
        self._message = message
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'Response':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Response of this Response.
        :rtype: Response
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Response.
        Internal identifier of the response

        :return: The id of this Response.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Response.
        Internal identifier of the response

        :param id: The id of this Response.
        :type id: int
        """

        self._id = id

    @property
    def code(self) -> int:
        """
        Gets the code of this Response.
        Numeric code denoting the success or failture of the response

        :return: The code of this Response.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """
        Sets the code of this Response.
        Numeric code denoting the success or failture of the response

        :param code: The code of this Response.
        :type code: int
        """

        self._code = code

    @property
    def code_string(self) -> str:
        """
        Gets the code_string of this Response.
        String code denoting the success or failture of the response

        :return: The code_string of this Response.
        :rtype: str
        """
        return self._code_string

    @code_string.setter
    def code_string(self, code_string: str):
        """
        Sets the code_string of this Response.
        String code denoting the success or failture of the response

        :param code_string: The code_string of this Response.
        :type code_string: str
        """

        self._code_string = code_string

    @property
    def message(self) -> str:
        """
        Gets the message of this Response.
        Extended message denoting the success or failture of the response

        :return: The message of this Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this Response.
        Extended message denoting the success or failture of the response

        :param message: The message of this Response.
        :type message: str
        """

        self._message = message

    @property
    def result(self) -> ResponseResult:
        """
        Gets the result of this Response.

        :return: The result of this Response.
        :rtype: ResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: ResponseResult):
        """
        Sets the result of this Response.

        :param result: The result of this Response.
        :type result: ResponseResult
        """

        self._result = result

