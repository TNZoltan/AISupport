from AI_model.Predict_Model import response


def concrete_command(request_object):
    if request_object['type'] == 'question':
        return response(request_object['question'], False)
    if request_object['type'] == 'greeting':
        return 'Function to be made'
    if request_object['type'] == 'starter':
        return 'Function to be made'
