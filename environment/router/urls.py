from enum import Enum

# API end points enum.
class URLs(str, Enum):
    base_v1 = "/api/v1/ecfastmvc"
    user = f'{base_v1}/user'
    