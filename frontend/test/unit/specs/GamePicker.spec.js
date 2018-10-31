import Vue from 'vue'
import GamePicker from '@/components/GamePicker'

describe('Game-picker Component', () => {
    let $mounted
    
    beforeEach(() => {
        $mounted = new Vue(GamePicker).$mount()
    })

    it('should render default option', () => {
        expect($mounted.$el.querySelector('.select select').textContent.trim())
        .toEqual('Any')
    })
})