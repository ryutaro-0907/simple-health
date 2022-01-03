<template>
  <validation-provider :rules="rules" :name="name" v-slot="{ errors }">
    <v-row>
      <div style="min-width:200px">
        <v-col>
          <v-row>
            <label
              class="text-subtitle1 font-weight-black"
            >
              {{ label }}
              <span class="red--text" v-if="rules.includes('required')">*</span>
            </label>
          </v-row>
          <v-row>
            <small v-if="errors" class="red--text">{{ errors[0] }}</small>
          </v-row>
        </v-col>
      </div>
      <v-text-field
        outlined
        label=""
        v-bind="$attrs"
        :value="value"
        single-line
        hide-details="auto"
        @input="$emit('input', $event)"
        style="max-width:300px"
        dense
      />
    </v-row>
  </validation-provider>
</template>

<style scoped>
.v-text-field--outlined >>> fieldset {
  border-color: rgba(0, 0, 0, 0.2);
}
</style>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api';
import { ValidationProvider } from 'vee-validate';

export default defineComponent({
  components: { ValidationProvider },

  props: {
    label: {
      type: String,
      default: '',
    },
    value: {
      type: String,
      default: '',
    },
    name: {
      type: String,
      default: '',
    },
    rules: {
      type: String,
      default: '',
    },
  },
})
</script>
