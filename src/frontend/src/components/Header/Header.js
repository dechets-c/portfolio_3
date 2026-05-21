import Navbar from '../Navbar/Navbar'
import './Header.css'

const Header = ({ header, sections }) => {
  const { homepage, title } = header

  return (
    <header className='header center'>
      <h3>
        {homepage ? (
          <a href={homepage} className='link'>
            {title}
          </a>
        ) : (
          title
        )}
      </h3>
      <Navbar sections={sections} />
    </header>
  )
}

export default Header
