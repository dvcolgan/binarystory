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
        m '.wrapper ',
            m '.container',
                m 'h1', node.title

                if node.image?
                    m '.img-container',
                        m 'img',
                            src: node.image

                m 'p.node-text', node.text

                if node.choice_a?
                    m '.choice.choice-a',
                        m "a[href=/#{node.choice_a}]",
                            config: m.route
                            node.choice_a_label
                if node.choice_b?
                    m '.choice.choice-b',
                        m "a[href=/#{node.choice_b}]",
                            config: m.route
                            node.choice_b_label

                if node.voiceover_mp3? or node.voiceover_ogg?
                    m 'audio',
                        autoplay: true
                        if node.voiceover_mp3?
                            m 'source',
                                src: node.voiceover_mp3
                                type: 'audio/mp3'
                        if node.voiceover_ogg?
                            m 'source',
                                src: node.voiceover_ogg
                                type: 'audio/ogg'
