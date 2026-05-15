import pytest
from django.contrib.auth.models import User
from blog.models import Post

@pytest.mark.django_db
def test_post_model():

  user = User.objects.create_user(
      username="admin",
      password="123"
  )

  post = Post.objects.create(
      title="Post Teste",
      slug="post-teste",
      author=user,
      content="Este é um post teste.",
      status="draft"
  )

  assert post.title == "Post Teste"
  assert post.content == "Este é um post teste."

