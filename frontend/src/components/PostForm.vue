<template>
  <div class="post-form">
    <button
      class="button is-primary"
      @click="toggleModal">
      Create post
    </button>
    <div
      class="modal"
      :class="{ 'is-active': visible }">
      <div
        class="modal-background"
        @click="toggleModal"/>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Create post</p>
          <button
            class="delete"
            aria-label="close"
            @click="toggleModal"/>
        </header>
        <section class="modal-card-body">
          <div class="field">
            <label class="label">Title</label>
            <input
              class="input"
              v-model="title"
              id="post-form-title">
          </div>
          <div class="columns">
            <div class="field column">
              <label class="label">Game</label>
              <game-picker
                :games="games"
                :game-id.sync="gameId"/>
            </div>
            <div
              v-if="gameId != -1"
              class="field column">
              <label class="label">Character</label>
              <char-picker
                :chars="chars"
                :char-id.sync="charId"/>
            </div>
          </div>
          <div class="field">
            <label class="label">Urls</label>
            <textarea
              class="textarea"
              v-model="urls"
              id="post-form-urls"/>
          </div>
          <div class="field">
            <label class="label">Category</label>
            <cat-picker
              :categories="categories"
              :cat-ids.sync="catIds"/>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-success">Create</button>
          <button class="button">Cancel</button>
        </footer>
      </div>
    </div>
    <!--<label>Title :

    </label>
    <div class="select">
      <select v-model="gameId">
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
      <select v-model="charId">
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
      <select v-model="catIds">
        <option value=-1>-</option>
        <option
          v-for="cat in categories"
          :value="cat.id"
          :key="cat.id">
          {{ cat.name }}
        </option>
      </select>
    </div>
    <button
      class="button"
      @click="submitPost">Submit</button>-->
  </div>
</template>

<script>
import gql from 'graphql-tag'
import CatPicker from './CatPicker.vue'
import GamePicker from './GamePicker.vue'
import CharPicker from './CharPicker.vue'

export default {
  name: 'PostForm',
  data: function () {
    return {
      title: '',
      gameId: '-1',
      charId: '-1',
      catIds: '-1',
      urls: '',
      visible: false
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
    }
  },
  computed: {
    chars: function () {
      return this.games.find((game) => game.id === this.gameId).chars
    }
  },
  methods: {
    toggleModal () {
      this.visible = !this.visible
    },
    submitPost () {
      const newPost = {
        title: this.title.trim(),
        gameId: this.gameId,
        charId: this.charId,
        urls: this.urls.trim().split('\n'),
        catIds: this.catIds !== -1 ? [this.catIds] : []
      }
      this.$apollo.mutate({
        mutation: gql`mutation createPost($title: String, $gameId: Int, $charId: Int, $categoriesId: [Int], $links: [String]){
                        createPost(title: $title, gameId: $gameId, charId: $charId, categoriesId: $categoriesId, links: $links) {
                           ok
                           post{id title game{name} char{name} links{url} categories{name}}
                        }
                      }`,
        variables: {
          title: newPost.title,
          gameId: newPost.gameId,
          charId: newPost.charId,
          categoriesId: newPost.catIds,
          links: newPost.urls
        }
      }).then(data => {
        console.log(data)
      }).catch(error => {
        console.error(error)
      })
    }
  },
  components: { GamePicker, CharPicker, CatPicker }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
