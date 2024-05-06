from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."
    #
    # def add_arguments(self, parser):  # паратметр парсер, то есть позволит в нашу команду принимать значения
    #     parser.add_argument('id', type=int, help='User ID')
    #
    # def handle(self, *args, **kwargs):
    #     id = kwargs['id']   # так как указали в прошлой функции так
    #     user = User.objects.get(id=id)  # выдаст ошибку если нет такого id, поэтому лучше использовать метод filter
    #     self.stdout.write(f'{user}')

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
