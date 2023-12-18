import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject20231211.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！',
        'zlc18317773889@sina.com',
        ['984614856@qq.com'],
    )
    # HTML格式测试
    # import os
    # from django.core.mail import EmailMultiAlternatives
    #
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    #
    # if __name__ == '__main__':
    #     subject, from_email, to = '来自www.liujiangblog.com的测试邮件', 'xxx@sina.com', 'xxx@qq.com'
    #     text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    #     html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()