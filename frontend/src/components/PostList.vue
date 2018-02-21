<template>
  <div class="post-list container">
    <post-searchbar
      :game-id.sync="gameId"
      :char-id.sync="charId"
      :title.sync="title"
      :cat-ids.sync="catIds"
      :games="allGames"
      :categories="allCategories"/>
    <table class="table is-hoverable">
      <post-header/>
      <tbody>
        <post-item
          v-for="post in filteredPosts.posts"
          :post="post"
          :key="post.id"
          @updateGameId="updateGameId"/>
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
import PostSearchbar from './PostSearchbar.vue'
import PostForm from './PostForm.vue'
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
      catIds: '-1'
    }
  },
  methods: {
    updateGameId: function (val) {
      this.gameId = val
    }
  },
  components: { PostItem, PostHeader, PostSearchbar, PostForm }
}

</script>
