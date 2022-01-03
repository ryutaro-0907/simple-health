import axios from 'axios';
import { IRecord, ICreateRecord} from "~/interfaces/record";

export const api = {

  async createRecord(data: ICreateRecord) {
    return axios.post('/records', data)
  },

  async getRecords() {
    return axios.get<IRecord[]>('records')
  },

  async getRecord(id: number) {
    return axios.get<IRecord>(`/projects/${id}`);
  },

}
