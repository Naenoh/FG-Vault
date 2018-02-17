<template>
  <div class="post-form">
    <label>Title :
      <input
        v-model="title"
        id="post-form-title">
    </label>
    <select v-model="gameId">
      <option value=-1>Any</option>
      <option
        v-for="game in games"
        :value="game.id"
        :key="game.id">
        {{ game.name }}
      </option>
    </select>
    <select
      v-if="gameId != -1"
      v-model="charId">
      <option value=-1>Any</option>
      <option
        v-for="char in chars"
        :value="char.id"
        :key="char.id">
        {{ char.name }}
      </option>
    </select>
    <textarea
      v-model="urls"
      id="post-form-urls"/>
    <select v-model="catId">
      <option value=-1>-</option>
      <option
        v-for="cat in categories"
        :value="cat.id"
        :key="cat.id">
        {{ cat.name }}
      </option>
    </select>
    <button @click="submitPost">Submit</button>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'PostForm',
  data: function () {
    return {
      title: '',
      gameId: -1,
      charId: -1,
      catId: -1,
      urls: ''
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
    submitPost () {
      const newPost = {
        title: this.title,
        gameId: this.gameId,
        charId: this.charId,
        urls: this.urls.split('\n'),
        catId: [this.catId]
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
          categoriesId: newPost.catId,
          links: newPost.urls
        }
      }).then(data => {
        console.log(data)
      }).catch(error => {
        console.error(error)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
