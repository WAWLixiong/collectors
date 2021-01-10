#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 上午 09:48:21
# @Author  : zzlion
# @File    : test_jp.py
# @Reference:

import jmespath

data = {
    "a": "foo",
    "b": {"d": {"e": "bob"}},
    "c": "baz",
    "f": ['a', 'b', 'c', 'd', 'e', 'f'],
    "g": [
        {"h": [0, [1, 2]]},
        {"h": [3, 4]},
    ],
    "people": [
        {"first": "James", "last": "d"},
        {"first": "Jacob", "last": "e"},
        {"first": "Jayden", "last": "f"},
        {"missing": "different"}
    ],
    "foo": {"bar": "baz"},
    "cal": 1,
    "ops": {
        "functionA": {"numArgs": 2},
        "functionB": {"numArgs": 3},
        "functionC": {"variadic": True}
    },
    "flatten": [
        {
            "instances": [
                {"state": "running"},
                {"state": "stopped"}
            ]
        },
        {
            "instances": [
                {"state": "terminated"},
                {"state": "running"}
            ]
        }
    ],
    "onece": [
        [0, 1],
        2,
        [3],
        4,
        [5, [6, 7]]
    ],
    "machines": [
        {"name": "a", "state": "running"},
        {"name": "b", "state": "stopped"},
        {"name": "b", "state": "running"}
    ]
}

patt = jmespath.compile("machines[?state=='running'].name")
# patt = jmespath.compile("ops.*")
ret = patt.search(data)
print(ret)
