<template>
  <div>
    <bread-clumbs :items="breadClumbs" />
    <section>
      <button @click="">{{ t('names.edit') }}</button>
      <button @click="">{{ t('names.delete') }}</button>
    </section>
  
  </div>
</template>

<script lang="ts">
import { api } from "~/store/api";
import {
  computed,
  defineComponent, onMounted,
  reactive, ref, useContext,
  useRoute, useRouter
} from "@nuxtjs/composition-api";
import { localize } from "vee-validate";
import { useI18n } from "nuxt-i18n-composable";
import { formatDatetime } from "~/plugins/datetime";
import BreadClumbs from "../../components/BreadClumbs.vue";


export default defineComponent({
  components: { BreadClumbs },
  setup(){
    const i18n = useI18n();
    const route = useRoute();
    const mapRef = ref(null) as any;
    const router = useRouter();

    const data = reactive({
      record: {
        date: '',
        id: '',
        sleep: ''
      }
    })

    const breadClumbs = computed(() => {
      return [
        {
          text: i18n.t('names.projectList'),
          disabled: false,
          href: '/',
        },
        {
          text: data.record.date,
          disabled: true,
          href: `projects/${data.record.id}`,
        },
      ]
    })


    // onMounted(() => {
    //   api.getProjectWithInspections(parseInt(route.value.params.id)).then(response => {
    //     data.obj = response.data;

    //     console.log(data.obj)

    //     data.obj.inspections.data_list.forEach((value, index) => {
    //       data.obj.inspections.data_list[index].order = index + 1;
    //     })

    //     data.markers = data.obj.inspections.data_list.map(inspection =>
    //       {
    //         return {
    //           position: { lat: inspection.area.lat, lng: inspection.area.lng },
    //           label: inspection.order.toString()
    //         }
    //       }
    //     )

    //     mapRef.value.setBounds();
    //   })
    // })

    localize(i18n.locale.value);

    return {
      data,
      ...useI18n(),
      mapRef,
      formatDatetime,
      // toCreateInspection,
      // toInspectionDetail,
      breadClumbs
    }
  }
})
</script>
