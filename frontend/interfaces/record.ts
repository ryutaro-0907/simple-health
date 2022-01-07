export interface ICreateRecord {
  user_id: number;

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
  record_id: string;

  user_id: number;

  created_at: string;
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

