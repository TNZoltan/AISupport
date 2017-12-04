#from AI_model.Predict_Model import response


def concrete_command(request_object):
    if request_object['type'] == 'question':
        return 'Did not manage to call yet'
    if request_object['type'] == 'greeting':
        return 'Function to be made'
    if request_object['type'] == 'starter':
        return 'Function to be made'
