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
    return execute(conn, """SELECT max(p.salary) salary, s.seniority 
                        FROM "position" p 
                        INNER JOIN seniority s ON (p.seniority_id = s.id_seniority)
                        where s.seniority != 'unknown'
                        GROUP BY s.seniority 
                        ORDER BY 1 DESC""")


def companiesWithBetterSalaries(conn):
    return execute(conn, """SELECT max(p.salary) salary, c.name 
                        FROM "position" p
                        INNER JOIN company c ON (c.id_company = p.company_id) 
                        GROUP BY c.name
                        ORDER BY 1 DESC
                        limit 5""")


def companiesWithLowestSalaries(conn):
    return execute(conn, """SELECT max(p.salary) salary, c.name 
                            FROM "position" p
                            INNER JOIN company c ON (c.id_company = p.company_id) 
                            GROUP BY c.name
                            having max(p.salary) != 0
                            ORDER BY 1 ASC
                            limit 5""")


def mostRequestedSkills(conn):
    return execute(conn, """SELECT count(*), skill 
                            FROM skill s
                            INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
                            INNER JOIN "position" p  ON (p.id_position = ps.position_id)
                            GROUP BY skill 
                            ORDER BY 1 DESC""")


def bestPayedSkills(conn):
    return execute(conn, """SELECT avg(p.salary), count(p.salary) ,skill
                            FROM skill s
                            INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
                            INNER JOIN "position" p  ON (p.id_position = ps.position_id)
                            GROUP BY skill
                            having count(p.salary) >= 3
                            ORDER BY 1 DESC
                            """)


# def positionsBySkills(conn):
#     return execute(conn, """SELECT count(p.num_offers), skill
#                             FROM skill s
#                             INNER JOIN position_skill ps ON (s.id_skill = ps.skill_id)
#                             INNER JOIN "position" p  ON (p.id_position = ps.position_id)
#                             GROUP BY skill
#                             ORDER BY 1 DESC
#                             """)


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


def highestCulture(conn):
    """AVG salarial de acuerdo al culture score y al total_reviews"""
    return execute(conn, """SELECT max(salary), c.name, culture_score 
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name, culture_score
                            ORDER BY 3 DESC
                            """)


def lowestCulture(conn):
    """AVG salarial de acuerdo al culture score y al total_reviews"""
    return execute(conn, """SELECT max(salary), c.name, culture_score 
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name, culture_score
                            ORDER BY 3 ASC
                            """)


def highestWorkLifeBalance(conn):
    return execute(conn, """SELECT max(salary), c.name, c.work_life_balance  
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name, work_life_balance
                            ORDER BY 3 DESC
                            """)


def lowestWorkLifeBalance(conn):
    return execute(conn, """SELECT max(salary), c.name, c.work_life_balance  
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name, work_life_balance
                            ORDER BY 3 ASC
                            """)


def highestCareerOportunities(conn):
    return execute(conn, """SELECT max(salary), c.name, c.carrer_opportunities 
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name
                            ORDER BY 3 DESC
                            """)


def lowestCareerOportunities(conn):
    return execute(conn, """SELECT max(salary), c.name, c.carrer_opportunities 
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name
                            ORDER BY 3 ASC
                            """)


def highestReputation(conn):
    return execute(conn, """SELECT max(salary), c.name, c.avg_reputation  
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name
                            ORDER BY 3 DESC
                            """)


def lowestReputation(conn):
    return execute(conn, """SELECT max(salary), c.name, c.avg_reputation  
                            FROM "position" p 
                            INNER JOIN company c ON (p.company_id = c.id_company)
                            GROUP BY c.name
                            ORDER BY 3 ASC
                            """)


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
