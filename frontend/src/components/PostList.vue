<template>
  <div class="post-list">
    <table>
      <post-header/>
      <post-item
        v-for="post in posts"
        :post="post"
        :key="post.id"/>
    </table>
    <p>
      {{ allPosts.posts }}
    </p>
  </div>
</template>

<script>
import PostItem from './PostItem.vue'
import PostHeader from './PostHeader.vue'
import gql from 'graphql-tag'

export default {
  name: 'PostList',
  props: {
    posts: {
      type: Array,
      default: function () {
        return {}
      }
    }
  },
  apollo: {
    allPosts: gql`{allPosts{posts{title}}}`
  },
  data () {
    return {
      allPosts: ''
    }
  },
  components: { PostItem, PostHeader }
}

</script>
