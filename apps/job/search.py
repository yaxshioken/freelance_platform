from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        search_fields = []

        if request.query_params.get("city_only"):
            search_fields.append("city")
        if request.query_params.get("country_only"):
            search_fields.append("country")
        return search_fields or super().get_search_fields(view, request)
