import React from 'react'

export default function RecentList({ items }){
  return (
    <div className="card mt-3">
      <div className="card-body">
        <h5>Recent</h5>
        <ul>
          {items && items.length ? items.map((s,i)=>(<li key={i}><a href={s.original_url}>{s.original_url}</a></li>)) : <li>No recent</li>}
        </ul>
      </div>
    </div>
  )
}
