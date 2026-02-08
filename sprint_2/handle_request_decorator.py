"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
Project1 Spring 2
File: handle_request_decorator.py
Purpose: This file contains the methods that handle decorators. It is supposed to eliminate as
        much repeatable code as possible when making a request.
"""
from typing import Callable
from functools import wraps
import requests


def get_request_exceptions() -> dict:
    """
    :return: a dictionary of exceptions and messages associated with it
    """
    return {
        requests.exceptions.RequestException: "Request Exception",
        requests.exceptions.ConnectionError: "Connection Error",
        requests.exceptions.HTTPError: "HTTP Error",
        requests.exceptions.Timeout: "Timeout",
        requests.exceptions.ConnectTimeout: "Connect Timeout",
        requests.exceptions.ReadTimeout: "Read Timeout",
        requests.exceptions.TooManyRedirects: "Too Many Redirects",
        requests.exceptions.URLRequired: "URL Required",
        requests.exceptions.InvalidURL: "Invalid URL",
        requests.exceptions.InvalidHeader: "Invalid Header",
        requests.exceptions.InvalidProxyURL: "Invalid Proxy URL",
        requests.exceptions.InvalidSchema: "Invalid Schema",
        requests.exceptions.ChunkedEncodingError: "Chunked Encoding Error",
        requests.exceptions.ContentDecodingError: "Content Decoding Error",
        requests.exceptions.StreamConsumedError: "Stream Consumed Error",
        requests.exceptions.RetryError: "Retry Error",
        requests.exceptions.JSONDecodeError: "InvalidJSONError"
    }


def handle_http_error(function_name: Callable, status_code: int, reason: str, message: str):
    """
    Handle http error separately
    :param function_name:
    :param status_code:
    :param reason:
    :param message:
    :return:None
    """
    print(f"There was an Exception in the method [{function_name}()]"
          f"\nMessage: {message}"
          f"\nStatus Code: {status_code}"
          f"\nReason: {reason}")
    raise SystemExit(1)


def handle_exception(function_name: Callable, exception: Exception, message: str = None) -> None:
    """
    Prints the function name, exception and message
    :param function_name:
    :param exception:
    :param message:
    :return:
    """
    print(f"There was an Exception in the method [{function_name}()]"
          f"\nMessage: {message} - \nException: {exception}")
    if message != "InvalidJSONError":
        raise SystemExit(1)


def handle_request_exceptions(function: Callable):
    """
    Gets a function and then wraps it with a function that handles exceptions
    :param function:
    :return: Callable
    """

    @wraps(function)
    def handle_function(*args, **kwargs) -> Callable or None:
        """
        Wrapper function that takes arguments and keyword arguments in a dictionary format
        Handles all errors as the same except HTTP error
            because I need the status code and the reason
        :param args:
        :param kwargs:
        :return: Callable or None
        """
        try:
            return function(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            handle_http_error(function.__name__, e.response.status_code,
                              e.response.reason, "HTTP error")
            return None
        except requests.exceptions.RequestException as e:
            message = get_request_exceptions().get(type(e), type(e).__name__)
            handle_exception(function.__name__, e, message)
            return None
    return handle_function
