m = require('mithril')
Story = require('client/views/story')

m.request
    method: 'GET'
    url: '/api/story/story-node/images/'
.then (images) ->
    for src in images
        img = new Image()
        img.src = src

    setTimeout (->
        m.route document.body, '/1',
            '/:id': Story
    ), 2000
