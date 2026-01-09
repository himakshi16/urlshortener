import React, { useState } from 'react'

export default function QRForm({ onResult }){
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const submit = async e=>{
    e.preventDefault()
    setLoading(true)
    try{
      const resp = await fetch('/api/generate-qr/', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ qr_url: url }) })
      const data = await resp.json()
      if (resp.ok){ onResult && onResult(data.qr_data, data.url) }
    }catch(err){console.error(err)}
    setLoading(false)
  }
  return (
    <form onSubmit={submit} className="card">
      <div className="card-body">
        <h4>Generate QR</h4>
        <input required placeholder="https://example.com" value={url} onChange={e=>setUrl(e.target.value)} />
        <button className="btn" disabled={loading}>{loading? '...' : 'Generate'}</button>
      </div>
    </form>
  )
}
