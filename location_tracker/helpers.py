from flask_restful import abort

def try_to_convert(data, data_type):
    '''
    tries to convert the given data to the 
    given data type. If the conversion fails,
    aborts the request with code 400
    '''
    try:
        return data_type(data)
    except:
        abort(400)