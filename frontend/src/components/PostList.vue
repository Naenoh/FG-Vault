<template>
  <div class="post-list container">
    <post-form
      :games="allGames"
      :categories="allCategories"/>
    <div class="columns is-centered post-filters">
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
            :game-id.sync="filters.gameId"/>
        </div>
      </div>
      <div
        class="field has-addons column is-narrow"
        v-if="filters.gameId">
        <div class="control">
          <div class="button is-static">Char</div>
        </div>
        <div class="control">
          <char-picker
            :chars="chars"
            :char-id.sync="filters.charId"/>
        </div>
      </div>
      <div class="field has-addons column is-narrow">
        <div class="control">
          <div class="button is-static">Category</div>
        </div>
        <div class="control">
          <cat-picker
            :categories="allCategories"
            :cat-ids.sync="filters.catIds"
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
    <div
      v-if="!noResults"
      class="table is-hoverable is-fullwidth">
      <post-header/>
      <div
      :class="{ 'is-blurred': isLoading}">
        <post-item
          v-for="post in filteredPosts.posts"
          :post="post"
          :key="post.id"
          @updateGameId="updateGameId"
          @updateCharId="updateCharId"
          @updateCatIds="updateCatIds"/>
      </div>
    </div>
    <div
      v-if="!noResults"
      class="buttons has-addons is-centered">
      <button
        :disabled="page === 1"
        class="button"
        @click="page--">&lt;</button>
      <button class="button is-static">{{ page }} / {{ filteredPosts.lastPage }}</button>
      <button
        :disabled="page === filteredPosts.lastPage"
        class="button"
        @click="page++">&gt;</button>
    </div>
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
      query: gql`query getFilteredPosts($page: Int, $title: String, $gameId: Int, $charId: Int, $catIds: [Int]){
          filteredPosts(page: $page, title:$title,gameId:$gameId,charId:$charId, catIds:$catIds){posts{title description game{id name} char{id name} categories{id name} links{url} timeCreated} lastPage}
       }`,
      variables () {
        let vars = Object.assign({page: this.page}, this.filters)
        return vars
      },
      result () {
        if (!this.querySynced()) {
          this.updateRoute()
        }
      },
      loadingKey: 'loadingCount'
    }
  },
  data () {
    return {
      allGames: [],
      allCategories: [],
      filteredPosts: {},
      page: 1,
      filters: {
        title: this.$route.query.title,
        gameId: this.$route.query.gameId,
        charId: this.$route.query.charId,
        catIds: this.$route.query.catIds
      },
      loadingCount: 0
    }
  },
  methods: {
    updateGameId: function (val) {
      this.filters.gameId = val
    },
    updateCharId: function (val) {
      this.filters.gameId = val.game
      this.filters.charId = val.char
    },
    updateCatIds: function (val) {
      this.filters.catIds = val
    },
    resetFilters: function () {
      this.filters = {
        title: undefined,
        gameId: undefined,
        charId: undefined,
        catIds: undefined
      }
      this.page = 1
    },
    querySynced: function () {
      return this.filters.title === this.$route.query.title &&
        this.filters.gameId === this.$route.query.gameId &&
        this.filters.charId === this.$route.query.charId &&
        this.filters.catIds === this.$route.query.catIds
    },
    updateRoute: function () {
      this.$router.replace(
        {
          path: '',
          query: this.filters
        }
      )
    },
    updateData: function () {
      // Copying the query object
      this.filters = Object.assign({}, this.$route.query)
    },
    debounceTitle: debounce(function (e) {
      this.filters.title = e.target.value.trim()
    }, 200)
  },
  computed: {
    isLoading: function () {
      return this.loadingCount > 0
    },
    isFiltered: function () {
      // Checks if every property in filters is undefined or empty string
      return !Object.values(this.filters).every(val => val === undefined || val === '')
    },
    noResults: function () {
      return !this.filteredPosts.posts || this.filteredPosts.posts.length === 0
    },
    chars: function () {
      if (this.filters.gameId) {
        return this.allGames.find((game) => game.id === this.filters.gameId).chars
      } else {
        return []
      }
    }
  },
  watch: {
    'filters.gameId': {
      handler (oldVal, newVal) {
        if (newVal) {
          this.filters.charId = undefined
        }
      }
    },
    'filters': {
      handler (oldVal, newVal) {
        this.page = 1
      },
      deep: true
    },
    '$route' (oldVal, newVal) {
      if (!this.querySynced()) {
        this.updateData()
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
  .is-blurred{
    -webkit-filter: blur(5px);
    -moz-filter: blur(5px);
    -o-filter: blur(5px);
    -ms-filter: blur(5px);
    filter: blur(5px);
  }
  @media screen and (max-width: 768px) {
    .post-filters {
      margin-left: 0.75rem;
    }
  }
</style>
