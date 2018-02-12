<template>
  <div class="post-searchbar">
    <label for="post-search-input">Name : </label>
    <input
      v-model="searchval.text"
      id="post-search-input">
    <select
    v-model="searchval.gameId">
      <option value=-1>Any</option>
      <option
        v-for="game in games"
        :value="game.id"
        :key="game.id">
        {{ game.name }}
      </option>
    </select>
    <select
      v-if="searchval.gameId != -1"
      v-model="searchval.charId">
      <option value=-1>Any</option>
      <option
        v-for="char in chars"
        :value="char.id"
        :key="char.id">
        {{ char.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'PostSearchbar',
  data: function () {
    return {
      searchval: {text: '', gameId: -1, charId: -1}
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
  computed: {
    chars: function () {
      return this.games.find((game) => game.id === this.searchval.gameId).chars
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
