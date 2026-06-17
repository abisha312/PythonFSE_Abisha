db.feedback.insertMany([
{
  student_id:1,
  course_code:"CS101",
  semester:"2022-ODD",
  rating:5,
  comments:"Excellent teaching",
  tags:["challenging","well-structured","good-examples"],
  submitted_at:new Date("2022-11-30T10:15:00Z"),
  attachments:[
    {filename:"notes.pdf",size_kb:240}
  ]
},
{
  student_id:2,
  course_code:"CS101",
  semester:"2022-ODD",
  rating:4,
  comments:"Good course",
  tags:["challenging","interesting"],
  submitted_at:new Date()
},
{
  student_id:3,
  course_code:"CS101",
  semester:"2022-EVEN",
  rating:3,
  comments:"Average",
  tags:["theory-heavy"],
  submitted_at:new Date(),
  attachments:[
    {filename:"review.docx",size_kb:50}
  ]
},
{
  student_id:4,
  course_code:"CS102",
  semester:"2022-ODD",
  rating:5,
  comments:"Loved DBMS",
  tags:["practical","well-structured"],
  submitted_at:new Date()
},
{
  student_id:5,
  course_code:"CS102",
  semester:"2022-ODD",
  rating:2,
  comments:"Needs improvement",
  tags:["difficult"],
  submitted_at:new Date()
},
{
  student_id:6,
  course_code:"EC101",
  semester:"2021-EVEN",
  rating:1,
  comments:"Poor content",
  tags:["boring"],
  submitted_at:new Date()
},
{
  student_id:7,
  course_code:"ME101",
  semester:"2022-ODD",
  rating:4,
  comments:"Useful",
  tags:["practical"],
  submitted_at:new Date()
},
{
  student_id:8,
  course_code:"CS101",
  semester:"2022-ODD",
  rating:5,
  comments:"Excellent examples",
  tags:["challenging","good-examples"],
  submitted_at:new Date()
},
{
  student_id:9,
  course_code:"CS102",
  semester:"2022-EVEN",
  rating:3,
  comments:"Okay",
  tags:["interesting"],
  submitted_at:new Date()
},
{
  student_id:10,
  course_code:"EC101",
  semester:"2022-ODD",
  rating:4,
  comments:"Well explained",
  tags:["good-examples"],
  submitted_at:new Date()
}
])
/*
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a2fdd1187c39b4cd2490329'),
    '1': ObjectId('6a2fdd1187c39b4cd249032a'),
    '2': ObjectId('6a2fdd1187c39b4cd249032b'),
    '3': ObjectId('6a2fdd1187c39b4cd249032c'),
    '4': ObjectId('6a2fdd1187c39b4cd249032d'),
    '5': ObjectId('6a2fdd1187c39b4cd249032e'),
    '6': ObjectId('6a2fdd1187c39b4cd249032f'),
    '7': ObjectId('6a2fdd1187c39b4cd2490330'),
    '8': ObjectId('6a2fdd1187c39b4cd2490331'),
    '9': ObjectId('6a2fdd1187c39b4cd2490332')
  }
}*/

db.feedback.countDocuments()
//10

db.feedback.find({
    rating:5
})
/*
{
  _id: ObjectId('6a2fdd1187c39b4cd2490329'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a2fdd1187c39b4cd249032c'),
  student_id: 4,
  course_code: 'CS102',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Loved DBMS',
  tags: [
    'practical',
    'well-structured'
  ],
  submitted_at: 2026-06-15T11:08:01.390Z
}
{
  _id: ObjectId('6a2fdd1187c39b4cd2490330'),
  student_id: 8,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent examples',
  tags: [
    'challenging',
    'good-examples'
  ],
  submitted_at: 2026-06-15T11:08:01.390Z
}
db.feedback.find({
    course_code:"CS101",
    tags:"challenging"
})
{
  _id: ObjectId('6a2fdd1187c39b4cd2490329'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a2fdd1187c39b4cd249032a'),
  student_id: 2,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 4,
  comments: 'Good course',
  tags: [
    'challenging',
    'interesting'
  ],
  submitted_at: 2026-06-15T11:08:01.390Z
}
{
  _id: ObjectId('6a2fdd1187c39b4cd2490330'),
  student_id: 8,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent examples',
  tags: [
    'challenging',
    'good-examples'
  ],
  submitted_at: 2026-06-15T11:08:01.390Z
}*/

db.feedback.find(
 {},
 {
   student_id:1,
   course_code:1,
   rating:1,
   _id:0
 }
)
/*
{
  student_id: 1,
  course_code: 'CS101',
  rating: 5
}
{
  student_id: 2,
  course_code: 'CS101',
  rating: 4
}
{
  student_id: 3,
  course_code: 'CS101',
  rating: 3
}
{
  student_id: 4,
  course_code: 'CS102',
  rating: 5
}
{
  student_id: 5,
  course_code: 'CS102',
  rating: 2
}
{
  student_id: 6,
  course_code: 'EC101',
  rating: 1
}
{
  student_id: 7,
  course_code: 'ME101',
  rating: 4
}
{
  student_id: 8,
  course_code: 'CS101',
  rating: 5
}
{
  student_id: 9,
  course_code: 'CS102',
  rating: 3
}
{
  student_id: 10,
  course_code: 'EC101',
  rating: 4
}*/


