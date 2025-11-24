from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category

def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by("-created_at")
    categories = Category.objects.all()
    current_category = request.GET.get("category")
    query = request.GET.get("q")

    if current_category:
        posts = posts.filter(category__slug=current_category)

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(meta_description__icontains=query)
        )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog_list.html", {
        "page_obj": page_obj,
        "categories": categories,
        "current_category": current_category,
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)

    # Fetch related posts by same category, exclude current post
    related_posts = BlogPost.objects.filter(
        published=True,
        category=post.category
    ).exclude(id=post.id).order_by('-created_at')[:3]

    # Fallback: if less than 3, get recent posts
    if related_posts.count() < 3:
        fallback_posts = BlogPost.objects.filter(published=True).exclude(id=post.id).order_by('-created_at')[:3]
        related_posts = fallback_posts

    return render(request, "blog/blog_detail.html", {
        "post": post,
        "related_posts": related_posts,
    })


