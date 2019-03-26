from django.db import models
from django.utils import timezone

class Post(models.Model): #models: Post가 장고 모델임을 의미. 이 코드 때문에 장고는 Post가 DB에 저장되어야 함을 알게 됨.
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #다른 모델에 대한 링크
  title = models.CharField(max_length=200) #글자 수가 제한된 텍스트를 정의할 때
  text = models.TextField() #글자 수에 제한이 없는 텍스트
  created_date = models.DateTimeField(default=timezone.now) #날짜, 시간
  published_date = models.DateTimeField(blank=True, null=True)

  # def: 메서드 정의 키워드
  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title