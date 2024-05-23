from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    # How many items on page
    page_size= 5 
    # Query name of page 
    page_query_param = 'mypage'
    # user define how many records he want on one page
    page_size_query_param = 'records'
    # restrict page size
    max_page_size = 5

    #last page string change
    last_page_strings='end'