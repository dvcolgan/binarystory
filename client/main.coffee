m = require('mithril')
Story = require('client/views/story')

m.route document.body, '/1',
    #'/login': Login
    '/:id': Story
