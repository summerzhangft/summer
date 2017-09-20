# summer
> based on [startbootstrap clean blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog)

# settings.py
SUMMER_CONFIG = {
    'SITE_NAME': os.getenv('SITE_NAME', 'Summer'), # site name
    'SITE_DESCRIPTION': os.getenv('SITE_DESCRIPTION', 'Shared Your knowledge'), # site description
    'SITE_HOME_BACKGROUND': os.getenv('SITE_HOME_BACKGROUND', '/static/img/home-bg.jpg'), # default home page background
    'SITE_ARTICLE_BACKGROUND': os.getenv('SITE_POST_BACKGROUND', '/static/img/article-bg.jpg'), # default article page background
    'SITE_FORM_BACKGROUND': os.getenv('SITE_FORM_BACKGROUND', '/static/img/form-bg.jpg'), # default form page background
    'SITE_ERROR_BACKGROUND': os.getenv('SITE_ERROR_BACKGROUND', '/static/img/error-bg.png'), # default error page background
    'SITE_ZHIHU_URL': os.getenv('ZHIHU_URL', 'https://www.zhihu.com/'), # zhihu url
    'SITE_GITHUB_URL': os.getenv('GITHUB_URL', 'https://github.com/summerzhangft') # github url
}
            
