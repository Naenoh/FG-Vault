import { mount } from '@vue/test-utils'
import CatPicker from '@/components/CatPicker'

describe('Category-picker Component', () => {
    let wrapper
    
    beforeEach(() => {
        wrapper = mount(CatPicker)
    })

    it('should render default option', () => {
        expect(wrapper.find('.select select').text())
            .toEqual('Any')
    })

    it('should render None option when not for search', () => {
        wrapper.setProps({forSearch: false})
        expect(wrapper.find('.select select').text())
            .toEqual('None')
    })

    it('should emit event when value is changed', () => {
        const categoryId = '1'
        wrapper.setProps({
            categories: [{id: categoryId, name:'Combo'}]
        })
        const options = wrapper.find('.select select').findAll('option')
        options.at(1).setSelected()
        const emittedUpdates = wrapper.emitted()['update:catIds']
        expect(emittedUpdates.length)
            .toEqual(1)
        
        // emmitedUpdates is an array of array because you can emit multiple values at once
        expect(emittedUpdates)
            .toEqual([[categoryId]])
    })
})