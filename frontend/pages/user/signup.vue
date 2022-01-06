<template>
  <v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1 class="display-1">SignUp</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
          <v-text-field
            prepend-icon="mdi-account-circle"
            label="Username"
            v-model="signUpForm.username"
            />
          <v-text-field
            prepend-icon="mdi-account-circle"
            label="Email"
            v-model="signUpForm.email"
            />
          <v-text-field
            v-bind:type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            label="Password"
            @click:append="showPassword = !showPassword"
            v-model="signUpForm.password"
          />
          <v-card-actions>
            <v-btn class="info" @click="submit">Signup</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-btn class="info" @click="toSignIn()">Already have an account?</v-btn>
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
import { SignUp } from "~/interfaces/user";

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

     const signUpForm = reactive<SignUp>({
       username: '',
       email: '',
       password: ''
    });

    const toSignIn = () => {
      router.push('/user/signin')
    }

    const submit = () => {
      const form: SignUp = {
        username: signUpForm.username,
        email: signUpForm.email,
        password:signUpForm.password
      }
      console.log('username:', form.username)

      api.signUp(form)
        .then(response => {
          console.log(response);
          let user_id = response.data.id
          console.log('user_id', user_id)
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
      toSignIn,
      signUpForm,
      submit
    }
  }
})
</script>
