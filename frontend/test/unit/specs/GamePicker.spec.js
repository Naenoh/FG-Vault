import { mount } from '@vue/test-utils'
import GamePicker from '@/components/GamePicker'

describe('Game-picker Component', () => {
    let wrapper
    
    beforeEach(() => {
        wrapper = mount(GamePicker)
    })

    it('should render default option', () => {
        expect(wrapper.find('.select select').text())
            .toEqual('Any')
    })

    it('should emit event when value is changed', () => {
        const gameId = '1'
        wrapper.setProps({
            games: [{id: gameId, name:'Tekken'}]
        })
        const options = wrapper.find('.select select').findAll('option')
        options.at(1).setSelected()
        const emittedUpdates = wrapper.emitted()['update:gameId']
        expect(emittedUpdates.length)
            .toEqual(1)
        
        // emmitedUpdates is an array of array because you can emit multiple values at once
        expect(emittedUpdates)
            .toEqual([[gameId]])
    })
})