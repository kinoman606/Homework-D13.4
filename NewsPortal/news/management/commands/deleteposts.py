from django.core.management import BaseCommand, CommandError

from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет публикации определенной категории'
    missing_args_message = 'Категория удаляемых сообщений указана не корректно'

    def add_arguments(self, parser):
        parser.add_argument("category", type=str)

    def handle(self, *args, **options):
        message = input(f'Вы хотите удалить все сообщения в категории {options["category"]}? yes/no:  ')

        if message == 'yes':
            try:
                category = Category.objects.get(name_cat=options['category'])
                posts = Post.objects.filter(post_category=category)
                posts.delete()
                self.stdout.write(self.style.SUCCESS(f'Все публикации из категории {category.name_cat} успешно удалены!'))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Категория {category.name_cat} не найдена'))
        else:
            self.stdout.write(self.style.ERROR('Удаление отменено!'))

            


