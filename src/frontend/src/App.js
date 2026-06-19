import { useContext, useEffect, useState } from 'react'
import { ThemeContext } from './contexts/theme'
import Header from './components/Header/Header'
import About from './components/About/About'
import Projects from './components/Projects/Projects'
import Skills from './components/Skills/Skills'
import Education from './components/Education/Education'
import Interests from './components/Interests/Interests'
import ScrollToTop from './components/ScrollToTop/ScrollToTop'
import Contact from './components/Contact/Contact'
import Admin from './components/Admin/Admin'
import Footer from './components/Footer/Footer'
import { loadPortfolio } from './api'
import './App.css'

const ADMIN_HASH = 'admin'

const App = () => {
  const [{ themeName }] = useContext(ThemeContext)
  const [portfolio, setPortfolio] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [isAdminRoute, setIsAdminRoute] = useState(false)

  useEffect(() => {
    const updateRoute = () => {
      const hash = window.location.hash.replace('#', '').trim().toLowerCase()
      setIsAdminRoute(hash === ADMIN_HASH)
    }

    updateRoute()
    window.addEventListener('hashchange', updateRoute)

    return () => {
      window.removeEventListener('hashchange', updateRoute)
    }
  }, [])

  useEffect(() => {
    let isMounted = true

    const loadData = async () => {
      try {
        const data = await loadPortfolio()
        if (!isMounted) return

        setPortfolio(data)
        setError('')
        document.title = data.header.title
      } catch (loadError) {
        if (!isMounted) return

        setError(loadError.message || 'Unable to load portfolio data')
      } finally {
        if (isMounted) {
          setLoading(false)
        }
      }
    }

    loadData()

    return () => {
      isMounted = false
    }
  }, [])

  if (loading) {
    return (
      <div id='top' className={`${themeName} app`}>
        <main className='app__state'>
          <h1>Chargement du portfolio</h1>
          <p>Connexion au backend en cours...</p>
        </main>
      </div>
    )
  }

  if (error || !portfolio) {
    return (
      <div id='top' className={`${themeName} app`}>
        <main className='app__state'>
          <h1>Impossible de charger le portfolio</h1>
          <p>{error || 'Aucune donnée reçue depuis le backend.'}</p>
        </main>
      </div>
    )
  }

  const { header, about, projects, skills, education, interests, contact } = portfolio

  if (isAdminRoute) {
    return (
      <div id='top' className={`${themeName} app app--admin-page`}>
        <main className='app__admin-page'>
          <div className='app__admin-return'>
            <a className='link' href='/'>
              Retour au portfolio
            </a>
          </div>
          <Admin />
        </main>
      </div>
    )
  }

  const sections = {
    projects: projects.length > 0,
    skills: Object.values(skills).some((group) => group.length > 0),
    education: education.length > 0,
    interests: interests.length > 0,
    contact: Boolean(contact.email),
  }

  return (
    <div id='top' className={`${themeName} app`}>
      <Header header={header} sections={sections} />

      <main>
        <About about={about} />
        <Projects projects={projects} />
        <Skills skills={skills} />
        <Education education={education} />
        <Interests interests={interests} />
        <Contact contact={contact} />
      </main>

      <ScrollToTop />
      <Footer profile={about} />
    </div>
  )
}

export default App
