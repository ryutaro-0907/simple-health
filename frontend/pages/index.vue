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



    // onMounted(() => {
    //   api.allProjectsWithInspections().then(response => {
    //     response.data.forEach((value) => {
    //       data.tableData.push({
    //         id: value.project.id,
    //         projectName: value.project.name,
    //         description: value.project.description,
    //         number_of_areas: value.inspections.number_of_areas,
    //         number_of_inspections: value.inspections.number_of_inspections,
    //         start_date: value.project.period.start_date,
    //         end_date: value.project.period.end_date
    //   })
    //   console.log(data.tableData)
    // })
    //   }).catch(e => console.log(e));
    // })

    // const headers = [
    //       {text: i18n.t('names.projectName'), value: 'projectName'},
    //       {text: i18n.t('names.projectDescription'), value: 'description'},
    //       {text: i18n.t('names.numberOfInspectionAreas'), value: 'number_of_areas'},
    //       {text: i18n.t('names.numberOfInspections'), value: 'number_of_inspections'},
    //       {text: i18n.t('names.startDate'), value: 'start_date'},
    //       {text: i18n.t('names.endDate'), value: 'end_date'},
    //       {text: '', value: 'controls', sortable: false }
    // ]


    localize(i18n.locale.value);

    return {
      // data,
      toCreateRecord,
      breadClumbs,
      // headers,
      options,
      ...useI18n()
    }
  }
})
</script>
