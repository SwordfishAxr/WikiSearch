# SPDX-License-Identifier: 0BSD
# Copyright 2026 Neltharion01

import httpx;
from httpx import RequestError;

from sbercode.colors import *;

WIKI_SEARCH_FUNCTION = {
    "name": "wiki_search",
    "description": "Выполнить поиск по статьям English Wikipedia",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Запрос для поиска"
            },
            "n": {
                "type": "integer",
                "description": "Количество результатов в выдаче",
                "default": 10
            },
        },
        "required": ["query"]
    },
    "few_shot_examples": [
        {
            "request": "Получить список статей про кошек",
            "params": {
                "query": "cat",
            }
        }
    ],
    "return_parameters": {
        "type": "object",
        "properties": {
            "result": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "src": {
                            "type": "string",
                            "description": "Источник результата. B для BM25 и V для векторного поиска"
                        },
                        "title": {
                            "type": "string",
                            "description": "Заголовок статьи"
                        },
                        "snippet": {
                            "type": "string",
                            "description": "Короткий отрывок начала статьи"
                        }
                    }
                }
            }
        }
    }
};

class WikiSearch:
    desc = WIKI_SEARCH_FUNCTION;
    def run(self, args):
        return httpx.post("https://drakohost.su/miniwiki", json=args).json();

    def print_args(self, args):
        print(f"  {YELLOW}+ Wiki search {WHITE}{args['query']}{RESET}");
