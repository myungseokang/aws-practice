# 기타
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from blog.models import Post
from common.models import Profile


# /user/<username>/ 유저 자세히 보기
class ViewUser(DetailView):
    model = User
    template_name = 'user/view_user.html'
    slug_field = 'username'
    context_object_name = 'p'

    def get_context_data(self, **kwargs):
        # post_number에 이사람이 적었던 글수를 카운트해서 리턴
        context = super(ViewUser, self).get_context_data(**kwargs)
        context["post_number"] = Post.objects.filter(author=self.get_object()).count()
        return context


# /post/<username>/delete/ 유저 삭제
class DeleteUser(DeleteView):
    model = User
    success_url = '/'
    slug_field = 'username'

    def get_object(self, queryset=None):
        obj = super(DeleteUser, self).get_object()
        print(obj.id + self.request.user.id)
        if not obj.id == self.request.user.id:
            raise Http404
        return obj


# / 홈
def home(request):
    # 메인에 표시할 글 5개
    posts = Post.objects.all().order_by('-id')[:5]
    # 글이 10개가 넘어가면 메인에서 [다음] 버튼 표시
    posts_count = Post.objects.all().count()
    return render(request, 'home.html', {'posts': posts, 'posts_count': posts_count})


# /create/ 가입
class CreateUser(CreateView):
    model = User
    template_name = 'create.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        p = Profile()
        p.user = user
        p.save()
        messages.success(self.request, 'Complete created User!')
        return super(CreateUser, self).form_valid(form)
