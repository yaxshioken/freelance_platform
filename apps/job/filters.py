from rest_framework import filters

from apps.job.models import JobAnnounce


class JobFilter(filters.BaseFilterBackend):
    """
    Filter that only allows level, technologies, price_measure, payment_verified, job_type, profession,
    to see their own objects.
    """
