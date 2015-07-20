m = require('mithril')

StoryNode = {}
StoryNode.get = (id) ->
    m.request
        method: 'GET'
        url: "/api/story/story-node/#{id}/"

module.exports =
    controller: class
        constructor: ->
            @vm = {}
            @vm.node = StoryNode.get(m.route.param('id'))

    view: (ctrl) ->
        node = ctrl.vm.node()
        [
            m 'h1', 'This is a game'
            m 'p', node.text

            if node.choice_a?
                m 'p',
                    m "a[href=/story/#{node.choice_a}]",
                        config: m.route
                        node.choice_a_label
            if node.choice_b?
                m 'p',
                    m "a[href=/story/#{node.choice_b}]",
                        config: m.route
                        node.choice_b_label
        ]
