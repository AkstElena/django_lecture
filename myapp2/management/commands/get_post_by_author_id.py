from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)  # здесь будет объект со всеми постами автора query set
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)  # query set можно перебирать как список
    #         self.stdout.write(f'{intro}{text}')

    # def handle(self, *args, **kwargs):  # если не нужно выводить автора, сразу обращаемся к постам
    #     pk = kwargs.get('pk')
    #     posts = Post.objects.filter(author__pk=pk)
    #     intro = f'All posts\n'
    #     text = '\n'.join(post.content for post in posts)
    #     self.stdout.write(f'{intro}{text}')

    def handle(self, *args, **kwargs):  # при использовании пользовательских методов
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')