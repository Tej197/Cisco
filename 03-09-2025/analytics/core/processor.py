from.validator import validate_data
def process_data(data):
    if(not validate_data(data)):
        return f"processed: {data}"
    else:
         return "invalid data"