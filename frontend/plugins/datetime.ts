import dayjs from "dayjs";
import localizedFormat from "dayjs/plugin/localizedFormat";

export function formatDatetime(datetime: string, format: string){
    dayjs.extend(localizedFormat);
    return dayjs(datetime).format(format);
}

export function formatDate(){

}
