
# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from mindmeld import Application

app = Application(__name__)

__all__ = ['app']


@app.handle(default=True)
@app.handle(intent='unsupported')
def default(request, responder):
    """
    When the user asks an unrelated question, convey the lack of understanding for the requested
    information and prompt to return to food ordering.
    """
    replies = ["Sorry, not sure what you meant there. I can help you find a place the best version of yourself "
               "Try something like 'Tell me the best place where i can learn to overcome my fears'"]
    responder.reply(replies)

@app.handle(intent='greet')
def welcome(request, responder):
    """
    When the user starts a conversation, say hi and give some restaurant suggestions to explore.
    """
    try:
        # Get user's name from session information in a request to personalize the greeting.
        responder.slots['name'] = request.context['name']
        prefix = 'Hello, {name}. '
    except KeyError:
        prefix = 'Hello. '

    places = app.question_answerer.get(index='wellness')
    suggestions = ', '.join([r['name'] for r in places[0:3]])

    # Build up the final natural language response and reply to the user.
    responder.reply(prefix + 'Some nearby that may intrest you '
                    + suggestions)

@app.handle(intent='exit')
def say_goodbye(request, responder):
    responder.reply(['Bye', 'Goodbye', 'Have a nice day.','peace out'])

