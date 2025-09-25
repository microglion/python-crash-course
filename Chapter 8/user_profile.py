def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
user_profile2 = build_profile('rick', 'deckard', field='blade runner', location='seattle')
print(user_profile)
print(user_profile2)