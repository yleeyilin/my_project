""" example for GitHub Actions with Sphinx """


def hello_world() -> str:
    """
    do the usual 'hello world'
    update stringsssss

    :return: Hello World
    :rtype: String
    """
    return "hello world!! :) "

def greeter_msg(*, greeter: str) -> str:
    """
    Custom greeting

    :param greeter: name of a person who message will be from
    :type greeter: str
    :return: a greeting from the greeter
    :rtype: str
    """
    return f"Hello to you from {greeter}"

def greeter_msg_2(*, greeter: str) -> str:
    """
    Custom greeting 2

    :param greeter: name of a person who message will be from
    :type greeter: str
    :return: a greeting from thmakee greeter
    :rtype: str
    """
    return f"Hello to you from {greeter}"

def greeter_msg_3(*, greeter: str) -> str:
    """
    Custom greeting 3

    :param greeter: name of a person who message will be from
    :type greeter: str
    :return: a greeting from thmakee greeter
    :rtype: str
    """
    return f"Hello to you from {greeter}"

def greeter_msg_4(*, greeter: str) -> str:
    """
    Custom greeting 4

    :param greeter: name of a person who message will be from
    :type greeter: str
    :return: a greeting from thmakee greeter
    :rtype: str
    """
    return f"Hello to you from {greeter}"
