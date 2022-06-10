from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Comment


def post_list(request):
    object_list= Post.published.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get("page", 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts,
               "page": page}
    return render(request, "blog/post/list.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    comments = Comment.objects.filter(post=post.pk)
    context = {"post": post, "comments": comments}
    return render(request, "blog/post/detail.html", context)

