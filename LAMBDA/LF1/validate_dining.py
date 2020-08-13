import helper_function
import dateutil.parser
import datetime

# Validate input data
def validate_dining(slots):

    dining_date = helper_function.try_ex(lambda: slots['diningDate'])
    dining_time = helper_function.try_ex(lambda: slots['diningTime'])
    num_people = helper_function.try_ex(lambda: slots['numPeople'])
    phone_num = helper_function.try_ex(lambda: slots['phoneNum'])
    location = helper_function.try_ex(lambda:slots["location"])
    cuisine = helper_function.try_ex(lambda:slots["cuisine"])
    
    # Validate Cuisine
    cuisines = ['italian', 'chinese', 'indian', 'american', 'mexican', 'spanish', 'greek', 'latin', 'Persian']
    if cuisine.lower() not in cuisines:
        return helper_function.build_validation_result(
            False,
            'cuisine',
            'Sorry the provided cuisine is not available. Can you try again?'
        )

    # Validate location
    place = ["Allen Road","Scarborough","Bayview Avenue","Bellamy","Beverley ","Brimley","","toronto","northyork","warden","victoria park","Don Valley Parkway","Avenue Road","Canlish","Guildwood Parkway","Birchmount","Town Haven Place","Danforth","Canlish","Guildwood","Rockwood Drive","Lawrence Avenue","Whitecap Boulevard","Eglinton","Valleys Drive","Pharmacy Avenue","Kingston Road","Dundalk Drive","St Clair Avenue East"]
    if location.lower() not in place:
        return helper_function.build_validation_result(
            False,
            'location',
            'Sorry please provide a place in Toronto. Can you try again?'
        )

    # Validate party size
    if num_people and not (0 < int(num_people) < 51):
        return helper_function.build_validation_result(
            False,
            'numPeople',
            'Your party needs to be between 1 and 50 people. Can you try again?'
        )

    # Validate the date first
    if dining_date:
        intended_date = dateutil.parser.parse(dining_date)
        grace_period = datetime.datetime.today() - datetime.timedelta(days=1)
        if intended_date < grace_period:
            return helper_function.build_validation_result(
                False,
                'diningDate',
                'You cannot go back in time!'
            )

    # Validate the time
    if dining_date and dining_time:
        intended_datetime = dateutil.parser.parse(dining_date + ' ' + dining_time)
        if intended_datetime < datetime.datetime.now():
            return helper_function.build_validation_result(
                False,
                'diningTime',
                'You cannot go back in date!'
            )

    # Validate the time format
    if dining_time:
        if type(dining_time)!=str:
            return helper_function.build_validation_result(
                False,
                'diningTime',
                'Please enter time in format!'
            )
            

    if phone_num and (phone_num.startswith('+1') is False or len(phone_num) != 12):
        return helper_function.build_validation_result(
                False,
                'phoneNum',
                'Phone number must follow format +1XXXXXXXXXX'
            )

    return {'isValid': True}

