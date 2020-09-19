from rest_framework import pagination


class CFEAPIPagination(pagination.PageNumberPagination):
	page_size = 5
	max_limit = 20
	default_limit = 10
	limit_query_param = 'limit'