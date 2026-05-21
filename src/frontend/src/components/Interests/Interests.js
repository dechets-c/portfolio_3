const Interests = ({ interests }) => {
  if (!interests.length) return null

  return (
    <section id='interests' className='section interests'>
      <h2 className='section__title'>Interests</h2>

      <div className='projects__grid'>
        {interests.map((item) => (
          <article key={item.id || item.title} className='project'>
            <h3>{item.title}</h3>
            <p className='project__description'>{item.description}</p>
          </article>
        ))}
      </div>
    </section>
  )
}

export default Interests