<template>
  <div>
      <bread-clumbs :items="breadClumbs">
      </bread-clumbs>

    <section>
       <v-container fluid>
        <v-container v-bind:style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }">
          <div class="text-h6">{{ t('names.recordList') }}</div>
          <v-row>
            <v-btn class="ml-auto" depressed right dark small color="#1F787A" @click="toCreateRecord()">
              {{ t('names.createRecord') }}
            </v-btn>
          </v-row>
        </v-container>
          <v-data-table
            :headers="headers"
            :items="data.records"
            class="elevation-1"
          >
            <!-- <template v-slot:item.calories="{ item }">
              <v-chip
                :color="getColor(item.calories)"
                dark
              >
                {{ item.calories }}
              </v-chip>
            </template> -->
          </v-data-table>
       </v-container>

    </section>
  </div>
</template>

<style scoped>
.v-data-table >>> .v-data-table-header {
  background-color: #F4F7F8;
}

.v-data-table >>> tr {
  cursor: pointer;
}

</style>

<script lang="ts">

import { api } from "~/store/api";
import {defineComponent, onMounted, reactive, useRouter} from "@nuxtjs/composition-api";
import { localize } from "vee-validate";
import { useI18n } from "nuxt-i18n-composable";
import BreadClumbs from "../components/BreadClumbs.vue";
import { IRecord } from "~/interfaces/record"


export default defineComponent({
  components: { BreadClumbs },

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
    const editProject =() => {
      console.log('edit project.')
    }
    const deleteProject = () => {
      console.log('delete project.')
    }

    const options = [
      {
        title: i18n.t('names.edit'),
        action: editProject
      },
      {
        title: i18n.t('names.delete'),
        action: deleteProject
      }
    ]

    const toCreateRecord = () => {
      router.push("/records/create");
    }

    const data = reactive({
      records: [] as IRecord[]
    });

    const user_id = 0

    onMounted(() => {
      api.getRecordsByUser(user_id).then(response => {
        response.data.forEach((value) => {
          data.records.push({
            record_id: value.record_id,
            user_id: value.user_id,
            created_at: value.created_at,
            happiness: value.happiness,
            motivation: value.motivation,
            workout: value.workout,
            helped: value.helped,
            carories: value.carories,
            steps: value.steps,
            meditation: value.meditation,
            study: value.study,
            work: value.work
      })
      console.log(data.records)
    })
      }).catch(e => console.log(e));
    })

    const headers = [
          {text: i18n.t('names.created_at'), value: 'created_at'},
          {text: i18n.t('names.happiness'), value: 'happiness'},
          {text: i18n.t('names.motivation'), value: 'motivation'},
          {text: i18n.t('names.workout'), value: 'workout'},
          {text: i18n.t('names.helped'), value: 'helped'},
          {text: i18n.t('names.steps'), value: 'steps'},
          {text: i18n.t('names.meditation'), value: 'meditation'},
          {text: i18n.t('names.study'), value: 'study'},
          {text: i18n.t('names.work'), value: 'work'},

          {text: '', value: 'controls', sortable: false }
    ]

    localize(i18n.locale.value);

    return {
      data,
      toCreateRecord,
      breadClumbs,
      headers,
      options,
      ...useI18n()
    }
  }
})
</script>
