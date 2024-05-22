from rest_framework.throttling import  UserRateThrottle


class UzainRateThrottle(UserRateThrottle):
    scope = 'uzain'