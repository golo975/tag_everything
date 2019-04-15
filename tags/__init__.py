
import os

class TagNode(object):
    def __init__(self, name, parent):
        self.__name = name
        self.__parent = parent

    def get_parent(self):
        return self.__parent

    def get_name(self):
        return self.__name


class Tag(TagNode):

    def __repr__(self) -> str:
        """
        1. 文档注释必须用双引号？？？为什么？？？
        2. -> 这是什么语法？？
        """
        return self.get_name()

    def __str__(self) -> str:
        return self.get_name()

    def __eq__(self, o: object) -> bool:
        """
        怎样重新equals方法？
        重写之后会影响哪些行为？
        """
        return isinstance(o, Tag) and super().__eq__(o) and super().get_name().__eq__(o.get_name())

    def __hash__(self) -> int:
        return super().__hash__()


tag_default = Tag("default", None)


class Entity(object):
    def __init__(self):
        self.__tags = {tag_default}

    def add_tag(self, tag):
        self.__tags.add(tag)
        if len(self.__tags) >= 2 and tag_default in self.__tags:
            self.__tags.remove(tag_default)

    def rm_tag(self, tag):
        if tag in self.__tags:
            self.__tags.remove(tag)
            if not self.__tags:
                self.add_tag(tag_default)

    def get_tags(self):
        return self.__tags

    def __repr__(self) -> str:
        return str(self.__tags)


class EntityTagRelation(object):
    pass


# tag_test = Tag("default", None)
# entity = Entity()
# print(entity.get_tags())
#
# entity.add_tag(tag_test)
# print(entity.get_tags())

entity_list = []
for root, dirs, files in os.walk('D:/movie'):
    for file in files:
        file_entity = Entity()
        file_entity.add_tag(Tag(root, None))
        entity_list.append(file_entity)

print(entity_list)
