from .root import app

#TODO: Optimize the qa class searching

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

@app.handle(intent="find_essentials")
def find_essentials(request, responder):
    #See is user already taked about the location
    selected_center_name = request.frame.get('center_name')

    #TODO: Write the logic for location as well

    if selected_location:
        #If a location has been selected, store the visiting location in chatbot
        responder.slots['center_name'] = selected_center_name

        #TODO: Write the backend code to find out weather of the location

        latitide = None
        longitude = None
        weather = None
        #Get the coordinates
        for c in app.question_answerer.get('centers'):
            if c['name']==selected_center_name:
                latitude = c['location'][1]['latitide']
                longitude = c['location'][1]['longitude']

                #TODO: Write the backend code to find out weather of the location

        if latitude!=None and longitude!=None:
            #For now, I am assuming that weather is cold and taking general items into account

            #TODO: We can ask for duration if we want to specify the quantity of the essentials
            replies = ['It is recommended to take warm clothes, bed sheet and few walnuts.']
        else:
            replies = [f'I am not able to find the location of {selected_center_name}. Could you please specify it?']

    else:
        #If no location has been specified, then prompt the user to tell location
        replies = ["I'm not sure. You haven't told me where you want to go!"]

    responder.reply(replies)


@app.handle(intent="list_reviews")
def list_reviews(request, responder):
    #See is user already taked about the location
    selected_center_name = request.frame.get('center_name')

    if selected_location:
        #If a location has been selected, store the visiting location in chatbot
        responder.slots['center_name'] = selected_center_name

        reviews = None
        for c in app.question_answerer.get('centers'):
            if c['name']==selected_center_name:
                reviews = c['reviews']

        if reviews:
            replies = "Here are some few reviews:\n"
            for i in range(len(reviews)):
                replies += f"{i}. {reviews[i]}\n"

            #TODO: Give them overall score of reviews through text classification models
            replies = reviews
        else:
            #TODO: We can write logic to verify with its opening date and give proper reply back
            replies = "The center has been started recently. There are no useful reviews yet."

    else:
        #If no location has been specified, then prompt the user to tell location
        replies = ["I'm not sure. You haven't told me what to review"]

    responder.reply(replies)
