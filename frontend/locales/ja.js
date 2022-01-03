export default {
  names: {
    home: 'ホーム',
    id: 'ID',
    no: 'No.',
    projectName: 'プロジェクト名',
    projectDescription: '説明',
    projectPeriod: 'プロジェクト期間',
    startDate: '開始日',
    endDate: '終了日',
    numberOfInspectionAreas: '探査エリア数',
    numberOfInspections: '探査数',
    inspectionDatetime: '探査日時',
    inspectionName: '探査名',
    inspectionArea: '探査エリア',
    inspectionImageData: '探査画像データ',
    inspectionGroundSurface: '探査地表面',
    inspectionDevice: '探査装置',
    memo: '備考',
    numberOfDetections: '検知数',
    aiModel: 'AIモデル',
    createProject: 'プロジェクト登録',
    createInspection: '探査登録',
    projectList: 'プロジェクト一覧',
    inspectionList: '探査一覧',
    analysisResult: '解析結果',
    fileName: 'ファイル名',
    detected: '検知あり',
    noDetected: '検知なし',
    report: 'レポート',
    cancel: 'キャンセル',
    save: '保存する',
    edit: '編集',
    delete: '削除',
    select: '選択',
    preview: 'プレビュー',
    analyze: '解析',
    viewData: 'データを見る',
    status: 'ステータス',
    success: '成功',
    checkResult: '結果確認',
    inspectionOutline: '探査概要',
    otherInput: '他（記入欄）',
    recordList: 'レコード一覧',
    createRecord: 'レコード作成'
  },
  descriptions: {
    selectModel: '解析に使用するモデルを選択'
  },
  groundSurfaceType: {
    asphalt: 'アスファルト',
    concrete: 'コンクリート',
    soil: '土'
  },
  messages: {
    registeredMessage: '登録しました。',
    analyzeMessage: '解析中です。画面を閉じずにお待ち下さい。',
    analyzeMessage2: '解析中です。時間を置いてからアクセスしてください。',
    errorMessage: 'エラーが発生しました。',
    finishAnalyzeMessage: '解析が終了しました。',
    after: (fieldName, _) => `${fieldName}は、開始日以降の日付を入力ください`,
    selected: (fieldName, _) => `${fieldName}を選択してください`
  },
  formats: {
    date: 'YYYY-MM-DD',
    datetime: 'YYYY-MM-DD HH:mm',
  }
}

