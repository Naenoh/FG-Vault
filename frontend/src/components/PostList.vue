<template>
  <div class="post-list container">
    <post-form
      :games="allGames"
      :categories="allCategories"/>
    <div class="columns is-centered">
      <div class="field has-addons column is-narrow">
        <div class="control">
          <div class="button is-static">Title</div>
        </div>
        <div class="control">
          <input
            class="input"
            @input="debounceTitle"
            id="post-search-input">
        </div>
      </div>
      <div class="field has-addons column is-narrow">
        <div class="control">
          <div class="button is-static">Game</div>
        </div>
        <div class="control">
          <game-picker
            :games="allGames"
            :game-id.sync="gameId"/>
        </div>
      </div>
      <div
        class="field has-addons column is-narrow"
        v-if="gameId != -1">
        <div class="control">
          <div class="button is-static">Char</div>
        </div>
        <div class="control">
          <char-picker
            :chars="chars"
            :char-id.sync="charId"/>
        </div>
      </div>
      <div class="field has-addons column is-narrow">
        <div class="control">
          <div class="button is-static">Category</div>
        </div>
        <div class="control">
          <cat-picker
            :categories="allCategories"
            :cat-ids.sync="catIds"
            :for-search="true"/>
        </div>
      </div>
      <div
        class="column is-narrow"
        v-if="isFiltered">
        <button
          class="button is-danger"
          @click="resetFilters">
          Reset
        </button>
      </div>
    </div>
    <table
      v-if="!noResults"
      class="table is-hoverable is-fullwidth">
      <post-header/>
      <tbody>
        <post-item
          v-for="post in filteredPosts.posts"
          :post="post"
          :key="post.id"
          @updateGameId="updateGameId"
          @updateCharId="updateCharId"
          @updateCatIds="updateCatIds"/>
      </tbody>
    </table>
    <div
      v-if="noResults"
      class="message is-danger">
      <div class="message-body">
        No results founds. Try broadening your query or adding new posts.
      </div>
    </div>
  </div>
</template>

<script>
import PostItem from './PostItem.vue'
import PostHeader from './PostHeader.vue'
import PostForm from './PostForm.vue'
import CatPicker from './CatPicker.vue'
import GamePicker from './GamePicker.vue'
import CharPicker from './CharPicker.vue'
import gql from 'graphql-tag'
import debounce from 'lodash.debounce'

export default {
  name: 'PostList',
  apollo: {
    allGames: gql`{allGames{id name chars{id name}}}`,
    allCategories: gql`{allCategories{id name}}`,
    filteredPosts: {
      query: gql`query getFilteredPosts($title: String, $gameId: Int, $charId: Int, $catIds: [Int]){
          filteredPosts(title:$title,gameId:$gameId,charId:$charId, catIds:$catIds){posts{title game{id name} char{id name} categories{id name} links{url}}}
       }`,
      variables () {
        return {
          title: this.title.trim(),
          gameId: this.gameId,
          charId: this.charId,
          catIds: this.catIds !== '-1' ? [this.catIds] : []
        }
      }
    }
  },
  data () {
    return {
      allGames: [],
      allCategories: [],
      filteredPosts: {},
      title: '',
      gameId: '-1',
      charId: '-1',
      catIds: '-1',
      baseData: {
        title: '',
        gameId: '-1',
        charId: '-1',
        catIds: '-1'
      }
    }
  },
  methods: {
    updateGameId: function (val) {
      this.gameId = val
    },
    updateCharId: function (val) {
      this.gameId = val.game
      this.charId = val.char
    },
    updateCatIds: function (val) {
      this.catIds = val
    },
    resetFilters: function () {
      this.title = ''
      this.gameId = '-1'
      this.charId = '-1'
      this.catIds = '-1'
    },
    debounceTitle: debounce(function (e) {
      this.title = e.target.value
    }, 200)
  },
  computed: {
    isFiltered: function () {
      const currentData = {
        title: this.title,
        gameId: this.gameId,
        charId: this.charId,
        catIds: this.catIds
      }
      return !(JSON.stringify(this.baseData) === JSON.stringify(currentData))
    },
    noResults: function () {
      return !this.filteredPosts.posts || this.filteredPosts.posts.length === 0
    },
    chars: function () {
      return this.allGames.find((game) => game.id === this.gameId).chars
    }
  },
  watch: {
    gameId: {
      handler (a, b) {
        if (b !== '-1') {
          this.charId = '-1'
        }
      }
    }
  },
  components: { PostItem, PostHeader, PostForm, CatPicker, GamePicker, CharPicker }
}

</script>

<style scoped>
  .post-list{
    flex: 1;
  }
</style>
