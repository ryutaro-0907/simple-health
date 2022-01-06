import axios from 'axios';
import { IRecord, ICreateRecord} from "~/interfaces/record";
import { SignUp, SignIn} from "~/interfaces/user";

export const api = {
  // for /records endpoint.
  async createRecord(data: ICreateRecord) {
    return axios.post('/records', data)
  },

  async getRecordsByUser(user_id: number) {
    return axios.get<IRecord[]>(`/records/${user_id}`)
  },

  async getRecord(id: number) {
    return axios.get<IRecord>(`/records/${id}`);
  },
  // for /users endpoint.
  async signUp(data: SignUp) {
    return axios.post('/users/signup', data)
  },
  async signIn(data: SignIn) {
    return axios.post('/users/signin', data)
  }

}
