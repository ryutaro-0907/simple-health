<template>
  <v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1 class="display-1">Sign In</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
          <v-text-field
            prepend-icon="mdi-account-circle"
            label="Email"
            v-model="signInForm.email"
            />
          <v-text-field
            v-bind:type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            label="Password"
            @click:append="showPassword = !showPassword"
            v-model="signInForm.password"
          />
          <v-card-actions>
            <v-btn class="info" @click="submit">Sign In</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-btn class="info" @click="signUp">Don't have an account?</v-btn>
          </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</v-app>
</template>


<script lang="ts">

import { api } from "~/store/api";
import {defineComponent, onMounted, reactive, useRouter} from "@nuxtjs/composition-api";
import { localize } from "vee-validate";
import { useI18n } from "nuxt-i18n-composable";
import BreadClumbs from "~/components/BreadClumbs.vue";
import { SignIn } from "~/interfaces/user";

export default defineComponent({
  components: { BreadClumbs },
  data(){
    return {
      showPassword : false,
    }
  },

  setup(){
    const router = useRouter();
    const i18n = useI18n();

    const breadClumbs = [
      {
        text: i18n.t('names.recordList'),
        href: '/',
        color: '#1F787A'
      },
    ]

     const signInForm = reactive<SignIn>({
       email: '',
       password: ''
    });
    const signUp = () => {
      router.push('/user/signup')
    }

    const submit = () => {
      const form: SignIn = {
        email: signInForm.email,
        password:signInForm.password
      }
      console.log('email=:', form.email)

      api.signIn(form)
        .then(response => {
          console.log(response);
          router.push("/")
        })
        .catch(e => {
          console.log(e);
          // message.value=i18n.t('messages.errorMessage').toString()
        });
    }

    localize(i18n.locale.value);

    return {
      ...useI18n(),
      signUp,
      signInForm,
      submit
    }
  }
})
</script>
