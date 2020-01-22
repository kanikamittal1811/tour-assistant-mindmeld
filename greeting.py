from .root import app

#TODO: Fix the X,Y and Z in greet function text Line 7

@app.handle(intent='greet')
def greet(request, responder):
    try:
        # Get user's name from session information in a request to personalize the greeting.
        responder.slots['name'] = request.context['name']
        prefix = 'Hello, {name}. '
    except KeyError:
        prefix = 'Hello. '
    responder.reply('Hi, I am your tour assistant. I can help you to do X, Y and Z.')


@app.handle(intent='exit')
def exit(request, responder):
    responder.reply(['Bye!', 'Goodbye', 'Have a nice day!','Peace out'])
