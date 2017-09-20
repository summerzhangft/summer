from django.shortcuts import render, get_object_or_404, render_to_response
from article.models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
#@login_required 装饰器修饰的view函数会先通过session key 检查是否登录，已经登录的用户可以正常操作。没有登录的用户重定向到login_url指定的位置。若未指定login_url参数，则重定向到settings.LOGIN_URL
from django.urls import reverse_lazy
from django.http import  HttpResponseForbidden
from django.http import HttpResponseRedirect
from .forms import ArticleForm
from .tools import get_article_background


def home(request):
    paginator=Paginator(Article.objects.all(),10)#10篇文章为一页
    page = request.GET.get('page')
    try:
        articles=paginator.page(page)
    except PageNotAnInteger:
        #if page id not an inter,deliver first page
        articles = paginator.page(1)
    except EmptyPage:
        #if page is out of range,deliver last page of results
        articles = paginator.page(paginator.num_pages)
    return render(request, 'home.html',{'articles':articles})

def detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    tags = article.tags.all()
    return render(request,'article_detail.html',{'article':article,'tags':tags})

@login_required(login_url=reverse_lazy('author:login')) 
def edit(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    if article.author != request.user and not request.user.is_superuser:
        #return HttpResponseForbidden()render_to_response('error.html',{'status_code':403,'message':'Forbidden :('}))
        return HttpResponseForbidden(render_to_response('error.html', {'status_code': 403, 'message': 'Forbidden :('}))
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('article:detail',kwargs={'article_id':form.instance.id}))
    context = {
              'form':form, #表单
              'header_id':'tag-heading',#前端的样式
              'title':'Edit Article',#标题
              'subtitle':form.instance.title,#子标题
              'background':form.instance.background or get_article_background(),#文章的背景以及图片
              'submit':'update',#提高按钮
              }
    return render(request,'generic_form.html', context)

@login_required(login_url=reverse_lazy('author:login'))
def new(request):
    #来获取article的表单数据
    form = ArticleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #将登录用户作为作者
        form.instance.author = request.user
        form.save()
        return HttpResponseRedirect(reverse_lazy('article:detail',kwargs={'article_id':form.instance.id}))
    #创建context来集中处理需要传递到页面的数据
    context = {
              'form':form, #表单
              'header_id':'tag-heading',#前端的样式
              'title':'New Article',#标题
              'subtitle':'That looks great!',#子标题
              'background':form.instance.background or get_article_background(),#文章的背景以及图片
              'submit':'new',#提高按钮
              }
    #如果表单没有正常提交，仍然留在原来页面
    return render(request, 'generic_form.html', context)

# Create your views here.

