<template>
  <tr class="post-item">
    <td>{{ post.title }}</td>
    <td>
      <a
        class="tag"
        @click="filterGame">{{ post.game.name }}</a>
    </td>
    <td>
      <a
        class="tag"
        @click="filterChar">{{ post.char.name }}</a>
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
    filterGame: function () {
      this.$emit('updateGameId', this.post.game.id)
    },
    filterChar: function () {
      this.$emit('updateCharId', { game: this.post.game.id, char: this.post.char.id })
    }
  }
}
</script>
