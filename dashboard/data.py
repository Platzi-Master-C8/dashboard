from dashboard.datasource import execute, scalar
from sqlalchemy.engine import CursorResult


def numberOfCompanies(conn) -> int:
    return scalar(conn, """
    SELECT count(*) FROM company
    """)


def numberOfPositions(conn) -> int:
    return scalar(conn, """
    SELECT count(*) FROM "position"
    """)


def numberOfSkills(conn) -> int:
    return scalar(conn, """
    SELECT count(*) FROM skill
    """)


def numberOfReviews(conn):
    return scalar(conn, """
    SELECT count(*) FROM user_review
    """)


def betterSalariesForModality(conn):
    return execute(conn, """SELECT max(p.salary) salary, p.modality 
                        FROM "position" p 
                        GROUP BY p.modality
                        ORDER BY 1 DESC""")


def betterSalariesForSeniority(conn):
    return execute(conn, """SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY position.salary) as median, s.seniority
                            FROM position
                            INNER JOIN seniority s ON (position.seniority_id = s.id_seniority)
                            WHERE s.seniority != 'unknown'
                              AND position.salary IS NOT NULL
                            GROUP BY s.seniority
                            ORDER BY 1 DESC""")


def companiesWithBetterSalaries(conn):
    return execute(conn, """SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY position.salary) as salary, company.name
                            FROM position
                            INNER JOIN company ON (company.id_company = position.company_id)
                            WHERE salary IS NOT NULL
                            GROUP BY company.name, position.salary
                            ORDER BY salary DESC
                            limit 5""")


def companiesWithLowestSalaries(conn):
    return execute(conn, """SELECT max(p.salary) AS salary, c.name 
                            FROM "position" p
                            INNER JOIN company c ON (c.id_company = p.company_id) 
                            GROUP BY c.name
                            having max(p.salary) != 0
                            ORDER BY salary
                            limit 5""")


def mostRequestedSkills(conn):
    return execute(conn, """SELECT count(*) count, skill 
                            FROM skill s
                            INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
                            INNER JOIN "position" p  ON (p.id_position = ps.position_id)
                            GROUP BY skill 
                            ORDER BY count DESC
                            LIMIT 10""")
    
    
def lessRequestedSkills(conn):
    return execute(conn, """SELECT count(*) count , skill 
                            FROM skill s
                            INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
                            INNER JOIN "position" p  ON (p.id_position = ps.position_id)
                            GROUP BY skill 
                            ORDER BY count ASC
                            LIMIT 10""")


def bestPayedSkills(conn):
    return execute(conn, """SELECT avg(p.salary) salary, count(p.salary) offers, skill
                            FROM skill s
                            INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
                            INNER JOIN "position" p  ON (p.id_position = ps.position_id)
                            GROUP BY skill
                            having count(p.salary) >= 3
                            ORDER BY 1 DESC
                            """)


def mostRequestedPositions(conn):
    return execute(conn, """SELECT count(*), pc.category 
                            FROM position_category pc 
                            INNER JOIN "position" p  ON (p.position_category_id = pc.id_position_category)
                            where pc.category not in ('UNKNOWN', 'DEVELOPER')
                            GROUP BY pc.category  
                            ORDER BY 1 DESC
                            """)


def betterOffers(conn):
    return execute(conn, """SELECT p.modality, c.name, s.seniority, position_title, salary 
                            FROM "position" p 
                            INNER JOIN seniority s ON (p.seniority_id = s.id_seniority)
                            INNER JOIN company c  ON (p.company_id = c.id_company)
                            ORDER BY p.salary DESC
                            """)


def companiesReputation():
    return """SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY position.salary) median,
                    name,
                    culture_score,
                    work_life_balance_score,
                    career_opportunities_score,
                    perks_score
                    FROM position
                    INNER JOIN company on (position.company_id = company.id_company)
                    WHERE total_ratings > 10 AND salary > 0
                    GROUP BY name,
                            culture_score,
                            work_life_balance_score,
                            career_opportunities_score,
                            perks_score
                    ORDER BY culture_score DESC
                    LIMIT 5
            """


def companiesBestAvgReputation(conn):
    return execute(conn, """SELECT name, avg_reputation
                            FROM company
                            WHERE total_ratings > 100
                            ORDER BY avg_reputation DESC;
                        """)


def allSkills(conn):
    return execute(conn, """select skill
                            from skill s
                            inner join position_skill ps on (s.id_skill = ps.skill_id)
                            inner join "position" p  on (p.id_position = ps.position_id)
                            """)


def allReviews(conn):
    return execute(conn, """SELECT content_type FROM user_review""")


def allDescriptions(conn):
    return execute(conn, """SELECT description FROM position WHERE NOT description LIKE '%Time zone%'""")


def remotePositions():
    return """SELECT remote, count(*) from position GROUP by remote"""


def datasets(columns: list, data: CursorResult):
    data_sets = [[] for column in columns]
    size = len(columns)
    for row in data.columns(*columns):
        for index in range(0, size):
            data_sets[index].append(row[index])
    return tuple(data_sets)


def table(columns: dict, data: CursorResult):
    column_keys = [column for column in columns.keys()]
    rows = []
    size = len(columns)
    for row in data.columns(*column_keys):
        new_row = {}
        for index in range(0, size):
            new_row[column_keys[index]] = row[index]
        rows.append(new_row)
    return rows, columns
