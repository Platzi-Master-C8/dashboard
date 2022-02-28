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


def betterSalariesForModality(conn):
    return execute(conn, """select max(p.salary) salary, p.modality 
                        from "position" p 
                        group by p.modality
                        order by 1 desc""")


def betterSalariesForSeniority(conn):
    return execute(conn, """select max(p.salary) salary, s.seniority 
                        from "position" p 
                        inner join seniority s on (p.seniority_id = s.id_seniority)
                        group by s.seniority 
                        order by 1 desc""")


def companiesWithBetterSalaries(conn):
    return execute(conn, """select max(p.salary), c.name 
                        from "position" p
                        inner join company c on (c.id_company = p.company_id) 
                        group by c.name
                        order by 1 desc""")


def companiesWithLowestSalaries(conn):
    return execute(conn, """select max(p.salary), c.name 
                            from "position" p
                            inner join company c on (c.id_company = p.company_id) 
                            group by c.name
                            order by 1 asc""")


def mostRequestedSkills(conn):
    return execute(conn, """select count(*), skill 
                            from skill s
                            inner join position_skill ps on (s.id_skill = ps.skill_id)
                            inner join "position" p  on (p.id_position = ps.position_id)
                            group by skill 
                            order by 1 desc""")


def bestPayedSkills(conn):
    return execute(conn, """select max(p.salary), skill 
                            from skill s
                            inner join position_skill ps on (s.id_skill = ps.skill_id)
                            inner join "position" p  on (p.id_position = ps.position_id)
                            group by skill 
                            order by 1 desc
                            """)


def positionsBySkills(conn):
    return execute(conn, """select count(p.num_offers), skill 
                            from skill s
                            inner join position_skill ps on (s.id_skill = ps.skill_id)
                            inner join "position" p  on (p.id_position = ps.position_id)
                            group by skill 
                            order by 1 desc
                            """)


def mostRequestedPositions(conn):
    return execute(conn, """select count(*), pc.category 
                            from position_category pc 
                            inner join "position" p  on (p.position_category_id = pc.id_position_category)
                            group by pc.category  
                            order by 1 desc
                            """)


def betterOffers(conn):
    return execute(conn, """select p.modality, c.name, s.seniority, position_title, salary 
                            from "position" p 
                            inner join seniority s on (p.seniority_id = s.id_seniority)
                            inner join company c  on (p.company_id = c.id_company)
                            order by p.salary desc
                            """)


def highestCulture(conn):
    return execute(conn, """select max(salary), c.name, culture_score 
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name, culture_score
                            order by 3 desc
                            """)


def lowestCulture(conn):
    return execute(conn, """select max(salary), c.name, culture_score 
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name, culture_score
                            order by 3 asc
                            """)


def highestWorkLifeBalance(conn):
    return execute(conn, """select max(salary), c.name, c.work_life_balance  
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name, work_life_balance
                            order by 3 desc
                            """)


def lowestWorkLifeBalance(conn):
    return execute(conn, """select max(salary), c.name, c.work_life_balance  
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name, work_life_balance
                            order by 3 asc
                            """)


def highestCareerOportunities(conn):
    return execute(conn, """select max(salary), c.name, c.carrer_opportunities 
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 desc
                            """)


def lowestCareerOportunities(conn):
    return execute(conn, """select max(salary), c.name, c.carrer_opportunities 
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 asc
                            """)


def highestCeoScore(conn):
    return execute(conn, """select max(salary), c.name, c.ceo_score  
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 desc
                            """)


def lowestCeoScore(conn):
    return execute(conn, """select max(salary), c.name, c.ceo_score 
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 asc
                            """)


def highestReputation(conn):
    return execute(conn, """select max(salary), c.name, c.avg_reputation  
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 desc
                            """)


def lowestReputation(conn):
    return execute(conn, """select max(salary), c.name, c.avg_reputation  
                            from "position" p 
                            inner join company c on (p.company_id = c.id_company)
                            group by c.name
                            order by 3 asc
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
