from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    # change query in url
    limit_query_param= 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 5