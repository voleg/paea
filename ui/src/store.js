var BASE_URL = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8000';

export default {
  getFeatures: async (okCb, errCB) => {
    return fetch(`${BASE_URL}/api/calculate/algo/features/`)
      .then(res => res.json())
      .then(res => {
        if (res && res.implementations && res.implementations.length !== -1 ) {
          okCb(res.implementations)
        }
      })
  },
  getTasks: async (okCb, errCb) => {
    return fetch(`${BASE_URL}/api/calculate/algo/?limit=50`)
      .then(res => res.json())
      .then(res => {
        if (res && res.total >= 0 ) {
          okCb(res)
        }
      })
  },
  setTask: async (obj, okCb, errCB) => {
    return fetch(`${BASE_URL}/api/calculate/algo/`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(obj)
    })
      .then(res => res.json())
      .then(res => {
        okCb(res)
      })
  },
  setTaskRestart: (id, okCb, errCB) => {
    return fetch(`${BASE_URL}/api/calculate/algo/${id}/restart/`, {
      method: 'POST',
    })
      .then(res => res.json())
      .then(res => {
        okCb && okCb(res)
      })
  }
}