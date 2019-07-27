from django.apps import AppConfig


class ThesaurusConfig(AppConfig):
    name = 'thesaurus'
    def ready(self):
        from thesaurus.models import WordCloudThread
        thread = WordCloudThread()
        thread.start()