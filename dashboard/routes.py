from dashboard.layouts import start, sample_size, salaries, salaries_table, salaries_by_company

navigation = {
    "start": (None, "sample_size", start.page),
    "sample_size": ("start", "salaries_by_company", sample_size.page),
    "salaries_by_company": ("sample_size", "salaries", salaries_by_company.page),
    "salaries": ("salaries_by_company", "salaries_table", salaries.page),
    "salaries_table": ("salaries", None, salaries_table.page)
}
