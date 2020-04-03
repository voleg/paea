import React, {useState} from 'react';

import store from '../store'


function FeatureCard({config, onSubmit}) {
  const [data, setData] = useState({})

  function submit(event) {
    event.preventDefault()
    const requestData = {
      params: Object.keys(data)
        .map(k=> ({ name:k, value: data[k] }))
    }
    requestData.func_name = config.name
    console.log(requestData)

    store.setTask(requestData, onSubmit)

  }

  const updateParam = key => event => {
    const tmpData = { ...data}
    tmpData[key] = event.target.value
    setData(tmpData)
  }

  return (
    <div className="card rounded-0">
      <div className="card-body">

        <form className="form-inline">
          <div className="form-group mb-2 ">
            <label
              htmlFor={config.name}
              className="sr-only"
            >
              {config.name}
            </label>
            <input
              type="text"
              readOnly
              className="form-control-plaintext"
              id={config.name}
              value={config.name} />
          </div>
          { config.params.map(item =>
            <div className="form-group mx-sm-3 mb-2" key={item.name}>
              <label
                htmlFor={item.name}
                className="sr-only">
                {item.name}
              </label>
              <input
                id={item.name}
                type={item.type}
                onChange={updateParam(item.name)}
                className="form-control rounded-0"
                placeholder={item.name}
              />
            </div>
          )}
          <button
            type="submit"
            className="btn btn-primary rounded-0 mb-2"
            onClick={submit}>
            Run
          </button>
        </form>
      </div>
    </div>
  )
}

export default FeatureCard