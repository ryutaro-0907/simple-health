<template>
  <div>
    <v-breadcrumbs :items="items" large>
      <template v-slot:divider>
        <v-icon>mdi-chevron-right</v-icon>
      </template>
    </v-breadcrumbs>
    <v-divider></v-divider>
  </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
  props: {
    items: {
      type: Array,
      default: []
    }
  },

  setup() {

  },
})
</script>

<style scoped>
.v-breadcrumbs {
  padding: 0px;
}

.v-divider {
  /* margin-right: calc(50% - 50vw);
  margin-left: calc(50% - 50vw); */
  /* margin-left: -20px;
  margin-right: -20px; */
}
</style>
