from dashboard.layouts import popular_skills, start, sample_size, salaries, salaries_table, salaries_by_company, \
    popular_skills, salary_popularity, remote_salary

navigation = {
    "start": (None, "sample_size", start.page),
    "sample_size": ("start", "salaries_by_company", sample_size.page),
    "salaries_by_company": ("sample_size", "salaries", salaries_by_company.page),
    "salaries": ("salaries_by_company", "salaries_table", salaries.page),
    "salaries_table": ("salaries", 'requested_skills', salaries_table.page),
    "requested_skills": ("salaries_table","salary_popularity",popular_skills.page),
    "salary_popularity": ("requested_skills","salary_remote",salary_popularity.page),
    "salary_remote": ("salary_popularity",None,remote_salary.page)
}
