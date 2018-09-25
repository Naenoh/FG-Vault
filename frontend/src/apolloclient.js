import Vue from 'vue'
import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'

let uri = window.location.origin + '/api/graphql'

if (process.env.NODE_ENV === 'development') {
  uri = 'http://127.0.0.1:5000/graphql'
}

const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: uri
})

// Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

// Install the vue plugin
Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

export {apolloProvider}
