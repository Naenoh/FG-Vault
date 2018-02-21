<template>
  <tr class="post-item">
    <td>{{ post.title }}</td>
    <td>
      <a
        class="tag"
        :data-id="post.game.id"
        @click="filterGame">{{ post.game.name }}</a>
    </td>
    <td>
      <a
        class="tag"
        :data-id="post.char.id">{{ post.char.name }}</a>
    </td>
    <td>
      <div
        v-for="link in post.links"
        :key="link.id">
        <a
        :href="link.url">{{ link.url }}
        </a>
      </div>
    </td>
    <td>
      <div class="tags">
        <a
          v-for="cat in post.categories"
          :key="cat.id"
          class="tag">
          {{ cat.name }}
        </a>
      </div>
    </td>

  </tr>
</template>

<script>
export default {
  name: 'PostItem',
  props: {
    post: {
      type: Object,
      default: function () {
        return {}
      }
    }
  },
  methods: {
    filterGame: function (a) {
      this.$emit('updateGameId', a.target.dataset.id)
    }
  }
}
</script>
