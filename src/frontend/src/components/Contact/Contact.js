import './Contact.css'

const Contact = ({ contact }) => {
  if (!contact.email) return null

  return (
    <section className='section contact center' id='contact'>
      <h2 className='section__title'>Contact</h2>
      <a href={`mailto:${contact.email}`}>
        <span type='button' className='btn btn--outline'>
          Email me
        </span>
      </a>
      {(contact.phone || contact.address) && (
        <div className='contact__details'>
          {contact.phone && <p>{contact.phone}</p>}
          {contact.address && <p>{contact.address}</p>}
        </div>
      )}
    </section>
  )
}

export default Contact
