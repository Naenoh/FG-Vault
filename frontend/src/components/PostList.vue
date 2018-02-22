<template>
  <div class="post-list container">
    <label for="post-search-input">Name : </label>
    <input
      class="input"
      v-model="title"
      id="post-search-input">
    <game-picker
      :games="allGames"
      :game-id.sync="gameId"/>
    <char-picker
      v-if="gameId != -1"
      :chars="chars"
      :char-id.sync="charId"/>
    <cat-picker
      :categories="allCategories"
      :cat-ids.sync="catIds"/>
    <div
      class="block"
      v-if="isFiltered">
      <span class="tag is-danger">
        Reset
        <button
          class="delete"
          @click="resetFilters"/>
      </span>
    </div>
    <table class="table is-hoverable">
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
    <post-form
      :games="allGames"
      :categories="allCategories"/>
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

export default {
  name: 'PostList',
  apollo: {
    allPosts: gql`{allPosts{posts{title game{name} char{name} categories{name} links{url}}}}`,
    allGames: gql`{allGames{id name chars{id name}}}`,
    allCategories: gql`{allCategories{id name}}`,
    filteredPosts: {
      query: gql`query getFilteredPosts($title: String, $gameId: Int, $charId: Int, $catIds: [Int]){
           filteredPosts(title:$title,gameId:$gameId,charId:$charId, catIds:$catIds){posts{title game{id name} char{id name} categories{id name} links{url}}}
        }`,
      variables () {
        return {
          title: this.title,
          gameId: this.gameId,
          charId: this.charId,
          catIds: this.catIds !== '-1' ? [this.catIds] : []
        }
      }
    }
  },
  data () {
    return {
      allPosts: {},
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
    }
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
