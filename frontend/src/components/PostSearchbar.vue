<template>
  <div class="post-searchbar">
    <label for="post-search-input">Name : </label>
    <input
      class="input"
      v-model="titlec"
      id="post-search-input">
    <div class="select">
      <select v-model="gameIdc">
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
      <select v-model="charIdc">
        <option value=-1>Any</option>
        <option
          v-for="char in chars"
          :value="char.id"
          :key="char.id">
          {{ char.name }}
        </option>
      </select>
    </div>
    <div class="select">
      <select v-model="catIdsc">
        <option value=-1>Any</option>
        <option
          v-for="cat in categories"
          :value="cat.id"
          :key="cat.id">
          {{ cat.name }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostSearchbar',
  data: function () {
    return {
      titlec: this.title,
      gameIdc: this.gameId,
      charIdc: this.charId,
      catIdsc: this.catIds
    }
  },
  props: {
    games: {
      type: Array,
      default: function () {
        return []
      }
    },
    categories: {
      type: Array,
      default: function () {
        return []
      }
    },
    title: {
      type: String,
      default: ''
    },
    gameId: {
      type: String,
      default: '-1'
    },
    charId: {
      type: String,
      default: '-1'
    },
    catIds: {
      type: String,
      default: '-1'
    }
  },
  computed: {
    chars: function () {
      console.log(this.games, this.gameIdc)
      return this.games.find((game) => game.id === this.gameIdc).chars
    }
  },
  watch: {
    titlec: {
      handler () {
        this.$emit('update:title', this.titlec)
      }
    },
    gameIdc: {
      handler () {
        this.$emit('update:gameId', this.gameIdc)
      }
    },
    charIdc: {
      handler () {
        this.$emit('update:charid', this.charIdc)
      }
    },
    catIdsc: {
      handler () {
        this.$emit('update:catids', this.catIdsc)
      }
    }
  }
}
</script>
