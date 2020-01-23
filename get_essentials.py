from .root import app

#TODO: Optimize the qa class searching
@app.handle(intent="get_essentials")
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
