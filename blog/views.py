from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Robaa",
        "date": date(2024, 2, 8),
        'title': 'Mountain Hiking',
        "excerpt": "There's noting like the views you get when hiking the mountains! And I wasn't even prepared fot what happened whilst I was enjoying the view!",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Modi, molestias veniam provident repellat numquam, in culpa sit eum totam est quia laudantium, dolore incidunt excepturi cupiditate suscipit officiis hic illo?
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Modi, molestias veniam provident repellat numquam, in culpa sit eum totam est quia laudantium, dolore incidunt excepturi cupiditate suscipit officiis hic illo?
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Modi, molestias veniam provident repellat numquam, in culpa sit eum totam est quia laudantium, dolore incidunt excepturi cupiditate suscipit officiis hic illo?
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Modi, molestias veniam provident repellat numquam, in culpa sit eum totam est quia laudantium, dolore incidunt excepturi cupiditate suscipit officiis hic illo?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Robaa",
        "date": date(2024, 2, 8),
        'title': 'Programming Is Great!',
        "excerpt":
        "Exploring the wonders of programming: from unleashing creativity to solving complex problems, it's a transformative tool shaping our digital landscape.",
        "content": """
        "Programming Is Great" delves into the multifaceted realm of coding, highlighting its significance in today's digital landscape. From fostering innovation to empowering problem-solving skills, this blog post celebrates the endless possibilities that programming offers. Join us as we explore the exciting journey of creativity and discovery through the art of coding.
        """
    },
    {
        "slug": "gaming-addiction",
        "image": "gaming.jpg",
        "author": "Robaa",
        "date": date(2024, 2, 8),
        'title': 'Conquering the Controller',
        "excerpt": "Examining the alarming rise of gaming addiction, its impact on mental health, and strategies for recovery and responsible gaming habits.",
        "content": """
        Gaming Addiction" explores the detrimental effects of excessive gaming on individuals' lives. From social isolation to compromised mental health, this blog post sheds light on the dark side of gaming. By delving into its root causes and offering strategies for recovery, readers can find hope and support in overcoming this pervasive addiction
        """
    }
]


def get_date(post):
    return post['date']
# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
