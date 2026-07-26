import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import React from 'react'

function App() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🚀 React App Deployed Successfully!</h1>

      <p style={styles.text}>
        This update was deployed automatically using GitHub + Render CI/CD.
      </p>

      <div style={styles.card}>
        <h2>Full Stack Deployment Test</h2>
        <p>✅ Yenesew Enyew Kassie</p>
        <p>✅ React Frontend: Running</p>

        <p>✅ FastAPI Backend: Connected</p>

        <p>✅ Docker Deployment: Working</p>

        <p>✅ Render Auto Deploy: Enabled</p>
      </div>
    </div>
  )
}

const styles = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    fontFamily: 'Arial, sans-serif',
    background: '#f4f6f8',
  },

  title: {
    color: '#2563eb',
  },

  text: {
    fontSize: '18px',
  },

  card: {
    marginTop: '20px',
    padding: '25px',
    background: 'white',
    borderRadius: '10px',
    boxShadow: '0 4px 10px rgba(0,0,0,0.1)',
  },
}

export default App
