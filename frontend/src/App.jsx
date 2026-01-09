import React, { useState, useEffect } from 'react'
import ShortenForm from './components/ShortenForm'
import QRForm from './components/QRForm'
import RecentList from './components/RecentList'

export default function App(){
  const [recent, setRecent] = useState([])
  const [created, setCreated] = useState(null)
  const [qrResult, setQrResult] = useState(null)

  useEffect(()=>{
    fetch('/api/recent/')
      .then(r=>r.json())
      .then(d=> setRecent(d.recent || []))
      .catch(()=>{})
  },[])

  return (
    <div className="app container">
      <header>
        <h1>ShortLink</h1>
        <p className="subtitle">Shorten URLs & generate QR codes</p>
      </header>
      <div className="grid">
        <div>
          <ShortenForm onCreated={(item, url)=>{ setCreated({item,url}); setQrResult(null) }} />
          {created && (
            <div className="card output">
              <h4>Shortened url</h4>
              <a href={created.url}>{created.url}</a>
              {created.qr && <div className="qr"><img src={`data:image/png;base64,${created.qr}`} alt="qr"/></div>}
            </div>
          )}
        </div>

        <div>
          <QRForm onResult={(data,url)=>{ setQrResult({data,url}); setCreated(null) }} />
          {qrResult && (
            <div className="card output">
              <h4>Generated QR</h4>
              <a href={qrResult.url}>{qrResult.url}</a>
              <div className="qr"><img src={`data:image/png;base64,${qrResult.data}`} alt="qr"/></div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
