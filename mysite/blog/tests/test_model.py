import pytest

from blog.models import Post

@pytest.mark.django_db
def test_post_model():
  post = Post.objects.create(title="Post Teste", text="Este é um post teste.")
  
  assert post.title == "Post Teste"
  assert post.text == "Este é um post teste."