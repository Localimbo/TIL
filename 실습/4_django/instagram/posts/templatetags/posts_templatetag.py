from django import template

register = template.Library()


# #멀캠  ->  <a>#멀캠</a>   으로 바꿔주기
@register.filter
def hashtag_link(post):

    #    #멀캠 #4차 #역삼
    content = post.content
    #  [H obj(1), H obj(3), H obj(7)]    들어있는 전체 해쉬태그 content 값들 바꿔주기
    hashtags = post.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            f'{hashtag.content}',
            f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>'
        )

    return content
