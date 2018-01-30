<template>
  <tr class="post-item">
    <td>{{ post.title }}</td>
    <td>{{ post.game.name }}</td>
    <td>{{ post.char.name }}</td>
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
      <div
        v-for="link in post.categories"
        :key="link.id">
        {{ link.name }}
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
  }
}
</script>
