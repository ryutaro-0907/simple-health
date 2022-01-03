<template>
  <div>
    <label :for="name">{{ label }}</label>
    <input v-bind="$attrs"
           :name="name"
           :value="value"
           @input="$emit('input', $event.target.value)">
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'

export default defineComponent({
  props: {
    name: {
      type: String,
      default: '',
    },
    label: {
      type: String,
      default: '',
    },
    value: {
      type: String,
      default: '',
    },
  },
})
</script>
