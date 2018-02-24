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
                :game-id.sync="gameId"
                :for-search="false"/>
            </div>
            <div
              v-if="gameId != 0"
              class="field column">
              <label class="label">Character</label>
              <char-picker
                :chars="chars"
                :char-id.sync="charId"
                :for-search="false"/>
            </div>
            <div class="field column">
              <label class="label">Category</label>
              <cat-picker
                :categories="categories"
                :cat-ids.sync="catIds"
                :for-search="false"/>
            </div>
          </div>
          <div class="field">
            <label
              class="label"
              for="post-form-urls">
              Links
              <div class="dropdown is-hoverable is-up">
                <span class="is-rounded tag is-unselectable is-info dropdown-trigger">
                  ?
                </span>
                <div class="dropdown-menu">
                  <div class="dropdown-content">
                    <div class="dropdown-item">
                      One link per line.
                    </div>
                  </div>
                </div>
              </div>
            </label>
            <textarea
              class="textarea"
              :class="{ 'is-danger': invalidLinks }"
              v-model="urls"
              id="post-form-urls"/>
            <div v-if="invalidLinks">
              <span
                class="help is-danger"
                v-for="(error,index) in linksErrorMsgs"
                :key="index"> {{ error }}</span>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button
            class="button is-success"
            :disabled="emptyTitle || invalidLinks"
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
import validUrl from 'valid-url'

export default {
  name: 'PostForm',
  data: function () {
    return {
      title: '',
      gameId: '1',
      charId: '1',
      catIds: '-1',
      urls: '',
      visible: false,
      externalLinkErrors: []
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
      if (this.games.length !== 0) {
        console.log(this.games)
        return this.games.find((game) => game.id === this.gameId).chars
      }
      return []
    },
    links: function () {
      return this.urls.trim().split('\n')
    },
    emptyTitle: function () {
      return this.title.trim() === ''
    },
    invalidLinks: function () {
      return this.linksErrorMsgs.length !== 0
    },
    linksErrorMsgs: function () {
      const errors = []
      if (this.urls.trim() === '') {
        errors.push('This field can\'t be empty')
      } else {
        this.links.map(function (link) {
          if (!validUrl.isWebUri(link)) {
            errors.push('This URL isn\'t valid: ' + link)
          }
        })
      }
      errors.push(...this.externalLinkErrors)
      return errors
    }
  },
  methods: {
    toggleModal () {
      this.visible = !this.visible
      this.gameId = '1'
      this.charId = '1'
    },
    submitPost () {
      const newPost = {
        title: this.title.trim(),
        gameId: this.gameId,
        charId: this.charId,
        urls: this.links,
        catIds: this.catIds !== -1 ? [this.catIds] : []
      }
      this.$apollo.mutate({
        mutation: gql`mutation createPost($title: String, $gameId: Int, $charId: Int, $categoriesId: [Int], $links: [String]){
                        createPost(title: $title, gameId: $gameId, charId: $charId, categoriesId: $categoriesId, links: $links) {
                           ok
                           post{title game{id name} char{id name} categories{id name} links{url}}
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
      }).then((response) => {
        const data = response.data.createPost
        if (data.ok) {
          console.log('Post successfully added.')
          this.$apollo.provider.defaultClient.resetStore()
          this.toggleModal()
        } else {
          this.externalLinkErrors.push(...data.errors)
        }
      }).catch(function (error) {
        console.error(error)
      })
    }
  },
  watch: {
    urls: function () {
      this.externalLinkErrors = []
    },
    gameId: function () {
      this.charId = this.chars[0].id
    }
  },
  components: { GamePicker, CharPicker, CatPicker }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
