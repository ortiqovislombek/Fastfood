import re

def check_phone(phone: str) -> bool:
    """
    O'zbekiston telefon raqamini tekshiradi.
    To'g'ri format: +998XXXXXXXXX (13 ta belgi, jami 9 ta raqam)
    """
    pattern = r'^\+998\d{9}$'
    return bool(re.match(pattern, phone))

def check_uzb_location(lat: float, lon: float) -> bool:
    """
    O'zbekiston hududida joylashganini tekshiradi.
    lat - latitude (kenglik)
    lon - longitude (uzunlik)
    """
    return 37.0 <= lat <= 46.0 and 55.0 <= lon <= 73.0

