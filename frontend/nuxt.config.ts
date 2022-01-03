import { NuxtConfig } from '@nuxt/types'

const config: NuxtConfig = {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'simple-health',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    "~/assets/health.general.css"
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    "~/plugins/vee-validate",
    "~/plugins/gmap-vue",
    "~/plugins/datetime",
    "~/plugins/axios",
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxt/typescript-build',
    '@nuxtjs/composition-api/module',
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/i18n'
  ],

  i18n: {
    locales: [
      { code: 'ja', iso: 'ja_JP', file: 'ja.js' },
      { code: 'en', iso: 'en-US', file: 'en.js' }
    ],
    defaultLocale: 'ja',
    langDir: 'locales/',
    vueI18n: {
      fallbackLocale: 'en'
    },
    detectBrowserLanguage: {
      useCookie: true,
      redirectOn: 'all'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [
      'vee-validate/dist/rules',
      /^gmap-vue($|\/)/
    ]
  },
  generate: {
    dir: 'public'
  },

  watchers: {
    webpack: {
      poll: true
    }
  },

  publicRuntimeConfig: {
    domain: process.env.DOMAIN,
    apiUrl: process.env.API_URL,
    // TODO: 可能ならprivateRuntimeConfigに定義する。
    googleApiKey: process.env.GOOGLE_API_KEY,
    fileStorage: process.env.FILE_STORAGE || 'Local',
    imageUrl: 'http://localhost/images/'
  }
}

export default config
