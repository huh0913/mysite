# your_app/utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_post_email(user, post):
    subject = 'New Post Alert'
    html_content = render_to_string('your_app/email_template.html', {'user': user, 'post': post, 'post_url': f'http://yourwebsite.com/posts/{post.id}'})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, 'your-email@example.com', [user.email])
    email.attach_alternative(html_content, "text/html")
    email.send()
