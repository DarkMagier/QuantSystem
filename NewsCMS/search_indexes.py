import datetime
from haystack import indexes
from NewsCMS.models import lastNews



class lastNewsIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，lastNews，lastNewsIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    author = indexes.CharField(model_attr='user')  # 创建一个author字段

    time = indexes.DateTimeField(model_attr='time')  # 创建一个pub_date字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return lastNews

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(time=datetime.datetime.now())
