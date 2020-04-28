import React, {useState, useEffect} from 'react';
import FeatureCard from './components/FeatureCard'
import TasksTable from './components/TasksTable'
import store from './store'


function App(props) {
  const [features, setFetures] = useState([])
  const [taskList, setTasklist] = useState([])
  const [columns, setColumns] = useState([])

  function processTaskList(data) {
    setTasklist(data)
    setColumns(data.columns)
  }
  const noop = e => false
  // function updateTaskList (row) {
  //   const tasks = [row, ...taskList.items]
  //   setTasklist({ ...taskList, items: tasks})
  // }

  useEffect( () => {
    store.getFeatures(setFetures)
  }, [])


    useEffect(() => {
      const timer = setInterval(
        () =>
          store.getTasks(processTaskList)
        ,
        1000)
      return () => clearInterval(timer)
    }, [])

  return (
    <>
      <nav className="navbar navbar-light bg-light">
        <a className="navbar-brand App-brand" href="#"><h1>[F]</h1></a>
      </nav>
      <div className="container-fluid">
        <div className="container-fluid">
            {
              features
                ? features.map(
                  item =>
                    <div className="row App-card App-content">
                      <div className="col-sm-12">
                        <FeatureCard key={item.name} config={item} onSubmit={noop}/>
                      </div>
                    </div>

                ): ''
            }
            <TasksTable columns={columns} taskList={taskList} />
        </div>
      </div>
    </>
  );
}

export default App;
