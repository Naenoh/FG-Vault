<template>
  <div class="site-footer">
    <p class="is-size-7">Made by
      <a href="https://twitter.com/Naen0">Naeno</a>
      -
      <a @click="toggleModal"> FAQ </a>
    </p>
    <div
      class="modal"
      :class="{ 'is-active': visible }">
      <div
        class="modal-background"
        @click="toggleModal"/>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">FAQ</p>
          <button
            class="delete"
            aria-label="close"
            @click="toggleModal"/>
        </header>
        <section class="modal-card-body has-text-left">
          <section>
            <h3 class="title is-4">What is this ?</h3>
            <p>This is a website made to centralize and store links to fighting games related resources.</p>
            <br>
          </section>
          <section>
            <h3 class="title is-4">Why did you make it ?</h3>
            <p>
              A lot of resources are scattered in many places (wikis, discords, forums, subreddits, youtube, twitter...) with no convenient way to look for them all at once.
              The goal of this website is to have a place where people can post resources they create or find to allow others to look for them easily.
            </p>
            <br>
          </section>
          <section>
            <h3 class="title is-4">How is it made ?</h3>
            <p>
              The secondary (might be primary if it goes unused) goal of this website for me was to learn about new technologies and tools.
              I tried to go for a stack I knew almost nothing about.
              The Frontend is built with <a href="https://vuejs.org/index.html"><strong>Vue.js</strong></a> and <a href="https://bulma.io/"><strong>Bulma</strong></a>.
              The Backend is made with <a href="http://flask.pocoo.org/"><strong>Flask</strong></a> and <a href="https://www.sqlalchemy.org/"><strong>SQLAlchemy</strong></a>.
              To connect the two parts, I decided to go for a <a href="https://graphql.org/"><strong>GraphQL</strong></a> based API.
              To do that, i'm using <a href="https://graphene-python.org/"><strong>Graphene</strong></a> on the server side and <a href="https://www.apollographql.com/"><strong>Apollo</strong></a> for the client.
              The database is <a href="https://graphene-python.org/"><strong>Graphene</strong></a> and I'm using <a href="https://www.docker.com/"><strong>Docker</strong></a> with <a href="https://docs.docker.com/compose/"><strong>Docker Compose</strong></a> to facilitate deployement.
              I'm also using <a href="http://www.fabfile.org/"><strong>Fabric</strong></a> to easily run various tasks remotely.
            </p>
          </section>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteFooter',
  data: function () {
    return {
      visible: false
    }
  },
  methods: {
    toggleModal: function () {
      this.visible = !this.visible
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .site-footer{
    text-align: center;
    margin-top: 10px;
  }
</style>
