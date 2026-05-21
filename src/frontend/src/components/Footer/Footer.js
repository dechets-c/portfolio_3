import './Footer.css'

const Footer = ({ profile }) => (
  <footer className='footer'>
    <a
      href={profile.github || '#top'}
      className='link footer__link'
    >
      Built from backend data
    </a>
  </footer>
)

export default Footer
