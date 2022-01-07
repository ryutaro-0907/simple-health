import { defineNuxtPlugin } from "@nuxtjs/composition-api";
import axios from "axios";

export default defineNuxtPlugin(ctx => {
  axios.defaults.baseURL = 'http://0.0.0.0:8000/api';
})
