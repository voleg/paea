import React from "react"
import moment from "moment";

import store from '../store'


function HeaderRow({ columns }) {
  return (
    <tr>
      {
        columns
          ? columns
            .filter(item => !item.hidden)
            .map(
              item =>
                <th scope="col" key={item.id}>
                  { item.name }
                </th>
            )
          : ''
      }
    </tr>
  )
}
const getClasses = status => {
  if (!status.indexOf('error')) return 'table-danger'
  if (!status.indexOf('new')) return 'table-info '
  // if (!status.indexOf('complete')) return 'table-success'
}

function Row({ row, columns, formatters }) {

  return (
    <tr className={getClasses(row.status)}>
      {
        columns.map(col =>
          !col.hidden
          && <td key={col.id}>
            {
              formatters[col.id]
                ? formatters[col.id](row[col.id])
                : row[col.id]
            }
          </td>
        )
      }
    </tr>
  )
}


function TasksTable({columns, taskList}) {
  return (
    <table className="table table-hover table-borderless">
      <thead>
        <HeaderRow columns={columns} />
      </thead>
      <tbody>
      {
        taskList.items && taskList.items.length !== -1
          ? taskList.items.map((row, i) =>
            <Row
              row={row}
              columns={columns}
              key={row.id}
              formatters={{
                created_at: t => moment.utc(t).fromNow(),
                params_display: p => `(${p})`,
                status: s =>
                  <div onClick={e => store.setTaskRestart(row.id)}>
                    {
                      s.indexOf('new') !== -1
                        ? <div className="spinner-grow text-light" role="status">
                          <span className="sr-only">calculating...</span>
                        </div>
                        : s
                    }
                  </div>
                }}/>
          )
          : ''
      }


      </tbody>
    </table>
  )

}

export default TasksTable