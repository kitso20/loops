import re
def uuid_validator(list_of_uuids):

    res = {"valid_uuid": [], "invalid_uuid": []}

    for id in list_of_uuids:
        if re.search(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):
            res['valid_uuid'].append(id)
        else:
            res["invalid_uuid"].append(id)
    
    return res


print(uuid_validator([
            '123e4567-e89b-12d3-a456-426614174000',
            '123e4567-e89b-12d3-a456-42661417400Z',
            '550e8400-e29b-41d4-a716-446655440000',
            '550e8400-e29b-41d4-a716-44665544000G'
        ])
)
