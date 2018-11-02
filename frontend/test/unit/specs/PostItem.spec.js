import { mount } from '@vue/test-utils'
import PostItem from '@/components/PostItem'

describe('Post-item Component', () => {
    let wrapper
    
    beforeEach(() => {
        wrapper = mount(PostItem, {
            propsData: {
              post: {
                  title: 'Bryan bnbs',
                  game: {name:'Tekken', id: 1},
                  char: {name:'Bryan', id: 2},
                  categories: [{name:'Combo', id: 3}],
                  description: 'Some basic Bryan combos'
              }
            }
          })
    })

    test('description toggle', () => {
        let description = wrapper.find('div.desc')
        let descriptionPreview = wrapper.find('div.desc-preview')
        expect(description.attributes('hidden')).toBeTruthy()
        expect(descriptionPreview.attributes('hidden')).toBeFalsy()

        wrapper.trigger('click')
        
        expect(description.attributes('hidden')).toBeFalsy()
        expect(descriptionPreview.attributes('hidden')).toBeTruthy()

        wrapper.find('.tag').trigger('click')

        expect(description.attributes('hidden')).toBeFalsy()
        expect(descriptionPreview.attributes('hidden')).toBeTruthy()
    })

    test('Emit event when clicking game tag', () => {
        let gameTag = wrapper.find('div:nth-of-type(2) .tag')
        gameTag.trigger('click')
        let emittedEvents = wrapper.emitted()
        expect(emittedEvents['updateGameId'].length).toBe(1)
    })

    test('Emit event when clicking char tag', () => {
        let charTag = wrapper.find('div:nth-of-type(3) .tag')
        charTag.trigger('click')
        let emittedEvents = wrapper.emitted()
        expect(emittedEvents['updateCharId'].length).toBe(1)
    })

    test('Emit event when clicking char tag', () => {
        let catTag = wrapper.find('div:nth-of-type(5) .tag')
        catTag.trigger('click')
        let emittedEvents = wrapper.emitted()
        expect(emittedEvents['updateCatIds'].length).toBe(1)
    })

    test('formatLink method', () => {
        let url = 'https://www.google.com/blabla'
        expect(wrapper.vm.formatLink(url)).toBe('www.google.com')
    })
})