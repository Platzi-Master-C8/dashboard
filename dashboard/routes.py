from dashboard.layouts import (
    start,
    sample_size,
    salaries,
    salaries_table,
    salaries_by_company,
    reviews,
    companies_reputation,
    salary_remote,
)

navigation = {
    "start": (None, "sample_size", start.page),
    "sample_size": ("start", "salaries_by_company", sample_size.page),
    "salaries_by_company": ("sample_size", "salaries", salaries_by_company.page),
    "salaries": ("salaries_by_company", "salaries_table", salaries.page),
    "salaries_table": ("salaries", "reputation", salaries_table.page),
    "reputation": ("salaries_table", "reviews", companies_reputation.page),
    "reviews": ("reputation", 'remote', reviews.page),
    "remote": ("reviews", None, salary_remote.page)
}
