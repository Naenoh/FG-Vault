<template>
  <div class="game-picker">
    <div class="select">
      <select v-model="gameIdC">
        <option
          v-if="forSearch"
          value="-1">Any</option>
        <option
          v-for="game in games"
          :value="game.id"
          :key="game.id">
          {{ game.name }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GameCharPicker',
  props: {
    games: {
      type: Array,
      default: function () {
        return []
      }
    },
    gameId: {
      type: String,
      default: function () {
        return '1'
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
    gameIdC: {
      get: function () {
        return this.gameId
      },
      set: function (newValue) {
        this.$emit('update:gameId', newValue)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
