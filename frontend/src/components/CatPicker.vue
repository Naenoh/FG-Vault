<template>
  <div class="select cat-picker">
    <select v-model="catIdsC">
      <option :value=undefined>{{ forSearch ? 'Any' : 'None' }}</option>
      <option
        v-for="cat in categories"
        :value="cat.id"
        :key="cat.id">
        {{ cat.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'CatPicker',
  props: {
    categories: {
      type: Array,
      default: function () {
        return []
      }
    },
    catIds: {
      type: String,
      default: function () {
        return undefined
      }
    },
    forSearch: {
      type: Boolean,
      default: function () {
        return true
      }
    }
  },
  computed: {
    catIdsC: {
      get: function () {
        return this.catIds
      },
      set: function (newValue) {
        this.$emit('update:catIds', newValue)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
