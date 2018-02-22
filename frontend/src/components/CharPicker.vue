<template>
  <div class="char-picker">
    <div class="select">
      <select v-model="charIdC">
        <option value=-1>Any</option>
        <option
          v-for="char in chars"
          :value="char.id"
          :key="char.id">
          {{ char.name }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CharPicker',
  props: {
    chars: {
      type: Array,
      default: function () {
        return []
      }
    },
    charId: {
      type: String,
      default: function () {
        return '-1'
      }
    }
  },
  computed: {
    charIdC: {
      get: function () {
        return this.charId
      },
      set: function (newValue) {
        this.$emit('update:charId', newValue)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
