#工厂方法模式
# 定义一个接口创建对象，但具体实例化哪个类由子类决定
# 抽象类creator包含factorymethod,
# concretecreator 提供实现creator类的factorymethod方法

from abc import  ABCMeta,abstractmethod
#接口product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass
#concreteproduct
class PersonalSection(Section):
    def describe(self):
        print('personal')

class AlbumSection(Section):
    def describe(self):
        print("album")

class PatentSection(Section):
    def describe(self):
        print("patent")

class PublicationSection(Section):
    def describe(self):
        print("publication")


#Creator
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    #factorymethod
    @abstractmethod
    def createProfile(self):
        pass
    def getSection(self):
        pass
    def addSection(self,section):
        self.sections.append(section)
#concretecreator
class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())

#客户端
if __name__ == "__main__":
    profile_type = input('which profile')
    profile = eval(profile_type.lower())()
    print('creating',type(profile).__name__)
    print("sections",profile.getSection())

