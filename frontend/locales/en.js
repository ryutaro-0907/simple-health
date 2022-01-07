export default {
  names: {
    id: 'ID',
    recordList: 'Records',
    createRecord: 'create record',
    created_at: 'created at',
    happiness: 'Happiness',
    motivation: 'Motivatoin',
    workout: 'Workout',
    helped: 'Helped Other',
    carories: 'Carories',
    steps: 'Steps',
    meditation: 'Meditation (min)',
    study: 'Study hours',
    work: 'Work hours'

  },
  messages: {
    registeredMessage: 'Registered.',
    errorMessage: 'Error.',
    after: (fieldName, _) => `Enter the date after the Start Date in ${fieldName}.`
  },
  formats: {
    date: 'll',
    datetime: 'lll',
  }
}
