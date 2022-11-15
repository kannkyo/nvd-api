# -*- coding: utf-8 -*-

import pytest
from my_project.skeleton import __fib, __parse_args, __setup_logging, main
import logging


def test_fib():
    assert __fib(1) == 1
    assert __fib(2) == 1
    assert __fib(7) == 13
    with pytest.raises(AssertionError):
        __fib(-10)


def test_parse_args():
    args = __parse_args(["--verbose", "1"])
    assert args.loglevel == logging.INFO
    assert args.n == 1

    args = __parse_args(["-vv", "2"])
    assert args.loglevel == logging.DEBUG
    assert args.n == 2

    # TODO: add_argumentのversionは試験困難
    # https://qiita.com/amedama/items/0cc2423ce53abf14ee54
    # args = __parse_args(["--version"])
    # assert args.version == "my_project 0.0.3"


def test_setup_logging(caplog):
    caplog.set_level(logging.DEBUG)

    __setup_logging(logging.DEBUG)

    assert caplog.messages[0] == 'set log level {}'.format(logging.DEBUG)


def test_main(capfd):
    main(["7"])

    out, err = capfd.readouterr()
    assert out == "The {}-th Fibonacci number is {}\n".format(7, 13)
    assert err == ""
