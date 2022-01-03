export interface ICreateRecord {
  date: string;
  happiness:string;
  motivation:string;
  workout: string;
  helped: string;
  carories: string;
  steps: string;
  meditation: string;
  study: string;
  work: string;
}

export interface IRecord {
  id: number;
  date: string;
  sleep: number;
}

export interface IDatetime {
  dt_object: string;
  format?: string;
}
