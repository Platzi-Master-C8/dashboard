from dashboard.components import infographic, layout
from dashboard.datasource import engine
from dashboard.data import allReviews, datasets, allDescriptions, allSkills


def _build_layout():
    _layoutStructure = ['reviews job_descriptions skills']

    with engine.connect() as conn:
        return layout.grid([
            layout.area(layout.titleAndContent('Companies Reviews',
                                               infographic.wordcloud(
                                                   *datasets(['content_type'], allReviews(conn)),
                                                   shape='fa-star',
                                                   size=400,
                                                   output_name='assets/reviews_content_type.png',
                                               )), 'reviews'),
            layout.area(layout.titleAndContent('Job Descriptions',
                                               infographic.wordcloud(
                                                   *datasets(['description'], allDescriptions(conn)),
                                                   shape='fa-window-maximize',
                                                   size=400,
                                                   output_name='assets/reviews_title.png',
                                               )), 'job_descriptions'),
            layout.area(layout.titleAndContent('Skills',
                                               infographic.wordcloud(
                                                   *datasets(["skill"], allSkills(conn)),
                                                   shape="fa-robot",
                                                   size=400,
                                                   output_name="assets/all_skills_cloud.png",
                                               )), 'skills'),
        ], 3, 1, _layoutStructure)


page = layout.titleAndContent('Most common words', _build_layout())
