<template>
  <div class="post-form">
    <div class="columns is-centered">
      <div class="column is-narrow">
        <button
          class="button is-primary"
          @click="toggleModal">
          Create post
        </button>
      </div>
    </div>
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
              :class="{ 'is-danger': emptyTitle }"
              v-model="title"
              id="post-form-title">
            <p
              class="help is-danger"
              v-if="emptyTitle">This field can't be empty</p>
          </div>
          <div class="columns is-centered">
            <div class="field column">
              <label class="label">Game</label>
              <game-picker
                :games="games"
                :game-id.sync="gameId"/>
            </div>
            <div
              v-if="gameId != 0"
              class="field column">
              <label class="label">Character</label>
              <char-picker
                :chars="chars"
                :char-id.sync="charId"/>
            </div>
            <div class="field column">
              <label class="label">Category</label>
              <cat-picker
                :categories="categories"
                :cat-ids.sync="catIds"/>
            </div>
          </div>
          <div class="field">
            <label class="label">Links</label>
            <textarea
              class="textarea"
              :class="{ 'is-danger': emptyLinks }"
              v-model="urls"
              id="post-form-urls"/>
            <p
              class="help is-danger"
              v-if="emptyLinks">This field can't be empty</p>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button
            class="button is-success"
            :disabled="emptyTitle || emptyLinks"
            @click="submitPost">Create</button>
          <button
            class="button"
            @click="toggleModal">Cancel</button>
        </footer>
      </div>
    </div>
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
      gameId: '0',
      charId: '0',
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
    },
    emptyTitle: function () {
      return this.title.trim() === ''
    },
    emptyLinks: function () {
      return this.urls.trim() === ''
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
                           errors
                        }
                      }`,
        variables: {
          title: newPost.title,
          gameId: newPost.gameId,
          charId: newPost.charId,
          categoriesId: newPost.catIds,
          links: newPost.urls
        }
      }).then(response => {
        const data = response.data.createPost
        if (data.ok) {
          console.log('Post successfully added.')
          this.toggleModal()
        } else {
          data.errors.map(err => {
            console.error(err)
          })
        }
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
