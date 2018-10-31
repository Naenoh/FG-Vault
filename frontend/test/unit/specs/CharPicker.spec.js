import { mount } from '@vue/test-utils'
import CharPicker from '@/components/CharPicker'

describe('Character-picker Component', () => {
    let wrapper
    
    beforeEach(() => {
        wrapper = mount(CharPicker)
    })

    it('should render default option', () => {
        expect(wrapper.find('.select select').text())
            .toEqual('Any')
    })

    it('should emit event when value is changed', () => {
        const charId = '1'
        wrapper.setProps({
            chars: [{id: charId, name:'Tekken'}]
        })
        const options = wrapper.find('.select select').findAll('option')
        options.at(1).setSelected()
        const emittedUpdates = wrapper.emitted()['update:charId']
        expect(emittedUpdates.length)
            .toEqual(1)
        
        // emmitedUpdates is an array of array because you can emit multiple values at once
        expect(emittedUpdates)
            .toEqual([[charId]])
    })
})