from django.shortcuts import render
from django.http import HttpResponse
import requests

NODE = "152.228.155.120:8765"


def get_blocks(since, max_len=16):
    blocks = []
    while True:
        resp = requests.get(
            "http://{}/json/blocks?since={}&count={}".format(NODE, since + len(blocks), 16),
            headers={"X-ZEEKA-NETWORK-NAME": "debug"},
            timeout=2,
        ).json()['blocks']
        if len(resp) == 0 or len(blocks) >= max_len:
            break
        blocks.extend(resp)
    return blocks


def index(request):
    blocks = get_blocks(0, 16)
    return render(request, 'index.html', {'blocks': blocks})
