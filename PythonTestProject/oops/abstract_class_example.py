from abc import ABC, abstractmethod


class AbstractRecipe(ABC):
    def execute(self):
        self.get_ready()
        self.prepare_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def prepare_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Recipe1(AbstractRecipe):

    def get_ready(self):
        print('Get ready for cooking')

    def prepare_dish(self):
        print('Cook dish')

    def cleanup(self):
        print('clean up vessels')


recipe1 = Recipe1()
recipe1.execute()
