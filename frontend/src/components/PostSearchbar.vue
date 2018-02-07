<template>
  <div class="post-searchbar">
    <label for="post-search-input">Name : </label>
    <input
      v-model="searchval.text"
      id="post-search-input">
    <select
    v-model="searchval.gameId">
      <option
        v-for="game in games"
        :value="game.id"
        :key="game.id">
        {{ game.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'PostSearchbar',
  data: function () {
    return {
      searchval: {text: '', gameId: -1}
    }
  },
  props: {
    games: {
      type: Array,
      default: function () {
        return []
      }
    }
  },
  watch: {
    searchval: {
      handler () {
        this.$emit('update:searchval', this.searchval)
      },
      deep: true
    }
  }
}
</script>
