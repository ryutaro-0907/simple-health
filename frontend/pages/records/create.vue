<template>
  <div>
    <bread-clumbs :items="breadClumbs" />
  <validation-observer
    ref="observer"
    v-slot="{ invalid }"
    @submit.prevent="validateBeforeSubmit"
  >
    <form>
      <validation-provider
        v-slot="{ errors }"
        name="happiness"
        rules="required"
      >
        <v-select
          v-model="formData.happiness"
          :items="options.choices"
          :error-messages="errors"
          label="Happiness"
          data-vv-name="happiness"
          required
        ></v-select>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="motivation"
        rules="required"
      >
        <v-select
          v-model="formDatamotivation"
          :items="options.choices"
          :error-messages="errors"
          label="How motivated"
          data-vv-name="motivation"
          required
        ></v-select>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="workout"
        rules="required"
      >
        <v-select
          v-model="formData.workout"
          :items="options.yesNo"
          :error-messages="errors"
          label="Worked out"
          data-vv-name="workout"
          required
        ></v-select>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="hangout"
        rules="required"
      >
        <v-select
          v-model="formData.hangout"
          :items="options.yesNo"
          :error-messages="errors"
          label="Hang out"
          data-vv-name="hangout"
          required
        ></v-select>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="helped"
        rules="required"
      >
        <v-select
          v-model="formData.helped"
          :items="options.yesNo"
          :error-messages="errors"
          label="Helped other"
          data-vv-name="helped"
          required
        ></v-select>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="carories"
        :rules="{
          required: true,
          max: 6,
          regex: '[+-]?([0-9]*[.])?[0-9]+'
        }"
      >
        <v-text-field
          v-model="formData.carories"
          :counter="6"
          :error-messages="errors"
          label="Carories"
          required
        ></v-text-field>
      </validation-provider>
       </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="steps"
        :rules="{
          required: true,
          max: 10,
          regex: '[+-]?([0-9]*[.])?[0-9]+'
        }"
      >
        <v-text-field
          v-model="formData.steps"
          :counter="10"
          :error-messages="errors"
          label="Steps"
          required
        ></v-text-field>
      </validation-provider>
       </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="meditation"
        :rules="{
          required: true,
          max: 4,
          regex: '[+-]?([0-9]*[.])?[0-9]+'
        }"
      >
        <v-text-field
          v-model="formData.meditation"
          :counter="4"
          :error-messages="errors"
          label="Meditation (min)"
          required
        ></v-text-field>
      </validation-provider>
       </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="study"
        :rules="{
          required: true,
          max: 2,
          regex: '[+-]?([0-9]*[.])?[0-9]+'
        }"
      >
        <v-text-field
          v-model="formData.study"
          :counter="2"
          :error-messages="errors"
          label="study hours"
          required
        ></v-text-field>
      </validation-provider>
       </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="work"
        :rules="{
          required: true,
          max: 2,
          regex: '[+-]?([0-9]*[.])?[0-9]+'
        }"
      >
        <v-text-field
          v-model="formData.work"
          :counter="2"
          :error-messages="errors"
          label="Work hours"
          required
        ></v-text-field>
      </validation-provider>


      <v-btn
        class="mr-4"
        type="submit"
        :disabled="invalid"
      >
        submit
      </v-btn>
      <v-btn @click="clear">
        clear
      </v-btn>
    </form>
  </validation-observer>
  </div>
</template>

<style scoped>
.v-text-field--outlined >>> fieldset {
  border-color: rgba(0, 0, 0, 0.2);
}
</style>

<script lang="ts">
import dayjs from "dayjs";
import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
import {computed, defineComponent, reactive, ref, useContext, useRouter} from '@nuxtjs/composition-api';
import { api } from '~/store/api';
import { ICreateRecord } from "~/interfaces/record";
import { useI18n } from 'nuxt-i18n-composable'
import { localize } from 'vee-validate';
import isSameOrAfter from "dayjs/plugin/isSameOrAfter";
import BreadClumbs from "../../components/BreadClumbs.vue";

type FormData = {
  date: string,
  happiness:string,
  motivation:string,
  workout: string,
  helped: string,
  carories: string,
  steps: string,
  meditation: string,
  study: string,
  work: string
}

dayjs.extend(isSameOrAfter);

extend('required', required);
 setInteractionMode('eager')

extend('digits', {
  ...digits,
  message: '{_field_} needs to be {length} digits. ({_value_})',
})

extend('required', {
  ...required,
  message: '{_field_} can not be empty',
})

extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters',
})

extend('regex', {
  ...regex,
  message: '{_field_} {_value_} does not match {regex}',
})


extend('after', {
  params: ['target'],
  validate: (value, params) => {
    const target = (params as Record<string, any>)["target"];
    const date1 = dayjs(value);
    const date2 = dayjs(target);
    if (!date1 || !date2) return false;
    return date1.isSameOrAfter(date2);
  }
})


export default defineComponent({
  components: { ValidationProvider, ValidationObserver, BreadClumbs },

  setup(){
    const router = useRouter();
    const i18n = useI18n();
    const language = computed(() => i18n.t('language'));

    const breadClumbs = [
      {
        text: i18n.t('names.recordList'),
        disabled: false,
        href: '/',
      },
      {
        text: i18n.t('names.createRecord'),
        disabled: true,
        href: '/create_record',
      },
    ]

    const formData = reactive<FormData>({
      date: '',
      happiness: '',
      motivation: '',
      workout: '',
      helped: '',
      carories: '',
      steps: '',
      meditation: '',
      study: '',
      work: ''
    });
    console.log('formData', formData)

    const options = {
      yesNo: [
        'yes',
        'no'
      ],
      choices: [
        '1',
        '2',
        '3',
        '4',
        '5'
      ],
    }

    const message = ref('');
    const menuStartDate = false;
    const menuEndDate = false;


    const validateBeforeSubmit = () => {
      console.log('prevent Before Submit')
      submit()
    }

    const cancel = () => {
      router.back();
    }

    const date = new Date()
    const offset = date.getTimezoneOffset()
    const adjustedDate = new Date(date.getTime() - (offset*60*1000))
    const today = adjustedDate.toISOString().split('T')[0]

    const user_id = '1'
    const submit = () => {
      const createRecord: ICreateRecord = {
        user_id: user_id,
        happiness: formData.happiness,
        motivation: formData.motivation,
        workout: formData.workout,
        helped: formData.helped,
        carories: formData.carories,
        steps: formData.steps,
        meditation: formData.meditation,
        study: formData.study,
        work: formData.work
      }
      console.log('happiness', createRecord.happiness)

      api.createRecord(createRecord)
        .then(response => router.push("/"))
        .catch(e => {
          console.log(e);
          message.value=i18n.t('messages.errorMessage').toString()
        });
    }

    localize(i18n.locale.value);

    return {
      formData,
      menuStartDate,
      menuEndDate,
      message,
      language,
      breadClumbs,
      validateBeforeSubmit,
      options,
      cancel,
      ...useI18n()
    }
  }

})

</script>
