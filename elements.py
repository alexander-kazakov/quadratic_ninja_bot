# -*- coding: utf-8 -*-

import emoji

class BotResponse:
    def __init__(self, text, reply_options):
        self.text = text
        self.reply_options = reply_options


class ContentText:
    def __init__(self,name,options,text):
        self.name = name
        for key in options.keys():
            options[unicode(key, "utf-8")] = options[key]
            del options[key]
        self.options = options
        self.text = text

    def show(self):
        return BotResponse(emoji.emojize(self.text, use_aliases=True), self.options.keys())

    def next_item(self, input):
        if input in self.options:
            return self.options[input]
        else:
            return self.name