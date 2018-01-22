<template>
  <div class="post-list">
    <table>
      <post-header/>
      <post-item
        v-for="post in posts"
        :post="post"
        :key="post.id"/>
    </table>
  </div>
</template>

<script>
import PostItem from './PostItem.vue'
import PostHeader from './PostHeader.vue'

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
  components: { PostItem, PostHeader }
}

</script>
