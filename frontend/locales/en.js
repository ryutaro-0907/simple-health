export default {
  names: {
    id: 'ID',
    recordList: 'Records',
    createRecord: 'create record'

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