db.feedback.updateMany(
 {
   rating:{$lt:3}
 },
 {
   $set:{needs_review:true}
 }
)
/*
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}*/


db.feedback.updateMany(
 {
   needs_review:true
 },
 {
   $push:{tags:"reviewed"}
 }
)
/*
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}*/


db.feedback.deleteMany(
 {
   semester:"2021-EVEN"
 }
)
/*
{
  acknowledged: true,
  deletedCount: 1
}*/


db.feedback.aggregate([
{
 $match:{
   semester:"2022-ODD"
 }
},
{
 $group:{
   _id:"$course_code",
   avg_rating:{$avg:"$rating"},
   feedback_count:{$sum:1}
 }
},
{
 $sort:{
   avg_rating:-1
 }
}
])
/*
{
  _id: 'CS101',
  avg_rating: 4.666666666666667,
  feedback_count: 3
}
{
  _id: 'ME101',
  avg_rating: 4,
  feedback_count: 1
}
{
  _id: 'EC101',
  avg_rating: 4,
  feedback_count: 1
}
{
  _id: 'CS102',
  avg_rating: 3.5,
  feedback_count: 2
}*/


db.feedback.aggregate([
{
 $match:{
   semester:"2022-ODD"
 }
},
{
 $group:{
   _id:"$course_code",
   avg_rating:{$avg:"$rating"},
   feedback_count:{$sum:1}
 }
},
{
 $project:{
   _id:0,
   course_code:"$_id",
   average_rating:{
     $round:["$avg_rating",1]
   },
   feedback_count:1
 }
},
{
 $sort:{
   average_rating:-1
 }
}
])
/*
{
  feedback_count: 3,
  course_code: 'CS101',
  average_rating: 4.7
}
{
  feedback_count: 1,
  course_code: 'ME101',
  average_rating: 4
}
{
  feedback_count: 1,
  course_code: 'EC101',
  average_rating: 4
}
{
  feedback_count: 2,
  course_code: 'CS102',
  average_rating: 3.5
}*/


db.feedback.aggregate([
{
 $unwind:"$tags"
},
{
 $group:{
   _id:"$tags",
   count:{
     $sum:1
   }
 }
},
{
 $sort:{
   count:-1
 }
}
])
/*
{
  _id: 'challenging',
  count: 3
}
{
  _id: 'good-examples',
  count: 3
}
{
  _id: 'practical',
  count: 2
}
{
  _id: 'well-structured',
  count: 2
}
{
  _id: 'interesting',
  count: 2
}
{
  _id: 'reviewed',
  count: 1
}
{
  _id: 'theory-heavy',
  count: 1
}
{
  _id: 'difficult',
  count: 1
}*/


db.feedback.createIndex({
 course_code:1
})
//course_code_1

db.feedback.find({
 course_code:"CS101"
}).explain("executionStats")
/*
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'college_nosql.feedback',
    parsedQuery: {
      course_code: {
        '$eq': 'CS101'
      }
    },
    indexFilterSet: false,
    queryHash: '83CE04A5',
    planCacheShapeHash: '83CE04A5',
    planCacheKey: 'E4E1D11D',
    optimizationTimeMillis: 2,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'FETCH',
      nss: 'college_nosql.feedback',
      inputStage: {
        stage: 'IXSCAN',
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 4,
    executionTimeMillis: 31,
    totalKeysExamined: 4,
    totalDocsExamined: 4,
    executionStages: {
      isCached: false,
      stage: 'FETCH',
      nReturned: 4,
      executionTimeMillisEstimate: 7,
      works: 5,
      advanced: 4,
      needTime: 0,
      needYield: 0,
      saveState: 0,
      restoreState: 0,
      isEOF: 1,
      nss: 'college_nosql.feedback',
      docsExamined: 4,
      alreadyHasObj: 0,
      inputStage: {
        stage: 'IXSCAN',
        nReturned: 4,
        executionTimeMillisEstimate: 7,
        works: 5,
        advanced: 4,
        needTime: 0,
        needYield: 0,
        saveState: 0,
        restoreState: 0,
        isEOF: 1,
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        },
        keysExamined: 4,
        seeks: 1,
        dupsTested: 0,
        dupsDropped: 0,
        peakTrackedMemBytes: 0
      }
    }
  },
  queryShapeHash: 'A93905E9C9869DA0264D6D85BC8875D4C698F973B857E2ABAAA6A355A5FCF0CB',
  command: {
    find: 'feedback',
    filter: {
      course_code: 'CS101'
    },
    '$db': 'college_nosql'
  },
  serverInfo: {
    host: 'LAPTOP-3JQMFO6D',
    port: 27017,
    version: '8.3.4',
    gitVersion: '4b03e7daaa316c78b9bf433046dba81637d581c0'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  ok: 1
}
*/ 