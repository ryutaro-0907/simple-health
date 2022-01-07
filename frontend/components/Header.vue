<template>
  <div>
    <v-app-bar
      color="#052037"
      dense
      dark
    >
      <div @click="router.push('/')" class="to-home">
        <img class="logo" src="logo.png" width="28" height="28">
        <v-toolbar-title>
          <span>
            Re.
          </span>
          <span style="font-size:14px">
            simple Health
          </span>
        </v-toolbar-title>
      </div>
      <v-spacer></v-spacer>
      <v-menu
        transition="slide-y-transition"
        bottom
        :offset-y="true"
        open-on-hover
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon
            v-bind="attrs"
            v-on="on"
          >
          <v-icon>mdi-web</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(language, key, index) in languages"
            :to="switchLocalePath(key)"
            :key="index"
            nuxt
          >
            <v-list-item-title>{{ language }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script lang="ts">
import {defineComponent, useRouter} from "@nuxtjs/composition-api";

export default defineComponent({
  setup(){
    const router = useRouter();

    const languages = {
      en: "English",
      ja: "日本語"
    }

    return{
      languages,
      router
    }
  }

})
</script>

<style scoped>
.logo {
  margin-right: 10px;
  float: left;;
}

.to-home {
  cursor : pointer;
}

v-toolbar-title{
  font-family: arial;
  font-weight: bold;
}

</style>
