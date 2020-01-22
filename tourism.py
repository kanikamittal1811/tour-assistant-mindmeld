from .root import app

#Here we have to make changes for toursism intents

@app.dialogue_flow(domain='tour_info',intent='info') #can add domain in this
def send_center_info(request, responder):
    active_center = None
    center_entity = next((e for e in request.entities if e['type'] == 'center_name'), None)
    if center_entity:
        try:
            center = app.question_answerer.get(index='wellness', id=center_entity['value']['id'])
        except TypeError:
            center = app.question_answerer.get(index='wellness', center_name=center_entity['text'])
        try:
            active_center = center[0]
            responder.frame['center_name'] = active_center
        except IndexError:
            # No active store... continue
            pass
    elif 'center_name' in request.frame:
        active_center = request.frame['center_name'] #center_name 

    if active_center:
        responder.slots['center_name'] = active_center['center_name']
        responder.slots['info'] = active_center['description']
        return

    responder.frame['count'] = responder.frame.get('count', 0) + 1

    if responder.frame['count'] <= 3:
        responder.reply('Which center would you like to know about?')
        responder.listen()
    else:
        responder.reply('Sorry I cannot help you. Please try again.')
        responder.exit_flow()

@send_center_info.handle(default=True)
def default_handler(request, responder):
    responder.frame['count'] += 1
    if responder.frame['count'] <= 3:
        responder.reply('Sorry, I did not get you. Which center would you like to know about?')
        responder.listen()
    else:
        responder.reply('Sorry I cannot help you. Please try again.')
        responder.exit_flow()


@send_center_info.handle(intent='exit', exit_flow=True)
def exit_handler(request, responder):
    responder.reply(['Bye', 'Goodbye', 'Have a nice day.'])


@send_center_info.handle(intent='info')
def send_center_info_in_flow_handler(request, responder):
    send_center_info(request, responder)