<template>
  <div class="game-char-picker">
    <h1> {{ gameId }} </h1>
    <div class="select">
      <select v-model="gameIdC">
        <option value=-1>Any</option>
        <option
          v-for="game in games"
          :value="game.id"
          :key="game.id">
          {{ game.name }}
        </option>
      </select>
    </div>
    <div
      class="select"
      v-if="gameId != -1">
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
        return '-1'
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
    gameIdC: {
      get: function () {
        return this.gameId
      },
      set: function (newValue) {
        this.$emit('update:gameId', newValue)
      }
    },
    charIdC: {
      get: function () {
        return this.charId
      },
      set: function (newValue) {
        this.$emit('update:charId', newValue)
      }
    },
    chars: function () {
      return this.games.find((game) => game.id === this.gameIdC).chars
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
