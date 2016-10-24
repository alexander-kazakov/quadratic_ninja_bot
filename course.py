# -*- coding: utf-8 -*-

import emoji

class BotResponse:
    def __init__(self, text, reply_options):
        self.text = text
        self.reply_options = reply_options


class ContentText:
    def __init__(self,name,options,text):
        self.name = name
        self.options = options
        self.text = text

    def show(self):
        return BotResponse(emoji.emojize(self.text, use_aliases=True), self.options.keys())

    def next_step(self, input):
        if input in self.options:
            return self.options[input]
        else:
            return self.name



def build_course():

    #TODO: Create a course validator checking all links

    course = {}
    steps = list()

    steps.append(ContentText('intro',       {'Let''s go!': 'definition',
                                             'Why would I want to learn it?': 'why_learn1'},    'Hey, my name is Mike and I will teach you to solve quadratic equations like a ninja! ⚔'))


    steps.append(ContentText('why_learn1',   {'For example?': 'why_learn2'},    'Many see quadratic equations as theoretical stuff that is not relevant for everyday life.\n\nWhile the direct practical use can be little, they are actually a super-cool step on your way to learn the powerful principles of math.'))

    steps.append(ContentText('why_learn2',   {'All right, so what is quadratic equation actually?': 'definition'},
"""They are likely the first kind of math problems you encounter that:
1. Can have multiple solutions or even none!
2. Have a simple algorithm to find a solution that you can apply each time you notice them
3. Are a great illustration how a slight shift of view on a problem can make it way easier to solve (more on that later)
4. Let you feel like a NINJA solving them! ⚔"""))


    steps.append(ContentText('definition',  {'Understood!': 'pretest'},         'In elementary algebra, a quadratic equation (from the Latin quadratus for "square") is any equation having the form ax^2+bx+c=0 where x represents an unknown, and a, b, and c represent known numbers such that a is not equal to 0'))

    steps.append(ContentText('pretest',     {'Yes, gotcha!': 'correct',
                                             'Nope, this is not it': 'wrong'},  'Is this a quadratic equation x^2 = 4?'))

    steps.append(ContentText('correct',     {'Continue': 'finished'},           'Well done, padawan!'))
    steps.append(ContentText('wrong',       {'Aha, now I see!': 'finished'},    'INCORRECT. Ha, this was a tricky one! You will become a ninja master through the path of learning through mistakes!\n\nThis was a quadratic equation. Try to put a=1, b=0 and c=0 in the definition I told you above. Do you see it now?'))

    steps.append(ContentText('finished',    {'Got it!': 'finished'},            'You are done for now! Nothing else here :-) You can restart by typing /start'))

    for step in steps:
        course[step.name] = step

    return course
