# -*- coding: utf-8 -*-

import config


def get_last(a):
    for x in a:
        if x.message is None:
            continue
        else:
            config.messages += [(x.message.text)]

def get_last_id(a):
    for x in a:
        if x.message is None:
            continue
        else:
            config.messages_id += [(x.message.message_id)]



