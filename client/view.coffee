m = require('mithril')

StoryNode = {}
StoryNode.get = (id) ->
    m.request
        method: 'GET'
        url: '/api/story/story-node/1/'

module.exports =
    controller: class
        constructor: ->
            @vm = {}
            @vm.node = StoryNode.get(1)

    view: (ctrl) ->
        m 'p', ctrl.vm.node.text
