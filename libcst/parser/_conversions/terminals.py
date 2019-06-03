# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Any

from libcst.parser._types.config import ParserConfig
from libcst.parser._types.token import Token
from libcst.parser._whitespace_parser import (
    parse_empty_lines,
    parse_trailing_whitespace,
)


def convert_NAME(config: ParserConfig, token: Token) -> Any:
    return token


def convert_NUMBER(config: ParserConfig, token: Token) -> Any:
    return token


def convert_STRING(config: ParserConfig, token: Token) -> Any:
    return token


def convert_OP(config: ParserConfig, token: Token) -> Any:
    return token


def convert_NEWLINE(config: ParserConfig, token: Token) -> Any:
    # A NEWLINE token is only emitted for semantic newlines, which means that this
    # corresponds to a TrailingWhitespace, since that's the only semantic
    # newline-containing node.

    # N.B. Because this token is whitespace, and because the whitespace parser doesn't
    # try to prevent overflows, `token.whitespace_before` will end up overflowing into
    # the value of this newline token, so `parse_trailing_whitespace` will include
    # token.string's value. This is expected and desired behavior.
    return parse_trailing_whitespace(config, token.whitespace_before)


def convert_INDENT(config: ParserConfig, token: Token) -> Any:
    return token


def convert_DEDENT(config: ParserConfig, token: Token) -> Any:
    return token


def convert_ENDMARKER(config: ParserConfig, token: Token) -> Any:
    return parse_empty_lines(config, token.whitespace_before)


def convert_FSTRING_START(config: ParserConfig, token: Token) -> Any:
    return token


def convert_FSTRING_END(config: ParserConfig, token: Token) -> Any:
    return token


def convert_FSTRING_STRING(config: ParserConfig, token: Token) -> Any:
    return token