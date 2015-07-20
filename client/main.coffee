m = require('mithril')
Story = require('client/views/story')

m.route.mode = 'hash'

m.route document.body, '/story/1',
    '/story/:id': Story
    #'/login': Login
