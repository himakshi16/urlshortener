import React, { useState } from 'react'

export default function ShortenForm({ onCreated }){
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const submit = async e=>{
    e.preventDefault()
    setLoading(true)
    try{
      const resp = await fetch('/api/shorten/', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ original_url: url }) })
      const data = await resp.json()
      if (resp.ok){
        onCreated && onCreated({ short_code: data.short_code, qr_data: data.qr_data }, data.short_url)
      }
    }catch(err){/*ignore*/}
    setLoading(false)
  }
  return (
    <form onSubmit={submit} className="card">
      <div className="card-body">
        <h4>Shorten</h4>
        <input required placeholder="https://example.com" value={url} onChange={e=>setUrl(e.target.value)} />
        <button className="btn" disabled={loading}>{loading? '...' : 'Shorten'}</button>
      </div>
    </form>
  )
}
