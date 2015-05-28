import sys

settings = sys.modules['project.settings']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '{{ project_name }}.default'
    }
}

if settings.PRODUCTION:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211'
        }
    }
