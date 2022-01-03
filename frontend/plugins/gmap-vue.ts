import Vue from 'vue'
import GmapVue from 'gmap-vue'
import { defineNuxtPlugin } from '@nuxtjs/composition-api'

export default defineNuxtPlugin(ctx => {
  Vue.use(GmapVue,{
    load: {
      key: ctx.$config.googleApiKey,
      libraries: 'places',
      region: 'En',
      language: 'en'
    },
    installComponents: true
  })
})
