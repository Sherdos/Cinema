movie = (
        (None, {
            'fields': (('title'),)
        }),
    (None, {
        'fields': ('description', ('poster', 'get_image', 'video'))
    }),
    (None, {
        'fields': (('year'),)
    }),
    (None, {
        'fields': (('genres', 'category'),)
    }),
    ('Options', {
        'fields': (('url',),)
    }),
)
serial = (
    (None, {
        'fields': (('title'),)
    }),
    (None, {
        'fields': ('description', ('poster', 'get_image'))
    }),
    (None, {
        'fields': (('year'),)
    }),
    (None, {
        'fields': (('genres', 'category'),)
    }),
    ('Options', {
        'fields': (('url',),)
    }),
)
