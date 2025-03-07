from simple_blogger import CommonBlogger
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import datetime
from datetime import timedelta

class Project(CommonBlogger):
    def _example_task_creator(self):
        return [
            {
                "name": "Name",
                "postion": "Position",
                "company": "Company",
            }
        ]

    def _get_category_folder(self, task):
        return f"{task['company']}"
                    
    def _get_topic_folder(self, task):
        return f"{task['name']}"

    def _system_prompt(self, task):
        return "Ты - блогер с 1000000 миллионном подписчиков"

    def _task_converter(self, idea):
        return { 
                    "name": idea['name'],
                    "position": idea['position'],
                    "company": idea['company'],
                    "topic_prompt": f"Расскажи интересный факт про '{idea['name']}' '{idea['position']}' из компании '{idea['company']}', используй не более {self.topic_word_limit} слов, используй смайлики",
                    "topic_image": f"Нарисуй рисунок, вдохновлённый '{idea['name']}' '{idea['position']}' из компании '{idea['company']}'",
                }

    def __init__(self, **kwargs):
        super().__init__(
            review_chat_id=-1002374309134,
            production_chat_id='@verge_of_breakdown',
            first_post_date=datetime(2025, 3, 9),
            days_between_posts=timedelta(7),
            text_generator=OpenAITextGenerator(),
            topic_word_limit=100,
            **kwargs
        )