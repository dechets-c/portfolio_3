const Education = ({ education }) => {
  if (!education.length) return null

  return (
    <section id='education' className='section education'>
      <h2 className='section__title'>Education</h2>

      <div className='projects__grid'>
        {education.map((item) => (
          <article key={item.id || item.title} className='project'>
            <h3>{item.title}</h3>
            <p className='project__description'>{item.subtitle}</p>
            <ul className='project__stack'>
              {item.description && (
                <li className='project__stack-item'>{item.description}</li>
              )}
              {item.meta && <li className='project__stack-item'>{item.meta}</li>}
            </ul>
          </article>
        ))}
      </div>
    </section>
  )
}

export default Education