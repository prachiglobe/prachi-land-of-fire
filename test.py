class TestModel(models.Model):
  name = models.charfield(max_lenghth = 100)


class Meta:
  db_table = " test_model"
