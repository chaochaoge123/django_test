from haystack import indexes

from test_one.models.user import User_info, Item

class User_infoIndex(indexes .SearchIndex ,indexes .Indexable ):
    #document=True，代表haystack和搜索引擎将使用此字段的内容作为索引进行检索
    text = indexes.CharField(document=True,use_template=True)
    name = indexes.CharField(model_attr='name')
    mobile = indexes.CharField (model_attr='mobile')
    remarks = indexes .CharField(model_attr='remarks')

    def get_model(self):
        return User_info
    def index_queryset(self, using=None):
        # 过滤出写入es索引库的数据
        return self.get_model() .objects .filter(remarks="庐州月")


class ItemIndex(indexes .SearchIndex, indexes .Indexable):
    text = indexes.CharField(document=True, use_template=True)
    case_no = indexes.CharField(model_attr='case_no')
    item_no = indexes.CharField(model_attr='item_no')

    def get_model(self):
        return Item
    def index_queryset(self, using=None):
        return self.get_model().objects.all()



# python3 manage.py rebuild_index  生成索引库
# https://blog.csdn.net/wzyaiwl/article/details/89763859