from .root import app

@app.handle(intent='unknown')
def default(request, responder):
    """
    When the user asks an unrelated question, convey the lack of understanding for the requested
    information and prompt to return to
    """
    replies = ["Sorry, not sure what you meant there. I can help you find the place that brings out the best version of yourself "
               "Try something like 'Tell me the best place where i can learn to overcome my fears'"]
    responder.reply(replies)
